# -*- coding: utf-8 -*-
# from odoo import http


# class ViindooSchool(http.Controller):
#     @http.route('/accounting/accounting', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/accounting/accounting/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('accounting.listing', {
#             'root': '/accounting/accounting',
#             'objects': http.request.env['accounting.accounting'].search([]),
#         })

#     @http.route('/accounting/accounting/objects/<model("accounting.accounting"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('accounting.object', {
#             'object': obj
#         })
