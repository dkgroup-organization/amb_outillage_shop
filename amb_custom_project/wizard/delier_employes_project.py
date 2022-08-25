# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class delier_emp_projet(models.TransientModel):
    _name = 'delier.employes.projet'
    _description = "delier emp"

    emp = fields.Many2one('hr.employee', string='Employé')

    @api.onchange('emp')
    def _getfilter(self):
        data = self.env['project.project'].browse(self._context.get('active_ids', []))
        return {'domain': {'emp': [('id', 'in', data.equipe.ids)]}}

    def action_delier_emp(self):
        data = self.env['project.project'].browse(self._context.get('active_ids', []))
        list_follows = []
        for m in data:
            m.equipe = [(3, self.emp.id)]
            # m.message_follower_ids = [(6, 0, self.emp.id)]
            list_follows.append(self.emp.user_partner_id.id)
            m.message_unsubscribe(list_follows)