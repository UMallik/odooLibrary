from odoo import models, fields, api

class Member(models.Model):
    _name = "library.member"
    _description = "Library Member"
    _inherit = ['mail.thread','mail.activity.mixin',]

    card_number = fields.Char('Card No.')
    partner_id = fields.Many2one('res.partner', 
                                delegate=True, 
                                on_delete='cascade', 
                                required=True)