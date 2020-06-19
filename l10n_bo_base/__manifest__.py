# -*- coding: utf-8 -*-

{
    'name': "Localización Boliviana base",
    'summary': """
        Coloca las tablas y configuraciones básicas bolivianas para:
        - Diarios
        - Partner
        - Invoice
        - Código de control
    """,
    'description': """
    """,
    'author': "Odootic.com",
    'category': 'localizacion bolivia',
    'version': '0.0.1',
    'depends': [
        'base',
        'account'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/catalogs_sunat_data.xml',
        'views/account_invoice.xml',
        'views/res_partner_view.xml',
        'views/account_tax_view.xml',
        'views/catalogs_sunat_view.xml',
        'views/table_sunat_view.xml',
        'views/type_affectation.xml',
        'wizard/report_book.xml',

    ],
    'installable': True,
    'application': False,
}