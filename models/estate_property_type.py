# -*- coding: utf-8 -*-

from odoo import models, api, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"

    name = fields.Char("Name", required=True)

