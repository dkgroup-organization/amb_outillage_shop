# -*- coding: utf-8 -*-
{
    'name': "Correction d'écritures comptables",

    'summary': """
        Accounting update""",

    'description': """
        Accounting update
    """,

    'author': "Giuseppe",
    'website': "https://www.bside.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '14.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/views.xml',
    ],
}