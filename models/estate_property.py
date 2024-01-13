# -*- coding: utf-8 -*-

from odoo import fields, models, api, tools


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char("Estate Name", required=True, translate=True)
    description = fields.Char("Estate Description", required=True)
   
    postcode = fields.Char("Post Code", required=True)
    date_availability = fields.Date("Date Availability")
    expected_price = fields.Float("Expected Price")
    selling_price = fields.Float("Selling Price")
    bedrooms = fields.Integer("Bedrooms")
    living_area = fields.Integer("Living Area")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area")
    total_area = fields.Integer("total_area", compute="_compute_total_area")

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for property_record in self:
            property_record.total_area = property_record.living_area + property_record.garden_area

    @api.onchange('garden')
    def _onchange_garden_area_orientation(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'

    GARDEN_ORIENTATION_SELECTION = [
        ("north", "North"),
        ("south", "South"),
        ("east", "East"),
        ("west", "West"),
        ("northeast", "North-East"),
        ("southeast", "South-East"),
        ("northwest", "North-West"),
        ("southwest", "South-West"),
    ]

    garden_orientation = fields.Selection(
        string="Garden Orientation", selection=GARDEN_ORIENTATION_SELECTION
    )
