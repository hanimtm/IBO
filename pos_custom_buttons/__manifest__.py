# -*- coding: utf-8 -*-
{
    'name': "pos_custom_buttons",

    'summary': """""",

    'description': """
    """,

    'author': "Abdelwahab Ayoubi",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/pos_templates.xml',

    ],
    'qweb': [
        'static/src/xml/pos_product_button_view.xml',
        'static/src/xml/pos_ticket_button_view.xml',
        'static/src/xml/pos_payment_button_view.xml',
        'static/src/xml/pos_counter_button_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
