{
        'name': "DepEd",
        'version': '1.0',
        'depends': ['base'],
        'author': "Rommel Laranjo",
        'category': "App",
        'description': """This app will track all schools if they have downloaded or not yet.""",
        'application': True,
        'data': [
                'security/ir.model.access.csv',
                # 'views/deped_principals.xml',
                'views/deped_schools.xml',
                'views/deped_teachers.xml',
                'views/menu.xml', 
                
        ]
}
