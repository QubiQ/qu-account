# -*- coding: utf-8 -*-

{
    'name': 'Account invoice analytic filter',
    'version': '8.0.1.0.0',
    'sequence': 1,
    'summary': 'Account invoice',
    'description': """
Account invoice analytic account filter
=======================

    """,
    'author': 'QubiQ SL',
    'website': 'https://www.qubiq.es',
    'depends': [
                'base',
                'account',
                ],
    'category': 'Account',
    'data': [
                'views/account_invoice_view.xml',
            ],
    'demo': [],
    'installable': True,
}
