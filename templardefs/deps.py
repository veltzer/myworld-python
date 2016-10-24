'''
dependencies for this project
'''

def populate(d):
    d.requirements=[
        'google-api-python-client',
        'click',
    ]

def getdeps():
    return [
        __file__, # myself
    ]
