# -*- coding: utf-8 -*-

from odoo import models, fields, api


class account_journal(models.Model):
    _inherit = 'account.journal'

    type_document_id = fields.Many2one(
        comodel_name='sunat.table',
        string='Table'
    )

    authorization_number = fields.Char(
        string=u'N° de Autorización'
    )

    date_limit_emision = fields.Date(
        string=u'Límite emisión'
    )

    key_dosing = fields.Char(
        string=u'Llave de Dosificación'
    )

    legend_1 = fields.Char(
        string='Leyenda 1',
    )

    legend_2 = fields.Char(
        string='Leyenda 2',
    )
