from odoo import models, api, fields


class helpdeskTicketInherit(models.Model):
    _inherit = 'help.ticket'
    _description = "Inherit model to customize Mendagri helpdesk module"

    def _default_employee(self):
        return self.env.user.employee_id

    supervisor_id = fields.Many2one('hr.employee', string='Supervisor', tracking=True)
    employee_id = fields.Many2one('hr.employee', string="Employee", default=_default_employee)


class StageTicketInherit(models.Model):
    _inherit = 'ticket.stage'


    