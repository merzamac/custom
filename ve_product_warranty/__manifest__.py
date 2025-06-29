# -*- coding: utf-8 -*-
{
    'name': 'Product warranty',
    'summary': 'Product warranty',
    'description': 'Product warranty',
    'author': 'Moises Merza',
    'category': 'product',
    'version': '17.0.0.1',
    'depends': ['product','stock','base','sale'],
    'data': [
        'views/product_template_views.xml',
        'views/product_product_views.xml',
        'views/sale_order_line_views.xml',
        'views/stock_report_view.xml',
    ],
    'license': 'AGPL-3',
    'application':True,
    'installable': True,
    'auto_install': False,
}