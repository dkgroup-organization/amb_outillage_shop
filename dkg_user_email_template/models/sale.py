# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons.mail.wizard.mail_compose_message import _reopen
from odoo.exceptions import UserError
from odoo.tools.misc import get_lang
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, get_lang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare

class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = 'sale.order'

    def _find_mail_template(self, force_confirmation_template=False):
        template_id = False

        if force_confirmation_template or (self.state == 'sale' and not self.env.context.get('proforma', False)):
            con_template_id = self.env['mail.template'].search([('id', '=', self.env.user.con_template_id.id)]).id
            if con_template_id :
                template_id = con_template_id
            else:
                template_id = int(
                    self.env['ir.config_parameter'].sudo().get_param('sale.default_confirmation_template'))
                template_id = self.env['mail.template'].search([('id', '=', template_id)]).id
                if not template_id:
                    template_id = self.env['ir.model.data'].xmlid_to_res_id('sale.mail_template_sale_confirmation',
                                                                        raise_if_not_found=False)

        if not template_id:
            so_template_id = self.env['mail.template'].search([('id', '=', self.env.user.so_template_id.id)]).id
            if so_template_id :
                template_id = so_template_id
            else:
                co_template_id = self.env['mail.template'].search([('name', 'ilike', self.company_id.name),
                                                          ('model_id', '=', 'sale.order')])
                if co_template_id :
                    template_id = co_template_id.id
                else :
                    template_id = self.env['ir.model.data'].xmlid_to_res_id('sale.email_template_edi_sale', raise_if_not_found=False)
        return template_id
