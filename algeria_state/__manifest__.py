{
    'name': 'Algerian state dz',
    'version': '17.0.0.0',
    'author': 'ESSID Fatima Zahraa',
    'category': 'Custom Modules',
    'license': 'LGPL-3',
    'summary': 'State and commune of algeria',
    'description': """
    """,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'data/state.xml',
        'data/commune.xml',
        'views/state_views.xml',
        'views/commune_views.xml',

    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
