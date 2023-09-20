# -*- coding: utf-8 -*-
# from odoo import http


# class ProductInherit(http.Controller):
#     @http.route('/product_inherit/product_inherit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_inherit/product_inherit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_inherit.listing', {
#             'root': '/product_inherit/product_inherit',
#             'objects': http.request.env['product_inherit.product_inherit'].search([]),
#         })

#     @http.route('/product_inherit/product_inherit/objects/<model("product_inherit.product_inherit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_inherit.object', {
#             'object': obj
#         })
