# -*- coding: utf-8 -*-
# © 2009 EduSense BV (<http://www.edusense.nl>)
# © 2011-2013 Therp BV (<http://therp.nl>)
# © 2014-2015 ACSONE SA/NV (<http://acsone.eu>)
# © 2015-2016 Akretion (<http://www.akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)


class AccountPaymentLineCreate(models.TransientModel):
    _inherit = 'account.payment.line.create'

    due_date_init = fields.Date(string="Fecha de vencimiento inicial")

    """
    Se realiza una herencia para filtrar con fecha de inicio a fin de
    vencimiento los apuntes, para ello se busca con un while para no
    forzar con un break el bucle y cierre de forma natural,
    se comprueba que se haya puesto la opcion de fecha de vencimiento
    para buscar en el domain y añadirlo si es necesario.
    """
    @api.multi
    def _prepare_move_line_domain(self):
        domain = super(AccountPaymentLineCreate, self)._prepare_move_line_domain()
        if self.date_type == 'due' and self.due_date_init:
            i = 0
            while i < len(domain):
                if domain[i][0] == 'date_maturity':
                    domain.insert(i-1,
                                  ('date_maturity', '>=', self.due_date_init))
                    i = len(domain)
                i += 1
        return domain
