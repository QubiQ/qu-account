# © 2019 Qubiq 2010
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Qu Filter Payment Orders By Range",
    "version": "11.0.1.0.0",
    "author": "QubiQ",
    "website": "https://www.qubiq.es",
    "category": "account",
    "license": "AGPL-3",
    "depends": [
        "base",
        "account",
        "account_payment_order",
    ],
    "data": [
         "wizards/account_payment_line_create_view.xml",
    ],
    'installable': True,
    'application': False,
}
