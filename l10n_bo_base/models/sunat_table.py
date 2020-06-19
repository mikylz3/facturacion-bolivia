# -*- coding: utf-8 -*-

from odoo import fields, models, api


class SunatTable(models.Model):
    _name = 'sunat.table'

    @api.model
    def _get_table(self):
        table = []
        table.append(('{}'.format('tabla10'), '{}'.format('Tabla 10')))
        table.append(('{}'.format('tabla25'), '{}'.format('Tabla 25')))
        table.append(('{}'.format('tabla31'), '{}'.format('Tabla 31')))
        table.append(('{}'.format('tabla8'), '{}'.format('Tabla 8')))
        table.append(('{}'.format('tabla12'), '{}'.format('Tabla 12')))
        table.append(('{}'.format('tabla54'), '{}'.format('Tabla 54')))
        table.append(('{}'.format('tabla01'), '{}'.format('Tabla 01')))
        table.append(('{}'.format('tabla06'), '{}'.format('Tabla 06')))

        return table

    name = fields.Char(
        'Name',
        required=True
    )
    code = fields.Char(
        'Code',
        required=True
    )
    table_type = fields.Selection(
        '_get_table',
        string='Type',
        required=True
    )
