from odoo import models, fields

class Ethnicity (models.Model):
    _name = 'res.ethnicity'
    _description = 'Name of Ethnicity'
    
    name = fields.Char(
        string='Ethnicity Name',
        help='The name of the Ethnicity',
        required=True
        )
    # code = fields.Char(
    #     string='Code',
        # required=True,
        # groups='base.group_user'
    #     )
    # => xong thuộc tính phân quyền: nhóm base sẽ được phân quyền đối với trường này, có thể thêm nhiều nhóm và cách nhau bằng dấu phẩy.
    # description = fields.Text(string='Description')
       
    country_ids = fields.Many2many(
        comodel_name='res.country', 
        relation='res_country_ethnicity_rel',
        column1='ethnicity_id',
        column2='country_id',
        )
    # code = fields.Char(
    #     string='Code',
    #     required='True',
    #     )
    # def update_code(self, new_code):
    #     for r in self:
    #         r.new_code = r.code
    # => nếu người thực thi đoạn code này mà không nằm trong group bên trên được khai báo thì sẽ bị lỗi