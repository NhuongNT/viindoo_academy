from odoo import models, fields, api
from pip._vendor.typing_extensions import Self
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class EducationClass(models.Model):
    _name = 'education.class'
    # _inherit = 'mail.thread'#tạo chat box
    _description = 'Education Class'

    name = fields.Char(
        string='Class Name',
        help='The name of the class for identification',
        required=True)
    
    state = fields.Selection (
        [
            ('draft', 'Draft'),#phần tử 1 là các trạng thái - value, phần tử 2 là nhãn thể hiện
            ('confirmed', 'Confirmed'),#bỏ thẻ header thì state dạng tiến trình sẽ chuyển thành dạng selection
            ('done','Done'),
            ('cancel','Cancel')
            ],
        required='True',#bắt buộc pải nhập giá trị (phải nhập trạng thái), nếu không có required thì có thể có giá trị null
        string='Status',
        default='draft',
        help="Status of the class" 
        )
    
    description = fields.Text(string='Description')
    
    active = fields.Boolean (default=True)
    
    start_date = fields.Datetime(
        string='Start Date',
        help='The date which your class will be begin'        
        )
    
    end_date = fields.Datetime(
        string='End Date',
        help='The date which your class will be finish'
        )
    
    student_ids = fields.One2many(
        comodel_name='education.student',
        inverse_name='class_id',
        string='Students',
        help='The Student that belong to the class'
        )
    # reponsible_id = fields.One2many(
    #     comodel_name='res.user',
    #     string='Responsible for the class'
    #     )
    historical_student_ids=fields.Many2many(
        comodel_name='education.student',
        relation='class_education_rel',
        column1='class_id',
        column2='student_id',
        string='Historical Students'
        )
    
    student_count=fields.Integer(string='Studying Student', compute='_compute_student_count')
    
    historical_student_count=fields.Integer(string='Historical Student', compute='_compute_historical_student_count')
    
    company_id=fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=lambda self: self.env.company
        )    
    
    enrollment_ids = fields.One2many(
        comodel_name='education.enrollment',
        inverse_name='class_id',
        string='Enrollment',
        readonly=True
        )
    
    enrollment_student_ids = fields.Many2many('education.student','enrollment_student_rel',compute='_compute_enrollment_student_ids')
    
    course_id = fields.Many2one('education.course',string='Course',required=True)
    
    @api.depends('enrollment_ids')
    def _compute_enrollment_student_ids(self):
        for lop_hoc in self:
            lop_hoc.enrollment_student_ids = self.enrollment_ids.student_id
    

    @api.depends('student_ids')
    def _compute_student_count(self):
        for r in self:
            r.student_count = len(r.student_ids)        
      
    def _compute_historical_student_count(self):
        for r in self:
            r.historical_student_count = len(r.historical_student_ids)  

# Python Constraints:
    @api.constrains('start_date','end_date')    
    def _check_date(self):
        # if self.start_date > self.end_date:
        #     raise ValidationError("The Start Date must be earlier than End Date.")
        for r in self:
            if r.start_date and r.end_date and r.start_date > r.end_date:
                raise UserError("The start date must be earlier than End Date")
#SQL Constraints:
    _sql_constraints =[('class_name_unique', 'unique(name)', "The class name must be unique")]
    # _sql_constraints =[
    #     ('class_name_unique', 'unique(name)', "The class name must be unique"),
    #     ('check_start_date_end_date', 'CHECK(start_date > end_date)', "The Start Date must be earlier than End Date.")
    #     ]
