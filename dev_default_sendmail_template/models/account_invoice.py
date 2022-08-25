# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import models


class account_invoice(models.Model):
    _inherit = 'account.move'

    def action_invoice_sent(self):
        res = super(account_invoice, self).action_invoice_sent()
        template_id = False
        template_id = self.company_id.invoice_template and self.company_id.invoice_template.id or False,
        if template_id:
            context = res.get('context')
            context.update({
                'default_use_template': bool(template_id[0]),
                'default_template_id': template_id[0],
            })
            res.update({
                'context': context,
            })
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: