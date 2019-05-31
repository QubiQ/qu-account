# Copyright 2019 Jesus Ramoneda <jesus.ramonedae@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Partner Journal Items",
    "summary": "Partner Journal Items",
    "version": "12.0.1.0.1",
    "category": "Accounting",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "account"
    ],
    "data": [
        "views/res_partner.xml",
    ],
}
