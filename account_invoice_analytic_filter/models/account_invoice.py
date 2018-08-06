# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)

from openerp import models, fields


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    analytic_acc = fields.Many2one(
        string='Analytic account',
        related='invoice_line.account_analytic_id',
        store=True,
    )
