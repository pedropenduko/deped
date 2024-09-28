from odoo import models, fields

class DepedSchoolFunding(models.Model):
    _name = "deped.school.funding"
    _description = "DepEd School Funding Table"
    _order = "create_date desc"

    fund_id = fields.Many2one("deped.funds", string="Funds", required=True)
    school_id = fields.Many2one("deped.school", string="School", required=True)
    date_downloaded = fields.Date("Date Downloaded")
    is_downloaded = fields.Boolean("Status", default=False)
    



