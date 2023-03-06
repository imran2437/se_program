# -*- coding: utf-8 -*-
# from odoo import http


# class SeProgram(http.Controller):
#     @http.route('/se_program/se_program', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/se_program/se_program/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('se_program.listing', {
#             'root': '/se_program/se_program',
#             'objects': http.request.env['se_program.se_program'].search([]),
#         })

#     @http.route('/se_program/se_program/objects/<model("se_program.se_program"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('se_program.object', {
#             'object': obj
#         })
