{
    'name': 'security_demo',
    'version': '1.0',
    'category' : 'demo',
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
        'res_partner_view.xml',
        'security/security.xml',
        'security/ir.model.access.csv'
    ],
    'auto_install': False,
    'installable': True,
}
