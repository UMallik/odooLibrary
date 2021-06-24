# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


# class LibraryWebsite(http.Controller):
#     @http.route('/library_website/library_website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_website/library_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_website.listing', {
#             'root': '/library_website/library_website',
#             'objects': http.request.env['library_website.library_website'].search([]),
#         })

#     @http.route('/library_website/library_website/objects/<model("library_website.library_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_website.object', {
#             'object': obj
#         })


class Main(http.Controller):
    @http.route('/checkouts', auth="user", website=True)
    def checkouts(self,**kw):
        Checkout = request.env['library.checkout']
        checkouts=Checkout.search([])
        return request.render('library_website.index',{'docs':checkouts})

    @http.route('/checkout/<model("library.checkout"):doc>', auth="user", website="True")
    def checkout(self,doc,**kw):
        return http.request.render('library_website.checkout',{'doc':doc})
