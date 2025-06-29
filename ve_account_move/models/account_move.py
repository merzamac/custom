from odoo import models,fields


class AccountMove(models.Model):
    #aplicando herencia del modelo existente
    _inherit = 'account.move'
    
    t_invoice= fields.Selection([('a','A'),('b','B'),('c','C')],string='Type of invoice',default='a')
    
    