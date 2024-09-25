from odoo import models, fields

class DepedPrincipal(models.Model):
    _name = "deped.principal"
    _description = "Principal assigned to School Table"

    teacher_id = fields.Many2one("deped.teacher", related="deped_teacher_teacher_id", string="Principal", default=lambda self: self._context.get('fullname'), required=True)
    school_id = fields.Many2one("deped.school", string="School", default=lambda self: self._context.get('school_name'), required=True)
    start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")
    date_created = fields.Datetime(default=fields.Datetime.now)
    date_updated = fields.Datetime(default=fields.Datetime.now)