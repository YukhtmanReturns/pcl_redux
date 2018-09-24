# Create your views here.
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.cache import cache
from django.core.mail import EmailMessage

from django.db.models import Count
from django.template import Context, RequestContext, loader
from django.conf import settings 
 
from models import User, Procedure, Question, Tag



class Message():
    def __init__(self, title, text, type):
        self.title = title
        self.text  = text
        self.type  = type
    


def underConstruction(request):    
        
    template = loader.get_template('pcl/msg.html')
    context = Context( {
                        "user": User.loadUserFromSession( request ), 
                        "msg": "Under Construction"
                        } )
    
    return HttpResponse(template.render(context))




def about(request):    
        
    template = loader.get_template('pcl/about.html')
    context = Context( {
                        "user": User.loadUserFromSession( request ), 
                        } )
    
    return HttpResponse(template.render(context))




def tos(request):    
        
    template = loader.get_template('pcl/tos.html')
    context = Context( {
                        "user": User.loadUserFromSession( request ), 
                        } )
    
    return HttpResponse(template.render(context))




def general(request, what):    
    
    what = what.lower().strip()
        
    if len( what ) == 0:
        what = "about"
    
    try:
        template = loader.get_template('pcl/general_' + what + '.html')
    except:
        what = "about"
        template = loader.get_template('pcl/general_' + what + '.html')
        
        
    context = Context( {
                        "user": User.loadUserFromSession( request ), 
                        } )
    
    return HttpResponse(template.render(context))



