# -*- coding: utf-8 -*-

from odoo import fields, models, api, tools, exceptions
from odoo.exceptions import UserError

class EstatePropertityOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property offer"

    validity = fields.Integer("Validity", default=7)
    date_deadline = fields.Date("Date Deadline", required=True)