# -*- coding: utf-8 -*-

from odoo import api, models
from datetime import date
from datetime import datetime, date, time, timedelta
import logging

class ReportSolupaperLogi(models.AbstractModel):
    _name = 'reporte.solupaper.logistica'
    nombre_reporte = ''
    
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
    _inherit = 'reporte.solupaper.logistica'

    nombre_reporte = 'solupaper.solupaper_logistica_report'
