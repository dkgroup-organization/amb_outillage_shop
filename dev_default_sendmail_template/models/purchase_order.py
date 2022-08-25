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


class purchase_order(models.Model):
    _inherit = 'purchase.order'

    def action_rfq_send(self):
        res = super(purchase_order, self).action_rfq_send()
        template_id = False
        if self.state in ['draft', 'send']:
            template_id = self.company_id.pur_quotation_template and self.company_id.pur_quotation_template.id or False,

        else:
            template_id = self.company_id.pur_order_template and self.company_id.pur_order_template.id or False,
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