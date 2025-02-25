from odoo import models, fields, api


class Reserva(models.Model):
    _name = 'skb_reservas.reserva'
    _description = 'Reserva de Sala'

    name = fields.Char('Referencia', required=True)
    sala_id = fields.Many2one('res.users', "Sala", required=True)
    usuario_id = fields.Many2one('res_users', "Usuario", default=lambda self: self.env.user)  
    fecha_reserva = fields.Datetime('Fecha y hora de la reserva', default=datetime.now())  
    estado = fields.Selection([('pendiente', 'Pendiente'), ('confirmado', 'Confirmado'), ('cancelado', 'Cancelado')], default='pendiente', string="Estado")