# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, Mar 2020

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    warranty = fields.Integer(
        'Warranty period',
        readonly=True,
        states={'draft': [('readonly', False)]},
        help="Warranty delay in year(s)",
        default=2
    )

    partner_shipping_zip_id = fields.Many2one(
        'res.city.zip',
        'ZIP Location',
        related='partner_shipping_id.zip_id',
        readonly=True,
    )
