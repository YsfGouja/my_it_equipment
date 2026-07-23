# My IT Equipment - Odoo 17

## Overview

**My IT Equipment** is an Odoo 17 module developed as part of a practical assignment. It allows an organization to manage IT equipment, employees, and equipment loans while demonstrating the main concepts of Odoo module development, including models, views, security, business logic, reporting, demo data, and automated testing.

---

## Features

### Equipment Management

* Create and manage IT equipment.
* Equipment information includes:

  * Name
  * Equipment Type (PC, Screen, Headset, Other)
  * Serial Number
  * Status (Available, Loaned, Broken)
  * Purchase Date
  * Notes

### Employee Management

* Create and manage employees.
* Associate employees with equipment loans.

### Loan Management

* Create equipment loans.
* Associate each loan with:

  * Equipment
  * Employee
  * Loan Date
  * Return Date

---

## Implemented Features

### Step 1 – Module Skeleton

* Created an installable Odoo module.
* Defined the `it.equipment` model.
* Configured the module manifest.
* Implemented the standard Odoo module structure.

### Step 2 – Business Fields

Added business fields to the equipment model:

* Equipment type
* Serial number
* Equipment status
* Purchase date
* Notes

### Step 3 – User Interface

Created:

* List (Tree) view
* Form view
* Window action
* Navigation menu

Implemented conditional row decorations based on equipment status:

* Green → Available
* Yellow → Loaned
* Red → Broken

### Step 4 – Relationships

Created:

* Employee model
* Loan model

Implemented:

* Many2one relationships
* One2many relationships

Each loan is linked to one employee and one equipment item.

### Step 5 – Security

Implemented:

* IT Manager security group
* Access rights using `ir.model.access.csv`
* Record rule limiting normal users to their own loans

### Step 6 – Business Logic

Added:

* "Mark as Loaned" button
* "Mark as Returned" button
* Constraint preventing broken equipment from being loaned
* Computed field displaying the number of days since purchase

### Step 7 – Kanban and Search

Implemented:

* Kanban view grouped by equipment status
* Search view
* Quick filters:

  * Available
  * Broken
* Group by Equipment Type

### Step 8 – Demo Data and Tests

Created:

* Demo equipment records
* Automated tests using `TransactionCase`

Tests verify:

* Loan button functionality
* Return button functionality
* Validation preventing loans of broken equipment

### Step 9 – Bonus (PDF Report)

Implemented:

* Loan report using QWeb
* Printable PDF containing:

  * Equipment
  * Employee
  * Loan date
  * Return date

---

## Project Structure

```text
my_it_equipment/
│
├── models/
│   ├── equipment.py
│   ├── employee.py
│   └── loan.py
│
├── security/
│   ├── security.xml
│   └── ir.model.access.csv
│
├── views/
│   ├── equipment_views.xml
│   ├── employee_views.xml
│   ├── loans_views.xml
│   └── menu.xml
│
├── reports/
│   ├── loan_report.xml
│   └── loan_report_template.xml
│
├── demo/
│   └── equipment_demo.xml
│
├── tests/
│   ├── __init__.py
│   └── test_equipment.py
│
├── __init__.py
├── __manifest__.py
└── README.md
```

---

## Technologies Used

* Odoo 17
* Python 3
* PostgreSQL
* XML (Views, Security, Reports)
* QWeb
* Odoo ORM

---

## Installation

1. Copy the module into the `custom_addons` directory.
2. Restart the Odoo server.
3. Update the Apps list.
4. Install **My IT Equipment**.

---

## Running Tests

```bash
python odoo-bin -d <database_name> --test-enable -u my_it_equipment
```

---

## Author

Developed as an educational Odoo 17 project for learning module development concepts including ORM models, XML views, security, business logic, reporting, and automated testing.
