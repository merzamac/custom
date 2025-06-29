from odoo import models,fields

class ProductProduct(models.Model):
    #aplicando herencia del modelo existente
    _inherit = 'product.product'
    
    warranty_months = fields.Integer(
        'Warranty months', 
        related="product_tmpl_id.warranty_months",
        store=True
    )