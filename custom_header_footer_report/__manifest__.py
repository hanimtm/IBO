# -*- coding: utf-8 -*-
{
    'name': "Custom Report",

    'summary': """+
    """,

    'description': """
        In this module we can to change and modify Header and Footer Report Qweb PDF
    """,

    'author': "Ibrahim Kaddour",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/template.xml',

    ],
    'qweb': [],
    # only loaded in demonstration mode
    'demo': [],
}
