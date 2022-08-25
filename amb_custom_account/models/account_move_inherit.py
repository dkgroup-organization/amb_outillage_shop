# Copyright 2016-2017 Akretion (http://www.akretion.com)
# Copyright 2016-2017 Camptocamp (http://www.camptocamp.com/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, exceptions, fields, models, _
from odoo.exceptions import UserError

class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    state2 = fields.Selection(selection=[
            ('normal', 'Normal'),
            ('cede', 'Cédé'),
        ], string='Status cession', tracking=True,
        default='normal',compute="_update_state_cession",store=True,copy=False)
    date_cession = fields.Date(string='Date de la cession',copy=False)

    numero_commande = fields.Char('Numéro de bon de commande')

    required_numero_commande = fields.Boolean( string="Joindre au Mail",related="partner_id.bcd_exige")


    @api.depends('state')
    def _update_state_cession(self):
        for rec in self:
            if (rec.state != 'posted'):
                rec.write({'state2': 'normal','date_cession':False})

    def action_post(self):
        if self.partner_id:
            if( not self.partner_id.allow_invoicing):
                raise UserError(("vous n'avez pas le droit de facturation pour ce client, veuillez contacter le comptable pour verifier les informations du client"))
        res = super(AccountMoveInherit, self).action_post()
        return res




