from odoo import models, fields, api

class DepedTeacher(models.Model):
    _name = "deped.teacher"
    _description = "DepEd Teacher Table"
    _order = "lastname asc"

    _sql_constraints = [
            ( 
                'unique_teacher_name',
                'UNIQUE(lastname, firstname, middlename)',
                'Teacher\'s name must be unique.'
             ),
    ]

    # @api.model
    # def create(self, vals):
    #     fullname = ''
    #     if vals.get('lastname'):
    #         fullname += vals['lastname']
    #     if vals.get('firstname'):
    #         fullname += ", " + vals['firstname']
    #     if vals.get('middlename'):
    #         fullname += " " + vals['middlename']
    #     vals['fullname'] = fullname
    #     res = super().create(vals)
    #     return res
    
    @api.depends('lastname', 'firstname', 'middlename')
    def _update_fullname(self):
        fullname = ''
        # for record in self:
        if self.lastname:
            fullname += self.lastname
        if self.firstname:
            fullname += ", " + self.firstname
        if self.middlename:
            fullname += " " + self.middlename
        self.fullname = fullname
        
    firstname = fields.Char("First Name", required=True)
    middlename = fields.Char("Middle Name")
    lastname = fields.Char("Last Name", required=True)
    fullname = fields.Char(compute="_update_fullname", store=True)
    contact_number = fields.Char("Contact Number")
    # school_assigned = fields.One2many("deped.principal", "teacher_id", string="School Assignment")
    school_assigned = fields.Many2many("deped.school", string="School Assigned")
    date_created = fields.Datetime(default=fields.Datetime.now)
    date_updated = fields.Datetime(default=fields.Datetime.now)