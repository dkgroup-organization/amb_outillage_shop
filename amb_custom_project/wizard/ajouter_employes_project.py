# -*- coding: utf-8 -*-
#

from odoo import api, fields, models, _

class ajouter_equipe(models.TransientModel):
    _name = 'ajouter.employes.project'
    _description = 'Ajouter Employees'

    equipe = fields.Many2many('hr.employee', 'equipe_relll', string='Equipe')

    def action_add_employess(self):
        dataa = self.env['project.project'].browse(self._context.get('active_ids', []))
        list_follow = []
        for m in self.equipe:
            dataa.equipe = [(4, m.id)]
            list_follow.append(m.user_partner_id.id)

        dataa.message_subscribe(list_follow)