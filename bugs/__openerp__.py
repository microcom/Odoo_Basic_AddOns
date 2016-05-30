# -*- coding: utf-8 -*-
{
    'name': "Bugs Tracker",
    'description': 'Categorize, Prioritize and Manage your Bugs',

    'author': "Noreddine Ben Jillali",
    'website': "http://www.microcom.ca",

    'version': '0.1',

    'depends': ['base', 'web_kanban'],
    'application': True,

    'data': [
        'data/bug.xml',
        'views/bug_view.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}