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

class AccountMove(models.Model):
    _name = "account.move"
    _inherit = "account.move"

    def action_invoice_sent(self):
        """ Open a window to compose an email, with the edi invoice template
            message loaded by default
        """
        self.ensure_one()
        template = self.env.ref('account.email_template_edi_invoice', raise_if_not_found=False)
        lang = False
        if template:
            lang = template._render_lang(self.ids)[self.id]
        if not lang:
            lang = get_lang(self.env).code
        compose_form = self.env.ref('account.account_invoice_send_wizard_form', raise_if_not_found=False)

        inv_user_templ = self.env['mail.template'].search([('id', '=', self.env.user.inv_template_id.id)])
        if inv_user_templ:
            templ = inv_user_templ
            print("USERRRRRRRRRRRRRRRRRRRRR", inv_user_templ, templ, type(templ))
        else:
            inv_comp_templ = self.env['mail.template'].search([('name', 'ilike', self.company_id.name), ('model_id', '=', 'account.move')])
            templ = inv_comp_templ
            print("COMPANYYYYYYYYYYYYYYYYYY", templ, type(templ))

        if templ:
             ctx = dict(
                default_model='account.move',
                default_res_id=self.id,
                # For the sake of consistency we need a default_res_model if
                # default_res_id is set. Not renaming default_model as it can
                # create many side-effects.
                default_res_model='account.move',
                default_use_template=bool(template),
                default_template_id= templ.id,
                default_composition_mode='comment',
                mark_invoice_as_sent=True,
                custom_layout="mail.mail_notification_paynow",
                model_description=self.with_context(lang=lang).type_name,
                force_email=True
             )
        else:
            ctx = dict(
            default_model='account.move',
            default_res_id=self.id,
            # For the sake of consistency we need a default_res_model if
            # default_res_id is set. Not renaming default_model as it can
            # create many side-effects.
            default_res_model='account.move',
            default_use_template=bool(template),
            default_template_id=template and template.id or False,
            default_composition_mode='comment',
            mark_invoice_as_sent=True,
            custom_layout="mail.mail_notification_paynow",
            model_description=self.with_context(lang=lang).type_name,
            force_email=True
         )
        return {
            'name': _('Send Invoice'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'account.invoice.send',
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
            'context': ctx,
         }
