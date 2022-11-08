# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _


class Solupaper(models.Model):
    _name = "solupaper.incoterm"

    name = fields.Char("Nombre incoterm")
