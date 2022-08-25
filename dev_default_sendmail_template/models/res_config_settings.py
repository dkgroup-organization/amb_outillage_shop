# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import models, fields


class res_config_settings(models.TransientModel):
    _inherit = 'res.config.settings'

    sale_quotation_template = fields.Many2one(related='company_id.sale_quotation_template', string='Sale Quotation Template', readonly=False)
    sale_order_template = fields.Many2one(related='company_id.sale_order_template', string='Sale Order Template', readonly=False)
    pur_quotation_template = fields.Many2one(related='company_id.pur_quotation_template', string='Pur. Quotation Template', readonly=False)
    pur_order_template = fields.Many2one(related='company_id.pur_order_template', string='Pur. Order Template', readonly=False)
    invoice_template = fields.Many2one(related='company_id.invoice_template', string='Invoice Template', readonly=False)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: