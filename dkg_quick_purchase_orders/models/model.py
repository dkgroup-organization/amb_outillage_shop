from odoo import models, fields,api,_

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _compute_purchase_count(self):
        for task in self:
            task.purchase_count = self.env['purchase.order'].search_count([('origin','=',self.name)])

    purchase_count = fields.Integer(compute='_compute_purchase_count',string="Purchase Order")


    def action_view_purchase(self):
        return {
                'name':_('Purchase Order'),
                'view_type': 'form',
                'views': [[False,'tree'],[False,'form']],
                'res_model': 'purchase.order',
                'domain':[['origin', '=',self.name]],
                'type': 'ir.actions.act_window',
                
                }

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    partner_id = fields.Many2one('res.partner',string="Vendor")

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    sale_partner_id = fields.Boolean(string="sale")

# class PurchaseOrder(models.Model):
#     _inherit='purchase.order'

#     def create(self,vals):
#         print("=====",self,vals)
#         self
        # xxxxx
        # if vals.get('sale_partner_id')
