from odoo import models, fields


class NewSchool(models.Model):
    _name = 'school.new'
    name = fields.Char(string='Name')
    roll_no=fields.Integer(string='Roll No')
    devition=fields.Char('Div')