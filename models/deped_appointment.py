from odoo import models, fields

class DepedAppointment(models.Model):
    _name = "deped.appointment"
    _description = "School Principal Appointment Table"
    _order = "start_date desc"

    teacher_id = fields.Many2one("deped.teacher", string="Teacher", required=True)
    school_id = fields.Many2one("deped.school", string="School", required=True)
    start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")
    date_created = fields.Datetime(default=fields.Datetime.now)
    date_updated = fields.Datetime(default=fields.Datetime.now)