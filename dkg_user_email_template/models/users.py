# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResUsers(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    so_template_id = fields.Many2one(comodel_name="mail.template", string="Sale Orders Template", required=False, )
    inv_template_id = fields.Many2one(comodel_name="mail.template", string="Invoices Template", required=False, )
    con_template_id = fields.Many2one(comodel_name="mail.template", string="Sale Confirmation Template", required=False, )

