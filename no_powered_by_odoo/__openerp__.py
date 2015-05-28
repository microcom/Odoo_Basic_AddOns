# -*- coding: utf-8 -*-
{
    'name': "no_powered_by_odoo",
    'version': '1.1',
    'category' : 'demo',
    'summary': """
        Removes "Powered by Odoo" branding.""",
    'description': """
        Removes "Powered by Odoo" branding found on login screen and main app page.""",
    'author': "Microcom",
    'images': [],
    'depends': ['web'],
    'demo': [],
    'test': [],
    'data': [
        'views/webclient_templates.xml',
    ],
    'auto_install': False,
    'installable': True,
}