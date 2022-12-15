# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _
from datetime import timedelta
import time
import logging


class SolupaperLogistica(models.Model):
    _name = "solupaper.logistica"
    _description = 'Creado para llevar la logística'

    fecha_logistica = fields.Date('Fecha: ')
    company_id = fields.Many2one(
        comodel_name='res.company',
        required=True, index=True,
        default=lambda self: self.env.company)


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
