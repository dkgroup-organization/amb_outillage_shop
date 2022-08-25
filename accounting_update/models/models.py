from odoo import models, fields, api, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError


class Wizard(models.TransientModel):
    _name = 'account.update'
    _description = "Wizard: Quick edit accounting"

    new_date = fields.Date(string="New date", help="If empty, we don't update the date.")
    account_id = fields.Many2one('account.account', string='Account to edit', help="If empty, we don't update the account.")
    new_account_id = fields.Many2one('account.account', string='New account', help="If empty, we don't update the account.")
    journal_id = fields.Many2one('account.journal', string='Journal to edit', help="If empty, we don't update the journal.")
    new_journal_id = fields.Many2one('account.journal', string='New journal', help="If empty, we don't update the journal.")
    new_name = fields.Char(string="New name", help="If empty, we don't update the date.")

    def trans_update_account(self):
        context = dict(self._context or {})
        if context.get('active_ids', False):
            ac_move_ids = self._context.get('active_ids', False)
            for move_id in ac_move_ids:
                if self.new_date:
                    date_due= self.new_date + relativedelta(days =+ 15)
                    query = """
                        UPDATE  
                            account_move
                        SET
                            date = %s,
                            invoice_date = %s,
                            invoice_date_due = %s
                        WHERE
                            id = %s
                        """
                    self.env.cr.execute(query, (self.new_date, self.new_date, date_due, move_id))

                    query = """
                        UPDATE  
                            account_move_line
                        SET
                            date = %s, 
                            date_maturity = %s
                        WHERE
                            move_id = %s
                        """
                    self.env.cr.execute(query, (self.new_date, date_due, move_id))


                if self.account_id and self.new_account_id:
                    query = """
                        UPDATE  
                            account_move_line
                        SET
                            account_id = %s
                        WHERE
                            move_id = %s AND
                            account_id = %s
                        """
                    self.env.cr.execute(query, (self.new_account_id.id, move_id, self.account_id.id,))


                if self.journal_id and self.new_journal_id:
                    query = """
                        UPDATE  
                            account_move
                        SET
                            journal_id = %s
                        WHERE
                            id = %s AND
                            journal_id = %s
                        """
                    self.env.cr.execute(query, (self.new_journal_id.id, move_id, self.journal_id.id,))
                
                if self.new_name and len(ac_move_ids) == 1:
                    name_exist = self.env['account.move'].search([('name', '=', self.new_name)])
                    if name_exist:
                        raise UserError(_('Impossible to update name already exist'))
                    else:
                        query = """
                            UPDATE  
                                account_move
                            SET
                                name = %s
                            WHERE
                                id = %s
                            """
                        self.env.cr.execute(query, (self.new_name, move_id))

        return {'type': 'ir.actions.act_window_close'}
