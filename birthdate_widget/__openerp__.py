{
    'name': 'birthdate_widget',
    'version':'1.0',
    'category' : 'demo',
    'description': """
This module adds a birthdate widget.
====================================

By default, the widget offers 10 years backward. This changes it to 100 years.

We apply this widget to partner's date on the Sale & Purchases tab.
    """,
    'author':'Microcom',
    'images':[],
    'depends':['web'],
    'demo':[],
    'test': [],
    'data':[
        'views/templates.xml',
        'views/res_partner_view.xml',
    ],
    'qweb' : [],
    'auto_install': False,
    'installable': True,
}
