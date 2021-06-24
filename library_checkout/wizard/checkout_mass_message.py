from odoo import models, api, fields,  exceptions

class CHeckoutMassMessage(models.TransientModel):
    _name = 'library.checkout.massmessage'
    _description = 'Send Mass Message to Borrowers'

    checkout_ids = fields.Many2many('library.checkout',
                                    string = 'Checkouts')
    message_subject = fields.Char()
    message_body = fields.Html()

    @api.model
    def default_get(self, field_names):
        defaults = super().default_get(field_names)
        checkout_ids = self.env.context['active_ids']
        defaults['checkout_ids'] = checkout_ids
        return defaults

    def button_send(self):
        
        self.ensure_one()
        # import pdb
        # pdb.set_trace()
        if not self.checkout_ids:
            raise exceptions.UserError('Select atleast one checkout')
        if not self.message_body:
            raise exceptions.UserError('Write a message body')
        for checkout in self.checkout_ids:
            checkout.message_post(
                body = self.message_body,
                subject = self.message_subject,
                subtype = 'mail.mt_comment'
            )