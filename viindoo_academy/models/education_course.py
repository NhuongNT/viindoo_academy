from odoo import models, fields, api

class EducationCourse(models.Model):
    _name = 'education.course'
    _description = 'Course'

    name = fields.Char(
        string='Course Name',
        required=True)
    
    description = fields.Char(
        string='Course program',
        required=True
        )
    
    class_ids = fields.One2many('education.class','course_id',string='Class')
    # student_ids = fields.One2many('education.student','course_id',string='Student')
    student_ids = fields.Many2many(
    'education.student',
    'course_student_rel',
    column1='course_id',
    column2='student_id',
    string='Students'
    )
    _sql_constraints = [('course_name_unique', 'unique(name)', "The name of Course must be unique!")]
    