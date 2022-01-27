from odoo import fields, api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    test = fields.Char(string='Test Field')
