# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    type_document_id = fields.Many2one(
        comodel_name='catalogs.sunat',
        string='Tipo documento',
        domain=[('type_catalog', '=', '6')]
    )
