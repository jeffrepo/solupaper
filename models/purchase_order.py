# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _
import logging

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    sale_order_id = fields.Many2one("sale.order","Proforma")
    descuento = fields.Float("Descuento %")

    @api.onchange('sale_order_id')
    def _onchange_sale_order_id(self):
        for purchase in self:
            po_lines = []
            if purchase.sale_order_id:
                for sale in purchase.sale_order_id:
                    for line in sale.order_line:
                        supplier_taxes = line.product_id.supplier_taxes_id.filtered(lambda t: t.company_id.id == purchase.company_id.id)
                        taxes = purchase.fiscal_position_id.map_tax(supplier_taxes)
                        po_line = (0, 0, {
                            'product_id': line.product_id.id,
                            'name': line.name,
                            'product_qty': line.product_uom_qty,
                            'price_unit': 1,
                            'price_tax': 1,
                            'account_analytic_id': 1,
                            'taxes_id': [(6, 0, taxes.ids)],
                            'date_planned': purchase.date_order,
                            'product_uom': line.product_uom.id
                        })

                        po_lines.append(po_line)

                    purchase.order_line = po_lines
