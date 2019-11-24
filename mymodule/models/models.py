from odoo import fields, models


class CreditPartner(models.Model):
    _inherit = 'res.partner'
    my_credit_limit = fields.Float('The Credit Limit :')
    my_credit_agent_change = fields.Boolean('Allow agents to modify this limit', default=True)
