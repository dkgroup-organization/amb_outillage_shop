# -*- coding: utf-8 -*-
#

from odoo import api, fields, models, _

class pose_info(models.Model):
    _inherit = 'project.project'



    equipe = fields.Many2many('hr.employee','equipe_rel22', string='Equipe')
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip')
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')
    reference_chantier = fields.Char(string="Reference chantier")
    date_debut = fields.Datetime(string='Date de Démarrage Chantier', required=False, copy=False,
                                 default=fields.Datetime.now)
    date_fin = fields.Datetime(string='Date de fin de chanier', required=False, copy=False, default=fields.Datetime.now)
    pieces_joint = fields.Many2many('ir.attachment','project_project_rel2', string='Piéces jointes', store=True)
    x_contact = fields.Many2one('res.partner',string="Contact client")
    type_ids = fields.Many2many(default=lambda self: self._get_default_type_common())

    def _get_default_type_common(self):
          ids = self.env["project.task.type"].search([("case_default", "=", True)])
          return ids


    state = fields.Selection([
        ('draft', 'Projet Valide'),
        ('prod', 'Production'),
        ('fact', 'Facturation'),
        ('done', 'Terminé'),
        ('cancel', 'Annuler'),
    ], default='draft')

    def prod(self):
        self.write({
            'state': 'prod',
        })

    def fact(self):
        self.write({
            'state': 'fact',
        })

    def done(self):
        self.write({
            'state': 'done',
        })

    def cancel(self):
        self.write({
            'state': 'cancel',
        })

    def draft(self):
        self.write({
            'state': 'draft',
        })
