# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'TMS',
    'version': '0.1',
    'category': 'Sales/Sales',
    'summary': 'Task Management System',
    'description': """
This module contains all about task management system and its features.
    """,
    'depends': [
        'base',
    ],
    'data': [
        # TODO: security.
        "security/ir.model.access.csv",

        # TODO: Views.
        
        "views/task_info.xml",
    ],

    'installable': True,
    'license': 'LGPL-3',
}
