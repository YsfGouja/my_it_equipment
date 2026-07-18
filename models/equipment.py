from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

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

    def action_mark_loaned(self):
        for record in self:
            record.state = "prete"

    def action_mark_returned(self):
        for record in self:
            record.state = "disponible"

    days_since_purchase = fields.Integer(
        string="Jours depuis l'achat",
        compute="_compute_days_since_purchase"
    )

    @api.depends("purchase_date")
    def _compute_days_since_purchase(self):
        today = date.today()

        for record in self:
            if record.purchase_date:
                record.days_since_purchase = (
                    today - record.purchase_date
                ).days
            else:
                record.days_since_purchase = 0