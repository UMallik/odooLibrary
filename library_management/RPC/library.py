from argparse import ArgumentParser
# from library_api import LibraryAPI

from library_odoorpc import LibraryAPI


parser = ArgumentParser()
parser.add_argument('command', choices=['list','add','set','del'])
# optional arguments
parser.add_argument('params',nargs='*')
args = parser.parse_args()

srv,db,port = 'localhost', 'odoo13', 8069
user, pwd = 'utsav.vacker360@gmail.com', 'odoo'
api = LibraryAPI(srv, port, db,user, pwd)

if args.command == 'add':
    for title in args.params:
        new_id = api.create(title)
        print('Bood added with ID %d' % new_id)
if args.command == 'list':
    # import pdb; pdb.set_trace()
    text = []
    for i in args.params:
        text.append(i)
    books = api.search_read(text[0])
    for book in books:
        print('%(id)d %(name)s' % book)
if args.command == 'set':
    if len(args.params) != 2:
        print("set command requires a Title and ID.")
    book_id, title = int(args.params[0]), args.params[1]
    api.write(title, book_id)
    print('Title set for Book ID %d' % book_id)

if args.command == 'del':
    for param in args.params:
        api.unlink(int(param))
        print('Book with ID %s deleted' % param)
