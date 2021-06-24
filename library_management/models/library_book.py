from odoo import models, fields, api
from odoo.exceptions import Warning
from odoo.exceptions import ValidationError
import logging

_logger=logging.getLogger(__name__)
class Book(models.Model):
    _name = 'library.books'
    _description = "Book Catalogue"
    _order = "name, date_published desc"
    _sql_constraints = [('library_book_name_uq', 'UNIQUE(name)','Book title mist be unique'),
                        ('library_book_check_date', 'CHECK (date_published <= current_date','Published date should not be in the future'),]

    def _check_isbn(self):
        self.ensure_one()
        digits =[int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6            
            terms = [a * b for a, b in zip(digits[:12], ponderations)]            
            remain = sum(terms) % 10            
            check = 10 - remain if remain != 0 else 0            
            return digits[-1] == check

    #String Fields
    name = fields.Char('Title', required=True, index=True, readonly=False, translate=False)
    isbn = fields.Char('ISBN')
    book_type = fields.Selection([('paper','Paperback'),
                                  ('hard','Hardcover'),
                                  ('elecltronic', 'E-book'),
                                  ('other','Other')],'Type')
    notes = fields.Text('Internal Notes')
    descr = fields.Html('Description')
    
    #Numeric Fields
    copies = fields.Integer(default=1)
    avg_rating = fields.Float('Average Rating', (3,2))
    price = fields.Monetary('Price','currency_id')
    currency_id = fields.Many2one('res.currency')

    #Date and time fields
    date_published = fields.Date()
    last_borrow_date = fields.Datetime('Last Borrowed On', default = lambda self: fields.Datetime.now())

    #others
    active = fields.Boolean('Active?', default=True)
    image = fields.Binary('Cover')
    
    #Relational Field
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')
    category = fields.Many2one('library.book.category', string='Category')
    sub_category = fields.Many2one('library.book.category', string ='Sub-Catgegory')
    publisher_country_id = fields.Many2one('res.country', string="Publisher Country", compute="_compute_publisher_company",
                                            inverse="_inverse_publisher_country",
                                            store=True)
    # search="_search_publisher_country" don't need to use this if computed field has store=Ture



    #Function for Check ISBN Button
    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise Warning('Please provide an ISBN for %s' %book.name)
            if book.isbn and not book._check_isbn():
                raise Warning('%s is an invalid ISBN' %book.isbn)
        return True

    # Function to compute publisher's country
    @api.depends('publisher_id.country_id')
    def _compute_publisher_company(self):
        for book in self:
            self.publisher_country_id = self.publisher_id.country_id

    # Inverse function to set publisher country from book model
    def _inverse_publisher_country(self):
        for book in self:
            _logger.info(book.publisher_country_id)
            book.publisher_id.country_id=book.publisher_country_id 
            _logger.info(book.publisher_id.country_id)
        
    #function to use the search domain when publisher_country_id is referenced
    def _search_publisher_country(self):
        return [('publisher_id.country_id',operator,value)]

    #function to add constraint on ISBN field
    @api.constrains('isbn')
    def _constraints_isbn_validation(self):
        for book in self:
            if book.isbn and not book._check_isbn():
                raise ValidationError('%s is an invalid ISBN' % book.isbn)

class BookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Book Category'
    #Faster queriying -> stores additional information about hierarchy
    _parent_store = True

    name = fields.Char(translate=True, required=True)

    #Hierarchy fields
    parent_id = fields.Many2one('library.book.category','Parent Category',
                                ondelete='restrict')
    parent_path = fields.Char(index=True)

    #For direct children
    child_id = fields.One2many('library.book.category', 'parent_id', 
                                string='Subcategories')

    highlighted_id = fields.Reference([('library.books','Book'),
                                        ('res.partner','Author')])


    