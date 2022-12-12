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
    
    user_id=fields.Many2one(
        comodel_name='res.user',
        string='User ID relate to Student'
        )
    #
    # ethnicity_code=fields.Char(related='ethnicty_id.code', store=True)
#khi thay đổi thì sẽ hồi tố tất cả các bản ghi trước đó
    #
    # ethnicity_code2=fields.Char(compute='_compute_ethnicity_code2', store=True)
#nếu compute mà k store thì nó giống như related
# nếu không depend vào chính xác trường thay đổi thì sẽ k bị gọi hồi tố

    @api.onchange('ethnicity_id')
    def _onchange_ethnicity_id(self):
            self.country_id = self.ethnicity_id.country_ids[:1]
#
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
