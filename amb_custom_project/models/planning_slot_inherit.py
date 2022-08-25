# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class PlanningSlotInherit(models.Model):
    _inherit = 'planning.slot'

    descriptiontask = fields.Html(string='Description' ,related="task_id.description")
    timesheet_timer_start = fields.Datetime("Timesheet Timer Start", related="task_id.timer_start")
    timesheet_timer_pause = fields.Datetime("Timesheet Timer Last Pause" , related="task_id.timer_pause")
    total_hours_spent = fields.Float("Total Hours", related="task_id.total_hours_spent")


    @api.model
    def create(self, values):
        res = super(PlanningSlotInherit, self).create(values)
        if res.task_id:
          data = self.env['project.task'].search([('id','=',res.task_id.id)])
          data.planns = [(4, res.id)]
        return res

    def action_timer_start(self):
      for  record in self:
        if record.task_id:
           return record.task_id.action_timer_start()
        else:
           return False

    def action_timer_pause(self):
      for record in self:
        if record.task_id:
           return record.task_id.action_timer_pause()

        else:
            return False
    def action_timer_resume(self):
      for record in self:
        if record.task_id:
           return record.task_id.action_timer_resume()
        else:
            return False

    def action_timer_stop(self):
      for record in self:
        if record.task_id:
           return record.task_id.action_timer_stop()
        else:
           return False