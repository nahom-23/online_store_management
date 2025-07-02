from odoo import models, fields


class Product(models.Model):
    _name = "management.product"
    _description = "Product"

    name = fields.Char(string="Number", required=True)
    prix = fields.Float(string="Prix", required=True)
    description = fields.Text(string="Description")
    stock = fields.Integer(string="Stock", default=0)
    categorie_id = fields.Many2one("product.category", string="Category")
