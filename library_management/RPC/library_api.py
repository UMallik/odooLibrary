from xmlrpc import client

"""
Expose basic CRUD methods
"""


class LibraryAPI():
    # store information to exeute calls on models
    def __init__(self, srv, port, db, user, pwd):
        common = client.ServerProxy('http://%s:%d/xmlrpc/2/common' % (srv,port))

        self.api = client.ServerProxy('http://%s:%d/xmlrpc/2/object' % (srv,port))
        self.uid = common.authenticate(db,user,pwd,{})
        self.pwd = pwd
        self.db = db
        self.model = 'library.books'

    # methods to execute calls
    def execute(self, method, arg_list, kwarg_dict=None):
        return self.api.execute_kw(self.db,self.uid,self.pwd,self.model,method,arg_list,kwarg_dict or {})

    # to retrive
    def search_read(self, text=None):
        domain = [('name','ilike', text)] if text else []
        fields =['id', 'name']
        return self.execute('search_read',[domain,fields])
    
    # to create
    def create(self,title):
        vals = {'name':title}
        return self.execute('create',[vals])

    # to update
    def write(self, title, id):
        vals = {'name': title}
        return self.execute('write',[[id],vals])
    
    def unlink(self,id):
        return self.execute('unlink',[[id]])

    if __name__ == 'main':
        srv,db,port = 'localhost', 'odoo13', 8069
        user, pwd = 'utsav.vacker360@gmail.com', 'odoo'
        api = LibraryAPI(srv,port,db, user,pwd)
        from pprint import pprint
        pprint(api.search_read())

