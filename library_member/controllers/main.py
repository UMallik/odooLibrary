from odoo import http
from odoo.addons.library_management.controllers.controllers import Books


class BooksExtended(Books):
    @http.route()
    def list(self, **kw):
        response = super().list(**kw)
        if kw.get('available'):
            Book = http.request.env['library.books']
            books = Book.search([('is_available','=',True)])
            response.qcontext['books'] = books

        return response