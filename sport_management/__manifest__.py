{
    'name': 'Sport Management',
    'version': '17.0.0.0',
    'author': 'ESSID Fatima Zahraa',
    'category': 'Custom Modules',
    'license': 'LGPL-3',
    'summary': 'Sports Management',
    'description': """
    The Sport Management module in Odoo provides a comprehensive solution for schools to efficiently oversee sports activities for students and athletes. 
    It consists of three core components: activities, sessions, and time slots.
    """,
    'depends': ['base','sale_management'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/sport_activity.xml',
        'views/sport_session.xml',
        'views/sport_time_slot.xml',

    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
