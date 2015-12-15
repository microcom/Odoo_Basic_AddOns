{
    'name': 'button_widget',
    'version': '1.0',
    'category': 'Hidden',
    'description': """
Widget for boolean fields
==========================

This makes a boolean in form of a button
    """,
    'author': 'Microcom',
    'images': [],
    'depends': ['web'],
    'demo': [],
    'test': [],
    'data': [
        'views/res_partner.xml',
        'views/templates.xml'
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'auto_install': False,
    'installable': True,
}
