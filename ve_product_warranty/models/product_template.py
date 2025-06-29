from odoo import models,fields,api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    #aplicando herencia del modelo existente
    _inherit = 'product.template'
    
    warranty_months = fields.Integer(
        string ='Warranty months',
        default=0
    )

    
    @api.constrains('warranty_months')
    def check_warranty_months(self):
        for rec in self:
            if rec.warranty_months < 0 or rec.warranty_months > 12:
                raise ValidationError('Not Valid, solo se permite 1 años de garantias')