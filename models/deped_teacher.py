from odoo import models, fields, api

class DepedTeacher(models.Model):
    _name = "deped.teacher"
    _description = "DepEd Teacher Table"
    _order = "lastname asc, firstname asc, middlename asc"

    _rec_name = 'fullname'
    
    _sql_constraints = [
            ( 
                'unique_teacher_name',
                'UNIQUE(lastname, firstname, middlename)',
                'Teacher\'s name must be unique.'
             ),
    ]
   
    @api.depends('lastname', 'firstname', 'middlename')
    def _update_fullname(self):
        fullname = ''
        for record in self:
            if record.lastname:
                fullname += record.lastname
            if record.firstname:
                fullname += ", " + record.firstname
            if record.middlename:
                fullname += " " + record.middlename
            record.fullname = fullname
        
    firstname = fields.Char("First Name", required=True)
    middlename = fields.Char("Middle Name")
    lastname = fields.Char("Last Name", required=True)
    fullname = fields.Char(compute="_update_fullname", store=True)
    contact_number = fields.Char("Contact Number")
    
    appointment_ids = fields.One2many("deped.appointment", "teacher_id", string="Appointments")
