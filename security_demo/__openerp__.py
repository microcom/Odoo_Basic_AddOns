# noinspection PyStatementEffect
{
    'name': 'security_demo',
    'version': '8.0.1.0.0',
    'category': 'demo',
    'description': """
Demo security.
============

It demos security.
    """,
    'author': 'Microcom',
    'images': [],
    'depends': ['contacts'],
    'demo': [],
    'test': [],
    'data': [
        'security/animal_pet_security.xml',
        'security/ir.model.access.csv',
        'views/res_partner.xml',
    ],
    'auto_install': False,
    'installable': True,
}
