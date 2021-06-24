from odoo.tests.common import TransactionCase

class TestWizard(TransactionCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args,**kwargs)
        user_admin = self.env.ref['base.user_admin']
        self.Checkout = self.env['library.checkout'].sudo(user_admin)
        self.Wizard = self.env['library.checkout.massmessage'].sudo(user_admin)
        a_member = self.env['library.member'].create({'name':'JOhn'})
        self.checkout0 = self.Checkout.create({'member_id':a_member.id})

    def test_button_send(self):
        "Send button creates messages on Checkouts"
        msgs_before = len(self.checkout0.message_ids)
        Wizard0 = self.Wizard.with_context(active_ids=self.checkout0.ids)
        wizard0 = Wizard0.create({'message_body':'Hekko'})
        wizard0.button_send()

        msgs_after = len(self.checkout0.message_ids)
        self.assertEqual(msgs_after, msgs_before +1, 'Expected one additional msg in Checkout')