# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import json

class product_product_inherit(models.Model):
    _inherit = 'product.product'
    _description = 'product_product_inherit'

    @api.model_create_multi
    def unlink(self):
        product = super(product_product_inherit, self).unlink()
        URL = "https://depotsarl.com/ecomerce/odoo/api.php"
        PARAMS = {'action':'post_delete','id':self.id}
        requests.get(url = URL, params = PARAMS)
        return product
