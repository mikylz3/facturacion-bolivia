# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    razonsocial = fields.Char(
        string='Razon Social',
        store=True
    )
