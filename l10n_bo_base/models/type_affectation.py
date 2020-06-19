# -*- coding: utf-8 -*-


from odoo import models, fields, api


class TypeAffectation(models.Model):
    _name = 'type.affectation'

    code = fields.Char(
        string='Code',
        size=4,
        required=True
    )

    name = fields.Char(
        string='Nombre',
        required=True
    )

    type = fields.Selection([
        ('purchase', 'Compra'),
        ('sale', 'Venta'),
        ('bank', 'Banco'),
        ('others', 'Otros')],
        string='type',
        required=True
    )

    visible = fields.Boolean(
        string='Visible',
        default=False
    )