from odoo import models, fields

class ItEquipment(models.Model):
    _name = "it.equipment"
    _description = "IT Equipment"

    name = fields.Char(string="Name")