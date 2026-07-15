from odoo import models, fields

class ItLoan(models.Model):
    _name = "it.loan"
    _description = "Prêt de materiel"

    equipment_id = fields.Many2one(
        "it.equipment",
        string="Materiels"
    )

    employee_id = fields.Many2one(
        "it.employee",
        string="Employé"
    )

    loan_date = fields.Date(
        string="Date de Prêt"
    )

    return_date = fields.Date(
        string="Date de Retour"
    )