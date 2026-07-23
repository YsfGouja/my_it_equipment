from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestEquipment(TransactionCase):

    def setUp(self):
        super().setUp()

        self.employee = self.env["it.employee"].create({
            "name": "John Doe",
        })

    def test_mark_loaned(self):
        equipment = self.env["it.equipment"].create({
            "name": "Dell Laptop",
            "equipment_type": "pc",
            "state": "disponible",
        })

        equipment.action_mark_loaned()

        self.assertEqual(equipment.state, "prete")

    def test_mark_returned(self):
        equipment = self.env["it.equipment"].create({
            "name": "Dell Laptop",
            "equipment_type": "pc",
            "state": "prete",
        })

        equipment.action_mark_returned()

        self.assertEqual(equipment.state, "disponible")

    def test_cannot_loan_broken_equipment(self):
        equipment = self.env["it.equipment"].create({
            "name": "Broken Screen",
            "equipment_type": "ecran",
            "state": "en_panne",
        })

        with self.assertRaises(ValidationError):
            self.env["it.loan"].create({
                "equipment_id": equipment.id,
                "employee_id": self.employee.id,
            })