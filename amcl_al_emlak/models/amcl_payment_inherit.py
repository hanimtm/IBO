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

    amount_str_before_point = fields.Char(compute='compute_amount_string')
    amount_str_after_point = fields.Char(compute='compute_amount_string')

    @api.depends('amount')
    def compute_amount_string(self):
        for payment in self:
            payment.amount_str_before_point = payment.amount.split('.')[0]
            payment.amount_str_after_point = payment.amount.split('.')[1]
