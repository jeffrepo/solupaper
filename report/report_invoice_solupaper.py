# -*- coding: utf-8 -*-

from odoo import api, models
from datetime import date
from datetime import datetime, date, time, timedelta
import logging

class ReportAbstractAccountMove(models.AbstractModel):
    _name = 'rolsa.abstract.account_move_invoice'

    nombre_reporte = ''

    @api.model
    def _get_report_values(self, docids, data=None):

        logging.warning('Bienvenido para jalar nuevos datos')
        logging.warning(self)
        logging.warning(docids)
        values={
        'total_peso_neto':0
        }
        model = 'account.move'
        docs = self.env[model].browse(docids)
        logging.warning(docs)
        logging.warning(docs.name)
        logging.warning(docs.purchase_id)
        sale_order = None
        for linea in docs.invoice_line_ids:
            logging.warning(linea.quantity)
            logging.warning(linea.sale_line_ids)
            logging.warning(linea.sale_line_ids.name)
            logging.warning(linea.sale_line_ids.order_id)
            sale_order = linea.sale_line_ids.order_id
            values['total_peso_neto']+=linea.quantity

        values['n_orden'] = sale_order.po_customer
        values['puerto'] = sale_order.puerto
        values['intercorm'] = sale_order.solupaper_incoterm_id
        values['orden_cliente'] = sale_order.po_customer_name
        values['plazo_pago'] = sale_order.payment_term_id
        values['representate_venta'] = sale_order.user_id.name


        logging.warning(values)
        logging.warning('')
        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
            'values':values,
        }


class ReportPurchaseOrder1(models.AbstractModel):
    _name = 'report.solupaper.report_account_solupaper'
    _inherit = 'rolsa.abstract.account_move_invoice'

    nombre_reporte = 'solupaper.report_account_solupaper'
