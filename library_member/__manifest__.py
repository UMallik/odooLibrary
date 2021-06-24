# -*- coding: utf-8 -*-
{
    'name': "Library Member",

    'summary': """
        Manage people who will be able to borrow library books""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Utsav Mallik",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['library_management','mail',],
    'application':False,

    # always loaded
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/member_view.xml',
        'views/book_view.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/book_list_template.xml',
        'views/member_kanban_view.xml',
        'reports/member_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
