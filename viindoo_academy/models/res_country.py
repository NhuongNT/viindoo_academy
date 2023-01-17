from odoo import models, fields

class ResCountry(models.Model):
    _inherit = 'res.country'
    _description = 'Country'
      
    class_ids = fields.One2many(
        comodel_name='education.class',
        inverse_name='country_id',
        string='Class'
        )
    
    ethnicity_ids = fields.Many2many(
        comodel_name='res.ethnicity',
        relation='res_country_ethnicity_rel',
        column1='country_id',
        column2='ethnicity_id',
        )
