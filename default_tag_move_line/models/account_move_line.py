# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)

from openerp import api, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    """
    Se sobrescribe la funcion 'default_get' y se comprueba si hay
    alguna linea ya, recogiendola por contexto, y le coloca ese valor
    por defecto en las siguientes.
    """

    @api.model
    def default_get(self, vals):
        res = super(AccountMoveLine, self).default_get(vals)
        line = self.env.context.get('line_ids')
        if line:
            res.update({
                        'name': line[0][2]['name'] or ''
                       })
        return res
