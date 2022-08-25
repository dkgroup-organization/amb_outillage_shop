# Copyright 2016-2017 Akretion (http://www.akretion.com)
# Copyright 2016-2017 Camptocamp (http://www.camptocamp.com/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, exceptions, fields, models, _
import datetime

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    allow_invoicing = fields.Boolean('Permettre la facturation pour ce Client', help='Permettre la facturation',default=False)
    bcd_exige = fields.Boolean('N° de BDC exigé', help='N° de BDC exigé dans la facture',default=False)
    montant_garantie = fields.Float(string='Montant de garantie ',help='montant de garantie qui est transmis par notre factor')
    date_garantie = fields.Date("Date de Garantie")
    #champs personalisés
    x_affacturage = fields.Boolean(string="Affacturage",default=False)
    x_autolqtva = fields.Boolean(string="Auto liquidation de la TVA",default=False)
    x_company_ids = fields.Many2many('res.company',string="Sociétés")
    x_exo = fields.Boolean('Exonération TVA dans Pdf',default=False)
    # x_ice = fields.Char('I.C.E')
    # x_reglement = fields.Selection([
    #         ('cheque', 'Chèque'),
    #         ('vir', 'Virement Bancaire'),
    #         ('paypal', 'Paypal'),
    #         ('prelev', 'Prélèvement'),('carte','Carte Bancaire'),('espese','Espèce')
    #         ],string="Moyen de règlement")
    x_siren = fields.Char('N° Siren')

    @api.onchange('montant_garantie')
    def change_date(self):
        if self.montant_garantie != 0.0:
            self.date_garantie = datetime.date.today()
#self.date_garantie = datetime.date.today().strftime('%Y-%m-%d')
        


