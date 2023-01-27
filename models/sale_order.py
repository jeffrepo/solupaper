# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    #Estos campos al confirmar se muestran de lo contrario se ocultan
    po_customer = fields.Char("Número de orden referencia")
    #quitarl pos_customer_name
    po_customer_name = fields.Char("Orden de compra cliente")
    solupaper_incoterm_id = fields.Many2one("solupaper.incoterm","Solupaper incoterm")

    requerido = fields.Char("Fecha requerido")

    forma_envio = fields.Char("Forma de envío")
    descuento = fields.Float("Descuento %")


    #Estos van en SO
    puerto = fields.Char("Puerto")
     #Estos van en PO
    puerto_destino = fields.Char("Puerto destino")
