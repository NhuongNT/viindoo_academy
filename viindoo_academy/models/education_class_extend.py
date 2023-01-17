from odoo import models,fields

class EducationClassExtend(models.Model):
    _inherit = 'education.class'

    # country = fields.Text()

    country_id=fields.Many2one(
        comodel_name='res.country',
        string='Country'
        )
