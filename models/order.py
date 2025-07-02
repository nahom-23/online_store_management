from odoo import models, fields, api


class Order(models.Model):
    _name = "management.order"
    _description = "Order"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = 'date_order desc'

    name = fields.Char(string="Number", required=True,
                       copy=False, default="New")
    client_id = fields.Many2one("res.partner", string="Client", required=True)
    date_order = fields.Date(string="Date", default=fields.Date.today)
    product_ids = fields.Many2many("management.product", string="Products")
    state = fields.Selection(
        [
            ("broth", "Broth"),
            ("confirm", "Confirm"),
            ("pounds", "Pounds"),
            ("cancel", "Cancel"),
        ],
        string="Status",
        default="broth",
    )
    amount_total = fields.Float(
        string="amount Total", compute="_compute_amount_total", store=True
    )

    @api.model
    def create(self, vals):
        if vals.get("name", "New") == "New":
            vals["name"] = (
                self.env["ir.sequence"].next_by_code(
                    "m") or "New"
            )
        return super(Order, self).create(vals)

    @api.depends("product_ids")
    def _compute_amount_total(self):
        for record in self:
            record.amount_total = sum(
                product.prix for product in record.product_ids)

    def action_confirm(self):
        self.state = "confirm"

    def action_pounds(self):
        self.state = "pounds"

    def action_cancel(self):
        self.state = "cancel"
