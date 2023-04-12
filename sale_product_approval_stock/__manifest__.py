# Copyright 2021 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Delivery Order Approval Workflow",
    "summary": "Delivery Order Product Apploval Workflow",
    "version": "16.0.1.0.0",
    "website": "https://github.com/OCA/sale-workflow",
    "category": "Products",
    "author": "Open Source Integrators, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "maintainers": ["dreispt"],
    "development_status": "Alpha",
    "depends": ["stock", "sale_product_approval"],
    "data": [
        "views/product_state.xml",
        "views/product_template.xml",
        "views/stock_picking.xml",
        "views/delivery_order_exception.xml",
    ],
}
