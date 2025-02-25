
from odoo import models, fields, api

class Libro(models.Model):
    _name = "sge_libreria.libro"
    _description = "Libro"

    name = fields.Char(string="Título", required=True, help="Introduce el título del libro")
    precio = fields.Float(string="Precio", help="Introduce el precio")
    ejemplares = fields.Integer(string="Ejemplares", help="Introduce el número de ejemplares en inventario")
    fecha_compra = fields.Date(string="Fecha de compra", help="Introduce fecha de compra")
    segunda_mano = fields.Boolean(string="Segunda mano", help="Marca si es de segunda mano")
    estado = fields.Selection([
        ('0', 'Bueno'),
        ('1', 'Regular'),
        ('2', 'Malo')
    ], string="Estado", default='0')