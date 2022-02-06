from odoo import fields, models, api
from num2words import num2words

# pip install num2words


class AMCLPaymentInherit(models.Model):
    _inherit = 'account.payment'

    amount_in_word = fields.Char(compute='compute_amount_to_letter')

    @api.depends('amount')
    def compute_amount_to_letter(self):
        for payment in self:
            payment.amount_in_word = num2words(payment.amount)

