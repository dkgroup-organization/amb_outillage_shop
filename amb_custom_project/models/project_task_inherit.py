# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class ProjectTaskInherit(models.Model):
    _inherit = 'project.task'

#    planns = fields.Many2many('planning.slot', 'palann_id2', string="Planning")
    localisation = fields.Char('Localisation Axes', copy=False, help="Example 33.578921, -7.616295")
    #google_map_long = fields.Char(string="", required=False, )
    #google_map_lat = fields.Char(string="", required=False, )
    planns = fields.Many2many(comodel_name="planning.slot", string="Plans", )
    pieces_joint = fields.Many2many(comodel_name="ir.attachment", string="Attachment")

    def action_add_plann(self):
        view_id = self.env.ref('planning.planning_view_form').id
        # context = {'project_id':self.project_id,'task_id':self.id}
        context = dict()
        context.update({
            'default_project_id':self.project_id.id,
            'default_task_id':self.id,
            'default_employee_id':self.user_id.employee_id.id,
        })
        return {
                'name':'Planning',
                'view_mode': 'form',
                'views' : [(view_id,'form')],
                'res_model':'planning.slot',
                'view_id':view_id,
                'type':'ir.actions.act_window',
                'target':'new',
                'context':context,
                }

