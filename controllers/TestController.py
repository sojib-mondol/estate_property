# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import Controller, Response

import json


class TestController(Controller):
    @http.route(
        "/test",
        type="http",
        auth="public",
        methods=["GET"],
    )
    def website_form_saleorder(self, **kwargs):
        student = {
            "name": "Mohiuddin",
            "roll": 102,
            "CGPA": 3.31,
        }

        return Response(response=json.dumps(student), mimetype="text/json")