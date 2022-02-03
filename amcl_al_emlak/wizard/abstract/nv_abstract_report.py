from odoo import fields, models, api
import logging
_logger = logging.getLogger(__name__)


# تقرير اقرار عادي
class OrdinaryConfessionReport(models.AbstractModel):
    _name = 'report.amcl_al_emlak.report_sale_order_ordinary_confession_view'
    _description = 'تقرير اقرار عادي'

    @api.model
    def _get_report_values(self, docids, data=None):
        doc_id = data['id']
        model = data['model']
        doc = self.env[data['model']].browse(doc_id)
        # data['info'] = doc.get_lines()
        docargs = {
            'doc_ids': [doc_id],
            'doc_model': model,
            'data': data,
            'docs': [doc],
        }
        return docargs


# نموذج استلام
class ReceiptFormReport(models.AbstractModel):
    _name = 'report.amcl_al_emlak.report_sale_order_receipt_form_view'
    _description = 'نموذج استلام'

    @api.model
    def _get_report_values(self, docids, data=None):
        doc_id = data['id']
        model = data['model']
        doc = self.env[data['model']].browse(doc_id)
        # data['info'] = doc.get_lines()
        docargs = {
            'doc_ids': [doc_id],
            'doc_model': model,
            'data': data,
            'docs': [doc],
        }
        return docargs


# نموذج رقم 4
class FormNb4CommitmentReport(models.AbstractModel):
    _name = 'report.amcl_al_emlak.form_nb_4_commitment_of_individuals'
    _description = 'نموذج رقم 4'

    @api.model
    def _get_report_values(self, docids, data=None):
        doc_id = data['id']
        model = data['model']
        doc = self.env[data['model']].browse(doc_id)
        # data['info'] = doc.get_lines()
        docargs = {
            'doc_ids': [doc_id],
            'doc_model': model,
            'data': data,
            'docs': [doc],
        }
        return docargs


# نموذج إقرار المستخدم
class FormNb4CommitmentReport(models.AbstractModel):
    _name = 'report.amcl_al_emlak.report_user_acknowledgment_form_view'
    _description = 'نموذج إقرار المستخدم'

    @api.model
    def _get_report_values(self, docids, data=None):
        doc_id = data['id']
        model = data['model']
        doc = self.env[data['model']].browse(doc_id)
        # data['info'] = doc.get_lines()
        docargs = {
            'doc_ids': [doc_id],
            'doc_model': model,
            'data': data,
            'docs': [doc],
        }
        return docargs


# #  سند قبض
# class CatchReceiptReport(models.AbstractModel):
#     _name = 'report.amcl_al_emlak.report_catch_receipt_report_view'
#     _description = 'سند قبض'
#
#     @api.model
#     def _get_report_values(self, docids, data=None):
#         doc_id = data['id']
#         model = data['model']
#         doc = self.env[data['model']].browse(doc_id)
#         # data['info'] = doc.get_lines()
#         docargs = {
#             'doc_ids': [doc_id],
#             'doc_model': model,
#             'data': data,
#             'docs': [doc],
#         }
#         return docargs