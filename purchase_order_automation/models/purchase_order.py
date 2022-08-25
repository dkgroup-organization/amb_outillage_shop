from odoo import api, fields, models, exceptions


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def button_confirm(self):
        imediate_obj=self.env['stock.immediate.transfer']
        invoice_obj = self.env['account.move']
        picking = self.env['stock.picking']
        res = super(PurchaseOrder,self).button_confirm()
        for order in self:
            print("====",order.picking_ids)
            company_id = order.company_id
            if company_id.is_po_delivery_set_to_done:
                order.picking_ids.button_validate()
                imediate_obj.process()
                order.picking_ids.write({'state':'done'})
                if order.picking_ids:
                    for line in order.picking_ids[0].move_ids_without_package:
                        line.quantity_done = line.product_uom_qty
                

            if company_id.create_invoice_for_po and not order.invoice_ids:
                valv=[]
                for data in order.order_line:
                    vals = (0,0,{

                        'display_type': data.display_type,
                        'sequence': data.sequence,
                        'name': '%s: %s' % (data.order_id.name, data.name),
                        'product_id': data.product_id.id,
                        'product_uom_id': data.product_uom.id,
                        'quantity': data.qty_to_invoice,
                        'price_unit': data.price_unit,
                        'tax_ids': [(6, 0, data.taxes_id.ids)],
                        'analytic_account_id': data.account_analytic_id.id,
                        'analytic_tag_ids': [(6, 0, data.analytic_tag_ids.ids)],
                        'move_id': data.order_id.id,
                                        })
                    valv.append(vals)
                    print("====",valv)
                    # sdsd
                    
                invoice_id=invoice_obj.create({'partner_id':order.partner_id.id,
                                'date' : str(self.date_order),
                                'invoice_line_ids':valv,
                                'journal_id' :10,
                            })

                for invoice in order.invoice_ids:
                    invoice.action_invoice_open()
            
        return res  
