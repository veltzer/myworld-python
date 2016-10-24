'''
dependencies for this project
'''

def populate(d):
    d.requirements3=[
        'google-api-python-client',
        'click',
    ]

def getdeps():
    return [
        __file__, # myself
    ]
