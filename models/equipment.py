from odoo import models, fields

class ItEquipment(models.Model):
    _name = "it.equipment"
    _description = "IT Equipment"

    name = fields.Char(string="Nom")

    equipment_type = fields.Selection([
        ('pc', 'PC'),
        ('ecran', 'Écran'),
        ('casque', 'Casque'),
        ('autre', 'Autre'),
    ], string="Type")

    serial_number = fields.Char(string="Numéro de série")

    state = fields.Selection([
        ('disponible', 'Disponible'),
        ('prete', 'Prêté'),
        ('en_panne', 'En panne'),
    ], string="État", default='disponible')

    purchase_date = fields.Date(string="Date d'achat")

    notes = fields.Text(string="Notes")

    loan_ids = fields.One2many(
        "it.loan",
        "equipment_id",
        string="Prêt"
    )