# -*- coding: utf-8 -*-
from openerp import http

# class CustomTreeviewColors(http.Controller):
#     @http.route('/custom_treeview_colors/custom_treeview_colors/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_treeview_colors/custom_treeview_colors/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_treeview_colors.listing', {
#             'root': '/custom_treeview_colors/custom_treeview_colors',
#             'objects': http.request.env['custom_treeview_colors.custom_treeview_colors'].search([]),
#         })

#     @http.route('/custom_treeview_colors/custom_treeview_colors/objects/<model("custom_treeview_colors.custom_treeview_colors"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_treeview_colors.object', {
#             'object': obj
#         })