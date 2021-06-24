from xmlrpc import client

srv = 'http://localhost:8069'
# public services that do not require login
common = client.ServerProxy('%s/xmlrpc/2/common' % srv)
print(common.version())

db = 'odoo13'
user, pwd = 'utsav.vacker360@gmail.com', 'odoo'
# authenticate method accepts uname and pwd for db and returns the uid to be used
uid = common.authenticate(db,user,pwd,{})
print(uid)

#services that require login

api = client.ServerProxy('%s/xmlrpc/2/object' % srv)

# xmlrpc does not create session so need to pass all info each time
api.execute_kw(db, uid, pwd,'res.partner','search_count',[[]])

domain = [('is_company','=', True)]

api.execute_kw(db,uid,pwd,'res.partner','search_count',[domain])

# does not have browse. use read insted to accept ids and pass fields

api.execute_kw(db,uid,pwd,'res.partner','read',[[14]],{'fields':['id','name']})

# search_read to pass domain and fields

api.execute_kw(db,uid,pwd,'res.partner','search_read',[domain], {'fields':['id','name']})

###xmlrpc does not support None value, so methods that return nothing cannot be called. Use jsonrpc or odoorpc instead###