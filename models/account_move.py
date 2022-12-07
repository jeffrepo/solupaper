# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict

from odoo import fields, models
from odoo.tools import float_is_zero, float_compare
from odoo.tools.misc import formatLang


class AccountMove(models.Model):
    _inherit = 'account.move'

    material_proveniente = fields.Char("Material proveniente de: ")
    total_peso_bruto = fields.Float(string="Total Peso Bruto (TM)")


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    rollos_paletas = fields.Char('Rollos / Paletas')
