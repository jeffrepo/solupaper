# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _
from datetime import timedelta
import time
import logging


class SolupaperLogistica(models.Model):
    _name = "solupaper.logistica"
    _description = 'Creado para llevar la logística'

    fecha_logistica = fields.Date('Date: ')
    company_id = fields.Many2one(
        comodel_name='res.company',
        required=True, index=True,
        default=lambda self: self.env.company)
    proforma_id = fields.Many2one("sale.order", "Proforma:")
    quantity_containers = fields.Integer("Quantity of containers")
    type_container = fields.Selection([('a', " 20' "), ('b', "40'DC"), ('c', "40'HC"), ('d', "40 NOR")])
    days_free = fields.Selection([('a', '7'), ('b', '14'), ('c', '21')])
    place_deliver = fields.Text(string='Place of  Delivery in Case of  DAP:')
    purchase_order = fields.Many2one("purchase.order", "Purchase order")
    incoterm_id = fields.Many2one("solupaper.incoterm","Solupaper incoterm")
    freight_supplier_id = fields.Many2one('res.partner', "Freigth Forward Information")
    price_quoted = fields.Float("Price Quoted")
    movement_type = fields.Text(string="Movement type")
    pais_destino_id = fields.Many2one('res.country', string="Destination country")
    pais_origen_id = fields.Many2one('res.country', string="Origin country")



    @api.model
    def _get_report_values(self, docids, data=None):
        model = 'solupaper.logistica'
        docs = self.env[model].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
        }


class ReportSolupaperLogistica(models.Model):
    _name = 'report.solupaper.reporte_solupaper_logistica'
    _inherit = 'solupaper.logistica'

    nombre_reporte = 'solupaper.solupaper_logistica_report'
