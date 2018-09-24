'''
Created on May 28, 2013

@author: oliver
'''

import foursquare




class FoursquareAPI:
    'tiny wrapper around foursquare API'


    # cid    = 'G11S2MN15RY3RI1TAZYU1FN13TV4U5BKIBYZN35E4LNYIYOX'
    # secret = 'TK0F5HJI21SLFQFKNSQQWLUE1PHAAD1EQNLQB1JHCGUOBG5E'
    
    cid    = "SD3DXAPO2ZASZX2I3UKK044MFMALHZ4FJODA1P1UIGUZOADO"
    secret = "BXCBPDFF5ZTZCC1NKPQF2GWMULKPPGQFM5GAFOU43TXCGYBC"
    
    
    def __init__( self, debug = False ):
        pass
    
    
    @staticmethod
    def getInstance( at = False, local = False ):
    
        if local:
            u    = 'http://local.4sqpix.com:8000'
        else:
            u    = 'http://4sqpix.com'
            
        u += "/guess/cb/"
        
        
        
        if at is False:
            client = foursquare.Foursquare( client_id       = FoursquareAPI.cid,
                                            client_secret   = FoursquareAPI.secret,
                                            redirect_uri    = u )
        else:
            client = foursquare.Foursquare( access_token = at )
            
        return client

    

