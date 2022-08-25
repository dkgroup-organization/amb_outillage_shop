# © 2017 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    margin = fields.Float(string="Margin", readonly=True)

    def _select(self):
        select_str = super()._select()
        return "%s, SUM(line.margin_signed) AS margin" % select_str

    # def _groupby(self):
    #     groupby_str = super()._groupby()
    #     return "%s, line.id AS line" % groupby_str