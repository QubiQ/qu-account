# -*- coding: utf-8 -*-
# © 2018 Qubiq 2010
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from openerp import api, fields, models, _
from openerp.exceptions import UserError
import datetime
_logger = logging.getLogger(__name__)


class account_invoice(models.Model):
    _inherit = 'account.invoice'

    """
    Función que poner por defecto un mandato y una cuenta bancaria
    cuando el campo mandate_required es True.
    """
    @api.multi
    @api.onchange('mandate_required')
    def onchange_mandate_required(self):
        for sel in self:
            if sel.mandate_required:
                if sel.company_id and sel.company_id.partner_id:
                    sel.partner_bank_id = self.env['res.partner.bank'].search([
                        ('company_id', '=', sel.company_id.id),
                        ('partner_id', '=', sel.company_id.partner_id.id)
                        ], limit=1)
                if sel.commercial_partner_id:
                    sel.mandate_id = self.env['account.banking.mandate'].search([
                        ('partner_id', '=', sel.commercial_partner_id.id),
                        ('company_id', '=', sel.company_id.id),
                        ('state', '=', 'valid')
                        ], limit=1)
            else:
                sel.partner_bank_id = None
                sel.mandate_id = None
