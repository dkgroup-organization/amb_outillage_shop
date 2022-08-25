# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettingsUserEmailTemplate(models.TransientModel):
    _inherit = 'res.config.settings'

    default_sale_template_id = fields.Many2one('mail.template', string='Default Sale Email',
                                               domain="[('model', '=', 'sale.order')]",
                                               #config_parameter='sale.default_sale_template',
                                               help="Email template when send SO by Email")

    @api.model
    def get_values(self):
        res = super(ResConfigSettingsUserEmailTemplate, self).get_values()
        res['default_sale_template_id'] = int(self.env['ir.config_parameter'].sudo().get_param('dkg_user_email_template.default_sale_template_id',
                                                                                               default=12
                                                                                               )) or 12
        return res

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].sudo().set_param('dkg_user_email_template.default_sale_template_id',
                                                         self.default_sale_template_id)
        super(ResConfigSettingsUserEmailTemplate, self).set_values()





