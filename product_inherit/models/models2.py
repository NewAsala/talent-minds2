# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError
import requests
import json

class ProductProduct(models.Model):
    _inherit = 'product.product'
    _description = 'product_product_inherit'

    def unlink(self):
        product = super(ProductProduct, self).unlink()
        #URL = "https://depotsarl.com/ecomerce/odoo/api.php"
        #PARAMS = {'action':'post_delete','id':self.id}
        #requests.get(url = URL, params = PARAMS)
        raise UserError(_(self.id))
        return product
