from odoo import api, fields, models, tools, _
from odoo.osv import expression
from odoo.exceptions import AccessError



class HelpdeskTicke2(models.Model):
    _inherit = 'helpdesk.ticket'



    civilite = fields.Selection([('mr', 'Monsieur'), ('mm', 'Madame')], string="Civilité")
    nom = fields.Char(string='Nom', store=True, index=True)
    prenom = fields.Char(string='Prénom', store=True, index=True)
    is_pro = fields.Boolean("je suis un professionnel", store=True)
    tele = fields.Char(string='Téléphone', store=True, index=True)
    numero_commande = fields.Char(string='Numéro de commande', store=True, index=True)
#     commande = fields.Many2one('sale.order', domain="[('partner_id', '=', partner_id)]",store=True)



    
