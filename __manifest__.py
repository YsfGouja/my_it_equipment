{
    'name': 'My IT Equipment',
    'version': '1.0.0',
    'category': 'Tools',
    'summary': 'Simple equipment management',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/equipment_views.xml',
        'views/employee_views.xml',
        'views/loans_views.xml',
        'views/menu.xml',
        
    ],
    'demo': [
        'demo/equipment_demo.xml',
    ],
    'installable': True,
    'application': False,
    'sequence':-100,
}