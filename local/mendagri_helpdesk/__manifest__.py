{
    'name': "Kementerian Dalam Negeri Helpdesk",
    'version': '16.0.0.0.0',
    'summary': """Helpdesk Module for Mendagri""",
    'description': """Can create ticket from website also and can manage it from backend.
    Bill can be created for ticket with service cost""",
    'author': "WannaBeStart",
    'category': 'Website',
    'depends': ['odoo_website_helpdesk', 'odoo_website_helpdesk_dashboard', 'base'],
    'data': [
        'security/security_helpdesk.xml',
        'security/ir.model.access.csv',
        'views/mendagri_helpdesk_menu_view.xml',
        'views/res_users_view.xml',
    ],
    'assets': {

    },
    'images': [],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
