# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name' : "AMB CUSTOM PROJECT",
    'version' : "14.0.1.0.0",
    'category' : "Project",
    'summary': 'ce module pour la gestion des Project_employé',
    'description' : """
        Project Details Management
        
        
     """,
    'author' : "KHALLOUT Asmaa",
    'website'  : "https://dkgroup.fr",
    'depends'  : [ 'base','hr','project','sale_timesheet_enterprise','planning'],
    'data'     : [
        'security/ir.model.access.csv',
        'wizard/ajouter_employes_project_view.xml',
        'wizard/delier_employes_project_view.xml',
        'views/project_project_inherit_view.xml',
        'views/project_type_inherit_view.xml',
        'views/project_task_inherit_view.xml',
        'views/planning_slot_inherit_view.xml',
        ],
    'installable' : True,
    'application' :  True,
    
}
