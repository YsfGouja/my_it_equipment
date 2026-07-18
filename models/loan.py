from odoo import models, fields, api
from odoo.exceptions import ValidationError

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

    @api.constrains("equipment_id")
    def _check_broken_equipment(self):
        for record in self:
            if record.equipment_id.state == "en_panne":
                raise ValidationError(
                    "Broken equipment cannot be loaned."
                )