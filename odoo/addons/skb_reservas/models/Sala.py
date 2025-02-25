from odoo import models, fields, api

class Sala(models.Model):
    _name = 'skb_reservas.sala'
    _description = 'Sala de Estudio o Coworking'

    name = fields.Char('Nombre',required=True)
    capacidad = fields.Integer('Capacidad')
    disponible = fields.Boolean('Disponible',default=True)
    reservas_ids = fields.One2many('skb_reservas.reserva', 'sala_id', string="Reservas") 


    