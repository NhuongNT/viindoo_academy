from odoo import models, fields

class EducationStudentVip(models.Model):
    _inherit="education.student"
    _description="Education Student Vip"
    

    class_vip_id=fields.Many2one(
        comodel_name='education.class.vip',
        string='Class Vip'
        )
    
    class_ids=fields.Many2many(
        comodel_name='education.class.vip',
        relation='class_education_vip_rel',
        column1='student_id',
        column2='class_id',
        string='Enrolled Classes'
        )

