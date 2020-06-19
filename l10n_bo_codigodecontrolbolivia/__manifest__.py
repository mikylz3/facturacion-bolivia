# -*- coding: utf-8 -*-
{
    'name': "Codigo de control Bolivia",
	
    'summary': """
        Modulo de Facturación para Bolivia, 
        Codigo de Control, QR, Total a Texto""",
    
	'sequence': 1,
	
    'description': """
        Este Modulo de Facturación para Bolivia, configura el Código de Control, Codigo QR, Total a Texto Literal.
		Algunas modificaciones previas hay que realizar antes de poder facturar de manera computarizada.	
    """,

    'author': "Aldair Venturo Calderon",
    'license': 'AGPL-3',

   
    'category': 'Invoicing Management',
    'version': '0.1',

   
    'depends': ['base', 'account', 'contacts','l10n_bo_base'],

   
    'data': [
        'views/account_journal_cc.xml',
        'views/account_invoice.xml',
    ],

    'qweb': [
    ],
    'application': True,
   
   
}