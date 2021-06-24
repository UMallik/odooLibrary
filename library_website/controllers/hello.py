from odoo import http
from odoo.http import request

class Hello(http.Controller):
    @http.route('/helloworld', auth="public",website=True)
    def helloworld(self,**kw):
        # return('<h1>Hello World</h1>')
        return http.request.render('library_website.helloworld')

    @http.route('/hellocms/<page>',auth="public")
    def hello(self,page,**kw):
        return http.request.render(page)