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
    Se realiza una herencia para que no se pueda borrar una factura
    que ya ha sido validada.
    """
    @api.multi
    def unlink(self):
        for invoice in self:
            if invoice.number:
                raise UserError(_('No puede borrar una factura que ya ha sido validada. Debería abonarla en su lugar.'))
        return super(account_invoice, self).unlink()
