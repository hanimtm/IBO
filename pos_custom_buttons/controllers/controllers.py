# -*- coding: utf-8 -*-
# from odoo import http


# class PosCustomButtons(http.Controller):
#     @http.route('/pos_custom_buttons/pos_custom_buttons/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_custom_buttons/pos_custom_buttons/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_custom_buttons.listing', {
#             'root': '/pos_custom_buttons/pos_custom_buttons',
#             'objects': http.request.env['pos_custom_buttons.pos_custom_buttons'].search([]),
#         })

#     @http.route('/pos_custom_buttons/pos_custom_buttons/objects/<model("pos_custom_buttons.pos_custom_buttons"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_custom_buttons.object', {
#             'object': obj
#         })
