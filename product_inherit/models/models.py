# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError
import requests
import json

class product_inherit(models.Model):
    _inherit = 'product.template'
    _description = 'product_inherit'

    @api.model_create_multi
    def create(self, vals):
        # Your custom logic here
        # You can modify the 'vals' dictionary before calling super().create()
       #headers = {"Content-Type": "application/json", "Accept": "application/json", "Catch-Control": "no-cache"}
        # Call the original create method
       product = super(product_inherit, self).create(vals)
       URL = "https://depotsarl.com/ecomerce/odoo/api.php"
       #json_data = json.dumps(product.__dict__, default=lambda o: o.__dict__, indent=4)
       #requests.post(url = URL,data=json_data,headers=headers)
       PARAMS = {'action':'post_add','id':product.id}
       requests.get(url = URL, params = PARAMS)         
        # Add custom behavior here if needed

       return product

    def write(self, vals):
        
        product = super(product_inherit, self).write(vals)
        URL = "https://depotsarl.com/ecomerce/odoo/api.php"
        PARAMS = {'action':'post_edit','id':self.id}
        requests.get(url = URL, params = PARAMS)
        return product

    def unlink(self):
        product = super(product_inherit, self).unlink()
        URL = "https://depotsarl.com/ecomerce/odoo/api.php"
        PARAMS = {'action':'post_delete','id':self.id}
        requests.get(url = URL, params = PARAMS)
        #raise UserError(_(self.id))
        return product

