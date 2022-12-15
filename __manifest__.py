# -*- coding: utf-8 -*-


{
    'name': 'Solupaper',
    'version': '1.0',
    'category': 'Hidden',
    'sequence': 6,
    'summary': 'Módulo para Solupaper',
    'description': """

""",
    'depends': ['base','sale','purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/reporte_purchase_order1.xml',
        'views/sale_views.xml',
        'views/purchase_views.xml',
        'views/report.xml',
        'views/sale_report.xml',
        'views/reporte_sale_order.xml',
        'views/account_report.xml',
        'report/report_account_solupaper.xml',
        'views/res_company_view.xml',
        'views/account_move_view.xml',
        'views/solupaper_logistica_view.xml',
        'report/solupaper_logistica_report.xml',
        'report/ir_actions_report.xml'
    ],
    'assets':{},
    'installable': True,
    'auto_install': False,
}
