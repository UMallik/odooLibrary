from odoo import api, models, fields, exceptions

class CheckoutStage(models.Model):
    _name = "library.checkout.stage"
    _description="Checkout Stage"
    _order="sequence,name"

    name=fields.Char()
    sequence= fields.Integer(default=10)
    fold = fields.Boolean()
    active = fields.Boolean(active=True)
    state = fields.Selection([('new', 'New'),
                            ('open','Borrowed'),
                            ('done','Returned'),
                            ('cancel','Cancelled')], default='new')

    