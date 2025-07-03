{
    "name": "Online Store Management",
    "version": "1.0",
    'category': 'Sales',
    "summary": "Online Store Management Module",
    "depends": ["sale", "stock", "account", "mail", 'base'],
    "data": [
        "security/ir.model.access.csv",
        "views/product_view.xml",
        "views/order_view.xml",
        "views/menu.xml",
        "data/sequence.xml",
    ],
    "installable": True,
    "application": True,
    'auto_install': False,
}
