{
    'name': 'Sport Management',
    'version': '17.0.0.0',
    'author': 'ESSID Fatima Zahraa',
    'category': 'Custom Modules',
    'license': 'LGPL-3',
    'summary': 'Management of sports',
    'description': """
    
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/sport_activity.xml',
        'views/sport_session.xml',
        'views/sport_time_slot.xml',

    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
