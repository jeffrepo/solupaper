# -*- coding: utf-8 -*-

from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'
    
    
    transferencia_a = fields.Char(string='POR FAVOR HACER PAGO POR TRANSFERENCIA BANCARIA A: ')
    beneficiario = fields.Char(string="Beneficiario: ")
    nombre_banco = fields.Char(string="Nombre del banco")
    numero_cuenta = fields.Char(string="Número de cuenta: ")
    tipo_cuenta = fields.Char(string="Tipo de cuenta: ")
    routing_number = fields.Char(string="Routing number: ")
    numero_swift = fields.Char(string="Nro de swift")
    direccion_beneficiario = fields.Char(string="Dirección del beneficiario")
    telefono = fields.Char(string="Teléfono")