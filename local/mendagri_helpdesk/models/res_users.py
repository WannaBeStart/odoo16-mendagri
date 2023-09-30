from odoo import fields, models, api


class ResUsersInherit(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    employee_id = fields.Many2one('hr.employee', string="Related Employee")
