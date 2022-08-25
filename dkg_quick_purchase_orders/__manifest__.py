# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
#    Globalteckz Software Solutions and Services                             #
#    Copyright (C) 2013-Today(www.globalteckz.com).                          #
#                                                                            #
#    This program is free software: you can redistribute it and/or modify    #
#    it under the terms of the GNU Affero General Public License as          #
#    published by the Free Software Foundation, either version 3 of the      #
#    License, or (at your option) any later version.                         #
#                                                                            #
#    This program is distributed in the hope that it will be useful,         #  
#    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#    GNU Affero General Public License for more details.                     #
#                                                                            #
#                                                                            #
##############################################################################

{
    "name" : "Advanced Quick Purchase Order",
    "version" : "1.0",
    "depends" : ['sale','base','stock','purchase'],
    "author" : "",
    "description": "Create POs from one SO grouped by vendors",
    "website" : "",
    "license" : "Other proprietary",
    "category" : "",

    "category": "",
    "sequence": "1",
    "demo" : [],
    'data'     : [  'security/ir.model.access.csv',
                    'wizard/purchase_order_wizard_view.xml',
                    'views/inherit_sale_order_view.xml',
            ],      
    'installable' : True,
    'application' :  False,


}
