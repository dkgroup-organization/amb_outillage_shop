# Copyright 2016-2017 Akretion (http://www.akretion.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'AMB CUSTOM ACCOUNT',
    'version': '14.0.1.0.0',
    'summary': 'Technical module permet editer la statut cession de la facture '
    ' State',
    'author': 'KHALLOUT Asmaa',
    'website': 'https://DKGROUP.FR',
    'license': 'AGPL-3',
    'category': 'Generic Modules',
    'depends': ['base','account','sale','purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/cede_invoice_view.xml',
        'views/res_partner_inherit_view.xml',
        'views/account_move_inherit_view.xml',
        'report/template_report_invoice_document_inherit.xml',
    ],
    'installable': True,
}
