# Copyright 2016-2017 Akretion (http://www.akretion.com)
# Copyright 2016-2017 Camptocamp (http://www.camptocamp.com/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import api, exceptions, fields, models, _

class CedeInvoice(models.TransientModel):
    _name = 'cede.invoice'
    _description = "Cédé Invoice"

    date_cession = fields.Date(string='Date de la cession', required=True,default=fields.Date.context_today)

    def action_cede(self):
        data = self.env['account.move'].browse(self._context.get('active_ids', []))
        cede = "cede"

        for m in data:
            m.date_cession = self.date_cession
            m.update({'state2': cede})
