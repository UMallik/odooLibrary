# -*- coding: utf-8 -*-
{
    'name': "library Management",

    'summary': """
        Manage Library bookm catalogue and lendings""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Utsav Mallik",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.1.0-alpha',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application': True,

    # always loaded
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/book_list_template.xml',
        'views/book_category_view.xml',
        'views/book_kanban_view.xml',
        'reports/library_book_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'data/res.partner.csv',
        'data/library.books.csv',
        'data/book_demo.xml',
    ],
}
