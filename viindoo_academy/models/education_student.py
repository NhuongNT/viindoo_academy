from odoo import models, fields, api    
from pickle import TRUE

class EducationStudent(models.Model):
    _name="education.student"
    _description="Education Student"
    
    name=fields.Char(
        string='Name',
        required=True
        )
    class_id=fields.Many2one(
        comodel_name='education.class',
        string='Class'
        )
    
    class_ids=fields.Many2many(
        comodel_name='education.class',
        relation='class_education_rel',
        column1='student_id',
        column2='class_id',
        string='Enrolled Classes'
        )
    
    country_id=fields.Many2one(
        comodel_name='res.country',
        string='Country'
        )
    
    ethnicity_id=fields.Many2one(
        comodel_name='res.ethnicity',
        string='Ethnicity'
        )
    
    # ethnicity_code=fields.Char(related='ethnicity_id', store=True)
    
    ethnicity_code2=fields.Char(compute='_compute_ethnicity_code2', store=True)
    
    user_id=fields.Many2one(
        comodel_name='res.user',
        string='User ID relate to Student'
        )
    
    enrollment_ids = fields.One2many(
        comodel_name='education.enrollment',
        inverse_name='student_id',
        string='Enrollment',
        readonly=True
        )

    enrollment_class_ids = fields.Many2many('education.class','enrollment_class_rel', compute='_compute_enrollment_class_ids')
    
    # course_id = fields.Many2one('education.course',string='Course')
    course_ids = fields.Many2many(
        'education.course',
        'course_student_rel',
        column1='student_id',
        column2='course_id',
        string='Courses'
        ) 
    
    @api.depends('enrollment_ids')
    def _compute_enrollment_class_ids(self):
        for std in self:
            std.enrollment_class_ids = self.enrollment_ids.class_id
            
    @api.onchange('ethnicity_id')
    def _onchange_ethnicity_id(self):
            self.country_id = self.ethnicity_id.country_ids[:1]

    @api.depends('ethnicity_id')
    def _compute_ethnicity_code2(self):
        for r in self:
            r.ethnicity_code2 = r.ethnicity_id.code
# #chỉ khi ethnicty_id thì mới chạy code dưới đây
#     @api.depends('ethnicity_id')
#     def _compute_ethnicity_code2(self):
#         for r in self:
#             r.ethnicity_code2 = r.ethnicity_id.code
            
# #chỉ khi code của ethnicty thì mới chạy code dưới đây
#     @api.depends('ethnicity_id.code')
#     def _compute_ethnicity_code2(self):
#         for r in self:
#             r.ethnicity_code2 = r.ethnicity_id.code
