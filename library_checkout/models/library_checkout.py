from odoo import models, api, fields, exceptions
import logging

_logger = logging.getLogger(__name__)

class Checkout(models.Model):
    _name='library.checkout'
    _description='Checkout Request'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    member_id = fields.Many2one('library.member',required=True)
    member_image = fields.Binary(related='member_id.partner_id.image_1920')
    name = fields.Char(related='member_id.partner_id.name')
    user_id = fields.Many2one('res.users','Librarian',
                            default = lambda s: s.env.uid)
    request_date = fields.Date(default=lambda s:fields.Date.today())
    line_ids = fields.One2many('library.checkout.line', 'checkout_id', string='Borrowed Books')
    @api.model
    def _default_stage(self):
        Stage = self.env['library.checkout.stage']
        return Stage.search([], limit=1)

    @api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([], order=order)



    stage_id = fields.Many2one('library.checkout.stage',
                                default=_default_stage,
                                group_expand='_group_expand_stage_id')
    state = fields.Selection(related='stage_id.state')
    checkout_date = fields.Date(readonly=True)
    close_date = fields.Date(readonly=True)
    num_other_checkouts = fields.Integer(compute = '_compute_num_other_checkouts')
    num_books = fields.Integer(compute='_compute_num_books', store=True)
    # Fields for kanban view
    color = fields.Integer('Color Index')
    priority = fields.Selection([('0','Low'),
                                ('1','Normal'),
                                ('2','High')],
                                'Priority',default='1')
    kanban_state = fields.Selection([('normal','In Progress'),
                                    ('blocked','Blocked'),
                                    ('done','Ready for Next Stage')],
                                    'Kanban State',
                                    default='normal')

   


    @api.onchange('member_id')
    def _onchange_member_id(self):
        today = fields.Date.today()
        if self.request_date != today:
            self.request_date = fields.Date.today()
            return{
                'warning':'Changed Request Date',
                'message' :'Request date changed to today'
            }


    @api.model
    def create(self,vals):
        # Code before create
        if 'stage_id' in vals:
            Stage = self.env['library.checkout.stage']
            new_state = Stage.browse(vals['stage_id']).state #no record is created, so we use browse
            if new_state == 'open':
                vals['checkout_date'] = fields.Date.today()
        new_record = super().create(vals)
        # Code after create can use new_record
        if new_record.state == 'done':
            raise exceptions.UserError(
                                 'Not allowed to create checkout in done state.')
        return new_record

    def write(self,vals):
       
        if 'stage_id' in vals:
            Stage = self.env['library.checkout.stage']
            new_state = Stage.browse(vals['stage_id']).state
            if new_state == 'open' and self.state != 'open':
                vals['checkout_date'] = fields.Date.today()
            if new_state == 'done' and self.state != 'done':
                vals['close_date'] = fields.Date.today()
        super().write(vals)

    def button_done(self):
        Stage = self.env['library.checkout.stage']
        done_stage = Stage.search([('state','=','done')], limit = 1)
        for checkout in self:
            checkout.stage_id = done_stage
        return True
    # Checkouts that are in open state excluding the current one 


    def _compute_num_books(self):
        for rec in self:
            rec.num_books = len(rec.line_ids)
    def _compute_num_other_checkouts(self):
        for rec in self:
            domain = [('member_id','=',rec.id),
            ('state','in',['open']),
            ('id','!=', rec.id)]
            rec.num_other_checkouts = self.search_count(domain)
class CheckoutLine(models.Model):
    _name = 'library.checkout.line'
    _description = 'Borrowed Request Line'

    checkout_id = fields.Many2one('library.checkout')
    book_id = fields.Many2one('library.books')