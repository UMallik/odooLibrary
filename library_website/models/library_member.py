from odoo import models,api,fields

class Member(models.Model):
    _inherit='library.member'
    user_id = fields.Many2one('res.users')