# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo import models, fields

class AccountingPayment (models.Model):
    _name = 'accounting.payment'
    _description = 'Accounting Payment'
    
    sequence = fields.Char(string='STT', required=True)
    
    type = fields.Selection(
        [
            ('phiếu thu','Phiếu Thu'),
            ('phiếu chi','Phiếu Chi')
            ],
        requied='True',
        string='Loại',
        default='phiếu thu'
        )
    description=fields.Text(string='Nội dung Thu, Chi')

# class accounting(models.Model):
#     _name = 'accounting.accounting'
#     _description = 'accounting.accounting'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
