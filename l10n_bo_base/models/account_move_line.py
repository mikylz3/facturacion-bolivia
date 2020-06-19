# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class AccountMoveLineInherit(models.Model):
    _inherit = 'account.move.line'

    type_affectation_id = fields.Many2one(
    comodel_name='type.affectation',
    string='T. afectacion'
    # domain=[('type_catalog', '=', '6')]
    )