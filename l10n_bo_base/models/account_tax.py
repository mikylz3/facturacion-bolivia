# -*- coding: utf-8 -*-

from odoo import models, fields


class AccounTax(models.Model):
    _inherit = 'account.tax'

    catalog5 = fields.Many2one(
        comodel_name='catalogs.sunat',
        string='Catalog 5',
        # domain=[('type_catalog', '=', '5')]
    )
    catalog7 = fields.Many2many(
        comodel_name='catalogs.sunat',
        string='Catalog 7',
        # domain=[('type_catalog', '=', '7')]
    )
    catalog14 = fields.Many2one(
        comodel_name='catalogs.sunat',
        string='Catalog 14',
        # domain=[('type_catalog', '=', '14')]
    )
    catalog16 = fields.Many2one(
        comodel_name='catalogs.sunat',
        string='Catalog 16',
        # domain=[('type_catalog', '=', '16')]
    )
