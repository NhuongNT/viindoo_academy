from odoo import fields, models

class EducationEnrollment (models.Model):
    _name = 'education.enrollment'
    _description = 'Education Enrollment'
    
    name = fields.Char(string='Ref.', required=True)
#Khi ở đây required = true thì bên wizard cũng phải required = true trường name để đảm bảo khi tạo dữ liệu từ wizard thì trường name không bị để rỗng => lúc truyền sang model eroll không bị vi phạm 

    
    student_id = fields.Many2one('education.student',string='Students')    
    class_id = fields.Many2one('education.class', string='Class')    
    date = fields.Date(string = "The date on which the student enrolls")
    
   

    
    
    

# self.env[model_name].create(value)
# self.env[model_name].create(value_list)
# value = {field:val,field:val}
# value_list = [{field:val,field:val},{field:val,field:val},...]

