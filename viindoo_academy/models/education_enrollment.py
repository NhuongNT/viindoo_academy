from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError

class EducationEnrollment (models.Model):
    _name = 'education.enrollment'
    _description = 'Education Enrollment'
    
    name = fields.Char(string='Ref.', required=True)
#Khi ở đây required = true thì bên wizard cũng phải required = true trường name để đảm bảo khi tạo dữ liệu từ wizard thì trường name không bị để rỗng => lúc truyền sang model eroll không bị vi phạm 

    
    student_id = fields.Many2one('education.student',string='Students')
      
    class_id = fields.Many2one('education.class', string='Class')    
    date = fields.Date(string = "The date on which the student enrolls")
    # _sql_constraints = [
    #     ('student_per class_unique',
    #      'UNIQUE(student_id,class_id)',
    #      "The student must be unique per class!"),
    #     ]
    
    @api.constrains('class_id','student_id')
    def _check_class_state(self):
        for r in self:
            if r.class_id.state != 'confirmed':
                raise UserError(
                    _("You may not able to enroll a student into the class %s whose the status is not confirmed")
                                % r.class_id.name
                                )
#wrong implementation of translation function
#raise UsserError(_("You may not able to enroll a student into the class %s whose the status is not confirmed" % cls.class_id.name))
            if r.student_id and r.class_id and r.class_id.state != 'cancelled':
                overlap = self.search(
                    domain=[
                        ('id', '!=', r.id),
                        ('student_id','=', r.student_id.id),
                        ('class_id','=', r.class_id.id),
                        ('class_id.state', '!=', 'cancelled')
                        ],
                    limit=1,
                    )
                if overlap:
                    raise UserError(
                        _("You may not able to enroll the student %s into the class %s twice")
                        % (r.student_id.name, r.class_id.name)
                        )
            

    # "dvfnjnvj %s dfnvjdsnj %s as sjfie" %(value1, value2)
    # "dvfnjnvj {} dfnvjdsnj {} as sjfie" .format(value1, value2)
    # "dvfnjnvj {1} dfnvjdsnj {0} as sjfie" .format(value1, value2)
    # "dvfnjnvj {v1} dfnvjdsnj {v2} as sjfie" .format(v1=value1, v2=value2)
   

    
    
    

# self.env[model_name].create(value)
# self.env[model_name].create(value_list)
# value = {field:val,field:val}
# value_list = [{field:val,field:val},{field:val,field:val},...]

