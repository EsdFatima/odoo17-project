{
    'name': 'Gestion Scolaire',
    'version': '17.0.0.0',
    'author': 'ESSID Fatima Zahraa',
    'category': 'Custom Modules',
    'license': 'LGPL-3',
    'summary': 'Gestion Scolaire',
    'description': """
   Le module de gestion scolaire dans Odoo offre une solution complète pour les écoles, permettant de superviser efficacement les étudiants et les inscriptions. 
    """,
    'depends': ['base', 'mail', 'algeria_state'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/student_profile_views.xml',
        'views/school_year_views.xml',
        'views/school_classes_views.xml',
        'views/school_sub_level_views.xml',
        'views/school_level_views.xml',
        'views/student_subscription_views.xml',

    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
