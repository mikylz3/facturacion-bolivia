# -*- coding: utf-8 -*-

from .CC import codcontr
from .TotalATexto import totalliteral
from odoo import api, fields, models, _
from odoo.fields import Datetime, Date
from odoo.exceptions import ValidationError


class AccountInvoice(models.Model):
    # Hereda todo y modifica encima
    _inherit = 'account.move'

    # Crea el codigodecontrol
    control_code = fields.Char(
        string='Codigo de Control',
        store=True,
        readonly=True,
        compute='_codigo_de_control'
    )

    date_limit_emision = fields.Date(
        string=u'Límite emisión',
        related='journal_id.date_limit_emision'
    )

    authorization_number = fields.Char(
        string=u'N° de Autorización',
        related='journal_id.authorization_number'
    )

    nit = fields.Char(
        string='Nit',
        store=True,
        readonly=True,
        compute='_compute_nit'
    )

    razonsocial = fields.Char(
        string='Razon Social',
        store=True,
        readonly=True,
        compute='_compute_nit'
    )

    totaltexto = fields.Char(
        string='Son :',
        store=False,
        readonly=True,
        compute='_compute_literal'
    )

    @api.depends('amount_total')
    def _compute_literal(self):
        for r in self:
            r.totaltexto = totalliteral(r.amount_total, r.currency_id.name)

    @api.depends('partner_id.vat', 'partner_id.razonsocial')
    def _compute_nit(self):
        for r in self:
            r.nit = r.partner_id.vat
            r.razonsocial = r.partner_id.razonsocial

    # Calcula el Codigo de Control
    @api.depends('journal_id.authorization_number', 'name', 'partner_id.vat', 'invoice_date', 'amount_total',
                 'journal_id.key_dosing')
    def _codigo_de_control(self):
        for r in self:
            r.control_code = codcontr(r.journal_id.authorization_number, r.name, r.partner_id.vat, r.invoice_date,
                                      r.amount_total, r.journal_id.key_dosing)
