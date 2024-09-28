from odoo import models, fields

class DepedSchool(models.Model):
    _name = "deped.school"
    _description = "DepEd School Table"
    _order = "school_name asc"

    _rec_name = "school_name"
    
    _sql_constraints = [
            ( 
                'unique_school_name',
                'UNIQUE(school_name)',
                'School name must be unique.'
             ),
            (
                'unique_deped_school_id',
                'UNIQUE(deped_school_id)',
                'School ID must be unique.'
            )
    ]

    deped_school_id = fields.Char("School ID", required=True)
    school_name = fields.Char("School Name", required=True)
    school_address = fields.Char("School Address")
    appointment_ids = fields.One2many("deped.appointment", "school_id", string="School Principal")
    fund_ids = fields.One2many("deped.school.funding", "school_id", string="DepEd Funding")


