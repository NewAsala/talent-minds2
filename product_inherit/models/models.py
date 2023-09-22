# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import json

class product_inherit(models.Model):
    _inherit = 'product.template'
#    _name = 'product_inherit.product_inherit'
    _description = 'product_inherit'

    @api.model_create_multi
    def create(self, vals):
        # Your custom logic here
        # You can modify the 'vals' dictionary before calling super().create()
       headers = {"Content-Type": "application/json", "Accept": "application/json", "Catch-Control": "no-cache"}
        # Call the original create method
       product = super(product_inherit, self).create(vals)
       URL = "https://depotsarl.com/ecomerce/odoo/api.php"
       requests.post(url = URL, data= json.dumps(product), headers=headers)
       #PARAMS = {'action':'post_add','id':6}
       #requests.get(url = URL, params = PARAMS)         
        # Add custom behavior here if needed

       return product

    def write(self, vals):
        
        product = super(product_inherit, self).write(vals)
        URL = "https://depotsarl.com/ecomerce/odoo/api.php"
        PARAMS = {'action':'post_edit','id':self.id}
        requests.get(url = URL, params = PARAMS)
        return product
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
