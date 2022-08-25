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


class res_company(models.Model):
    _inherit = 'res.company'

    sale_quotation_template = fields.Many2one('mail.template', string='Sale Quotation Template')
    sale_order_template = fields.Many2one('mail.template', string='Sale Order Template')
    pur_quotation_template = fields.Many2one('mail.template', string='Pur. Quotation Template')
    pur_order_template = fields.Many2one('mail.template', string='Pur. Order Template')
    invoice_template = fields.Many2one('mail.template', string='Invoice Template')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: