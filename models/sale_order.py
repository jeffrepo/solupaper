# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    po_customer = fields.Char("PO cliente")
    po_customer_name = fields.Char("Po nombre cliente")
    solupaper_incoterm_id = fields.Many2one("solupaper.incoterm","Solupaper incoterm")
    puerto = fields.Char("Puerto")
    requerido = fields.Char("requerido")
    puerto_destino = fields.Char("Puerto destino")
    forma_envio = fields.Char("Forma de envío")
