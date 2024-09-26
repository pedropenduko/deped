{
        'name': "DepEd School Management System",
        'version': '1.0',
        'depends': ['base'],
        'author': "Rommel Laranjo",
        'category': "App",
        'description': """This app will help track all schools if they have downloaded their budget or not yet.""",
        'application': True,
        'data': [
                'security/ir.model.access.csv',
                'views/deped_appointment.xml',
                'views/deped_schools.xml',
                'views/deped_teachers.xml',
                'views/menu.xml',                 
        ]
}
