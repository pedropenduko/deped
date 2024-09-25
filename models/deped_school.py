from odoo import models, fields

class DepedSchool(models.Model):
    _name = "deped.school"
    _description = "DepEd School Database"
    _order = "school_id asc"

    _sql_constraints = [
            ( 
                'unique_school_name',
                'UNIQUE(school_name)',
                'School name must be unique.'
             ),
            (
                'unique_school_id',
                'UNIQUE(school_id)',
                'School ID must be unique.'
            )
    ]

    school_id = fields.Char("School ID", required=True)
    school_name = fields.Char("School Name", required=True)
    school_address = fields.Char("School Address")
    # principal_assigned = fields.One2many("deped.principal", "school_id", string="School Principal")
    principal_assigned = fields.Many2many("deped.teacher", string="School Principal")
    date_created = fields.Datetime(default=fields.Datetime.now)
    date_updated = fields.Datetime(default=fields.Datetime.now)

