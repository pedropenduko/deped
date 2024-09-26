from odoo import models, fields

class DepedSchoolBudget(models.Model):
    __name = "deped.school.budget"
    __description = "DepEd School Budget Database"

    school_id = fields.Char("School ID", required=True)
    school_name = fields.Char("School Name", require=True)
    school_address = fields.Char("School Address")
    date_created = fields.Datetime(default=fields.Datetime.now)
    date_updated = fields.Datetime(default=fields.Datetime.now)

