# -*- coding: utf-8 -*-
{
    'name': "Control the Credit Limit",
    'summary': "Allows a credit limit to be set for partners",
    'description': """
        This plugin can be used to limit the allowable credit for a partner can have. 
  All new credit transactions are checked against the credit limit and the accumulated owed credit to validate new sale
    """,
    'author': "ERPish",
    'website': "http://www.erpish.com",
    'category': 'Partner',
    'version': '10.0.2',
    'depends': ['account'],
    'data': [
        'views/partner_credit_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}