from odoo import models, fields

class DepedFunds(models.Model):
    _name = "deped.funds"
    _description = "DepEd Funds Table"
    _order = "fund_date desc, fund_name asc"
    
    _rec_name = "fund_name"
    
    
    fund_name = fields.Char("Fund Name", required=True)
    fund_amount = fields.Float("Fund Amount", required=True)
    fund_description = fields.Char("Fund Description")
    fund_code = fields.Char("Fund Code")
    fund_date = fields.Date("Fund Date", required=True)
    fund_ids = fields.One2many("deped.school.funding", "fund_id", string="Recipient Schools")
