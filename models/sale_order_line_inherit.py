from odoo import models, api, fields


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order.line'

    product_image = fields.Binary(relate='product_id.image_1920')

