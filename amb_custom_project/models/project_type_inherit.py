# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

#    is_finish_stage = fields.Boolean(string="Is Finish Stage")
    case_default = fields.Boolean(
        string="Par défaut pour les nouveaux projets",
        help="Si vous cochez ce champ, cette étape vous sera proposée par défaut sur chaque nouveau projet. Il n'affectera pas cette étape à l'existant projets.",
    )