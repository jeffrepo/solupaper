# -*- coding: utf-8 -*-

from odoo import api, models
from datetime import date
from datetime import datetime, date, time, timedelta
import logging

class ReportAbstractPurchaseOrder(models.AbstractModel):
    _name = 'rolsa.abstract.reporte_purchase_order'

    nombre_reporte = ''

    @api.model
    def _get_report_values(self, docids, data=None):
        model = 'purchase.order'
        docs = self.env[model].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
            # 'a_letras': a_letras.num_a_letras,
            # 'producto': self.producto,
            # 'impuesto_impresos': self.impuesto_impresos,
            # 'impuestos': self.impuestos,
            # 'a_letras_dolares': self.a_letras_dolares
        }


class ReportPurchaseOrder1(models.AbstractModel):
    _name = 'report.solupaper.reporte_purchase_order1'
    _inherit = 'rolsa.abstract.reporte_purchase_order'

    nombre_reporte = 'solupaper.reporte_purchase_order1'
