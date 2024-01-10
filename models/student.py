from odoo import models, fields

class Student(models.Model):
    _name = "student"
    _description = "Student model"


    name = fields.Char("Name")
    father_name = fields.Char("Father name")
    age = fields.Integer("Age")

