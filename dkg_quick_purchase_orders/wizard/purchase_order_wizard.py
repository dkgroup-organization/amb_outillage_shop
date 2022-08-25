# -*- coding: utf-8 -*-

import time
from odoo import api, fields, models, _
from datetime import datetime
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError


class createpurchaseorder(models.TransientModel):
	_name = 'create.purchaseorder'
	_description = "Create Purchase Order"

	new_order_line_ids = fields.One2many( 'getsale.orderdata', 'new_order_line_id',string="Order Line")
	partner_id = fields.Many2one('res.partner', string='Vendor')
	date_order = fields.Datetime(string='Order Date', required=True, copy=False, default=fields.Datetime.now)
	
	@api.model
	def default_get(self,  default_fields):
		res = super(createpurchaseorder, self).default_get(default_fields)
		data = self.env['sale.order'].browse(self._context.get('active_ids',[]))
		update = []
		for record in data.order_line:
			update.append((0,0,{
							'product_id' : record.product_id.id,
							'product_uom' : record.product_uom.id,
							'order_id': record.order_id.id,
							'name' : record.name,
							'product_qty' : record.product_uom_qty,
							'price_unit' : record.price_unit,
							'product_subtotal' : record.price_subtotal,
							}))
			print("======",update)

		res.update({'new_order_line_ids':update})
		return res

	def action_create_purchase_order(self):
		self.ensure_one()
		res = self.env['purchase.order']
		value = []
		so = self.env['sale.order'].browse(self._context.get('active_id'))
		pricelist = self.partner_id.property_product_pricelist
		sale_order_name = ""
		valv={}
		for data in self.new_order_line_ids:
			vals = (0,0,{
								'product_id' : data.product_id.id,
								'name' : data.name,
								'product_qty' : data.product_qty,
								'order_id':data.order_id.id,
								'product_uom' : data.product_uom.id,
								'taxes_id' : data.product_id.supplier_taxes_id.ids,
								'date_planned' : data.date_planned,
								'price_unit' : data.price_unit,
								'sale_partner_id':True
								})
			if data.partner_id not in valv:
				valv.update({data.partner_id:[vals]})

			else:
				valv.get(data.partner_id).append(vals)
		sale_order_name = so.name
		print("====valv",valv)
		for val in valv:
			print("===val",val)
			res.create({	'partner_id':val.id,
							'date_order' : str(self.date_order),
							'order_line':valv.get(val),
							'origin' : sale_order_name,
							'partner_ref' : sale_order_name
						})

			
		
		return res


class Getsaleorderdata(models.TransientModel):
	_name = 'getsale.orderdata'
	_description = "Get Sale Order Data"

	new_order_line_id = fields.Many2one('create.purchaseorder')
		
	product_id = fields.Many2one('product.product', string="Product", required=True)
	name = fields.Char(string="Description")
	product_qty = fields.Float(string='Quantity', required=True)
	date_planned = fields.Datetime(string='Scheduled Date', default = datetime.today())
	product_uom = fields.Many2one('uom.uom', string='Product Unit of Measure')
	order_id = fields.Many2one('sale.order', string='Order Reference', ondelete='cascade', index=True)
	price_unit = fields.Float(string='Unit Price', digits='Product Price')
	product_subtotal = fields.Float(string="Sub Total", compute='_compute_total')
	partner_id = fields.Many2one('res.partner', string='Vendor', required = True)

	@api.depends('product_qty', 'price_unit')
	def _compute_total(self):
		for record in self:
			record.product_subtotal = record.product_qty * record.price_unit
