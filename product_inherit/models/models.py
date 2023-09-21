# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests

class product_inherit(models.Model):
    _inherit = 'product.template'
#    _name = 'product_inherit.product_inherit'
    _description = 'product_inherit'

    @api.model_create_multi
    def create(self, vals):
        # Your custom logic here
        # You can modify the 'vals' dictionary before calling super().create()
        
        # Call the original create method
       product = super(product_inherit, self).create(vals)
       URL = "https://depotsarl.com/ali/active/asala.php"
       PARAMS = {'action':'post_add','id':product.id}
       requests.get(url = URL, params = PARAMS)         
       #requests.get("https://depotsarl.com/ecomerce/odoo/api.php"+"?"+"action=post_add"+"&"+"id="+str(product.id))
        # Add custom behavior here if needed

       return product

    def write(self, vals):
        
        product = super(product_inherit, self).write(vals)
        URL = "https://depotsarl.com/ali/active/asala.php"
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
