# -*- coding: utf-8 -*-

from odoo import tools
from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class FacturaComputarizadaHojaCarta(models.AbstractModel):
    _name = 'report.l10n_bo_account.factura_computarizada_hoja_carta'


    @api.model
    def _get_report_values(self, docids, data=None):
        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': self.env['account.move'].browse(docids),
            'report_type': data.get('report_type') if data else '',
        }