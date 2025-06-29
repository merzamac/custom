from odoo import models,fields, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    warranty_months = fields.Integer(
        'Warranty months',
        compute="_compute_warranty_months",
        readonly=False,  
    )
    
    @api.depends('product_id', 'product_id.warranty_months')
    def _compute_warranty_months(self):
        for line in self:
            line.warranty_months = line.product_id.warranty_months or 0