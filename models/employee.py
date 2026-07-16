from odoo import models, fields

class ItEmployee(models.Model):
    _name = "it.employee"
    _description = "Employé"

    name = fields.Char(string="Nom")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Telephone")

    loan_ids = fields.One2many(
        "it.loan",
        "employee_id",
        string="Prêt"
    )

    user_id = fields.Many2one(
        "res.users",
        string="Utilisateur"
    )