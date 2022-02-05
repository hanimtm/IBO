from odoo import fields, models, api
# from openerp.tools.amount_to_text_en import amount_to_text


class AMCLPaymentInherit(models.Model):
    _inherit = 'account.payment'

    amount_in_word = fields.Char()
    # compute = 'compute_amount_to_letter'
    # @api.depends('amount')
    # def compute_amount_to_letter(self):
    #     for payment in self:
    #         payment.amount_in_word = payment.currency_id.amount_to_text(amount)

