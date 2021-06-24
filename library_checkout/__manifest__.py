# -*- coding: utf-8 -*-
{
    'name': "Library Book Borrowing",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Members can borrow books from the library
    """,

    'author': "Utsav Mallik",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['library_member','mail'],
    'application':False,
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/library_checkout_stage.xml',
        'wizard/checkout_mass_message_view.xml',
        'views/views.xml',
        'views/library_menu.xml',
        'views/checkout_view.xml', 
        'views/checkout_kanban_view.xml', 
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
