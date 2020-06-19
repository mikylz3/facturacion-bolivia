# -*- coding: utf-8 -*-

{
    'name': "Factura impresa para Bolivia",
    'summary': """
        
    """,
    'description': """
    """,
    'author': "Odootic.com",
    'category': '',
    'version': '0.0.1',
    'depends': [
        'base',
        'account'
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/views/config_report.xml',
        'report/views/factura_computarizada_hoja_carta.xml',

    ],
    'installable': True,
    'application': False,
}