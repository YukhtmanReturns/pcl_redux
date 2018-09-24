import pprint


from django.conf import settings 




def my_pprint( obj ):
    
    if False: #settings.DEBUG:    
        pprint.pprint( obj )