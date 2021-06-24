# -*- coding: utf-8 -*-
{
    'name': "Library Website",

    'summary': """
        Create and check book checkout requests""",

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
    'depends': ['library_checkout','website',],
    'appliction':'False',
    # always loaded
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_member.xml',
        'views/helloworld.xml',
        'views/website_assets.xml',
        'views/checkout_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
