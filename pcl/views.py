from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.cache import cache
from django.core.mail import EmailMessage

from django.db.models import Count
from django.template import Context, RequestContext, loader
from django.conf import settings 
 
from models import *

import json
import urllib
from django.http.response import HttpResponseServerError

from common import my_pprint




def quickList(request):
    
    reqParams = request.POST
    
    my_pprint( reqParams )
    
    qs = None

    my_pprint( request.session )

    try:         
        order_items = reqParams['qs'].split(' ')
        qs = []
        
        for item in order_items:
            try:
                q = Question.objects.get(pk=item)
                qs.append( q ) 
            except:
                pass
    
    except:
        pass
        
    
    template = loader.get_template('pcl/inc.list.html')
    ctx = Context( {
                    "questions": qs,
                    "read_only": False
                    } )

    return HttpResponse( template.render( ctx ) )



def listPrint(request):
    
    reqParams = request.GET
    
    qs = None
    title = ""
    
    try:      
        
        if 'title' in reqParams:
            title = reqParams['title']
           
        order_items = reqParams['l'].split(' ')
        qs = []
        
        for item in order_items:
            try:
                q = Question.objects.get(pk=item)
                qs.append( q ) 
            except:
                pass
    
    except:
        pass
        

    
    template = loader.get_template('pcl/print.html')
    ctx = Context( {
                    "questions" : qs,
                    "title"     : title,        
                    } )

    return HttpResponse( template.render( ctx ) )









def index(request):
    
    u = User.loadUserFromSession( request )

# handle the flash msg
    msg = request.session.get( "msg", None )
    if msg != None: 
        del request.session['msg']
        
    
    template = loader.get_template('pcl/index.html')
    context = Context( { 
                        "tasks":   None,
                        "user":    u,
                        "message": msg
                        } )
    
    return HttpResponse(template.render(context))



def blog(request):
    
    u = User.loadUserFromSession( request )

    template = loader.get_template('pcl/blog.html')
    context = Context( { 
                        "user":    u
                        } )
    
    return HttpResponse(template.render(context))




def search(request):

    query = request.GET.get( 'p', '' ) 
    
    return searchQuery( request, query )





def get_procedures_for_query( user, query ):
    

    if len( query ) == 0 :
        return None

    query     = urllib.unquote( query ).strip().lower().replace( '+', " " )    
    pg_query  = "|".join( query.split() )

    try:                
        procedures = list ( Procedure.objects.raw( "select * from pcl_procedure as p, procedure_query_and_rank( %s ) as qr where p.id = qr.pid and p.active = true", 
                                            [ pg_query ] ) )[:1]
    except Exception as ex:
        return None
    
    if procedures == None:
        return None
    
    
            
    for proc in procedures:

        # check if two different queries are really needed
        if user == None:
            proc.res_q = Procedure.objects.get( pk=proc.id ).questions.all()
        else:
            q = Question.objects.raw( 'SELECT q.*, v.val as is_starred , pqs.score as score FROM pcl_question as q INNER JOIN pcl_procedurequestionscore as pqs ON q.id = pqs.question_id LEFT OUTER JOIN pcl_vote as v on q.id = v.question_id AND v.user_id = %s and v.procedure_id = pqs.procedure_id WHERE pqs.procedure_id = %s order by pqs.score desc, pqs.procedure_id',
                                      [ user.id, proc.id ] )

            proc.res_q = q
                
                
    return procedures



def searchQuery( request, 
                 query, 
                 templ = "index.html" ):
    
    
    user        = User.loadUserFromSession( request )    
    
    procedures  = get_procedures_for_query( user, 
                                            query )
        
    
    template = loader.get_template('pcl/' + templ )
    context = Context( {
                        "search_query": query, 
                        "procedures":   procedures,
                        "user":         user   
                    } )

    return HttpResponse(template.render(context))







def sendContact(request):

    try:
                
        u = User.loadUserFromSession( request )

        c = Contact( txt   = request.POST['contactTxt'], 
                     email = request.POST['contactEmail'], 
                     uid   = u  )
        c.save()
        # print "saved"
        email = EmailMessage( 'New Contact Form Submission', 
                              request.POST['txt'],
                              'Patients Checklist <mail@patientschecklist.com>',
                              ['mail@patientschecklist.com',
                               'oh@patientschecklist.com']    )
        email.send()
        # print "sent"
        
        
    except:
        pass
    
    return HttpResponse( "OK" );        






def procedures(request):
    
    procs = Procedure.objects.filter(active=True).order_by( "label" ).all()
    
    user  = User.loadUserFromSession( request )
    
    
    template = loader.get_template('pcl/procedures_list.html')
    context = Context( {
                        "user":     user, 
                        "procs":    procs
                    } )

    return HttpResponse(template.render(context))






def questionStar(request):
    
    reqParam = request.POST
    
    if not "pid" in reqParam:
        return HttpResponse( "0" )
    
    if not "qid" in reqParam:
        return HttpResponse( "0" )
    
    user = User.loadUserFromSession( request )
    if user == None:
        return HttpResponse( "0" )
    
    res = "0"
    
    try:
        v = Vote.objects.get( user_id=user.id, 
                              question_id=reqParam['qid'], 
                              procedure_id=reqParam['pid'] )        
        v.delete()
        
    except Exception as ex:
        
        v = Vote( user_id=user.id, 
                  question_id=reqParam['qid'], 
                  procedure_id=reqParam['pid'],
                  val = 10,
                  ts=int( time.time() ) )

        v.save()
        
        res = 1
    
    return HttpResponse( res )
        




def dataProcedures( request ):
    

    res = []
    
    if "query" in request.POST:
        
        query = request.POST['query'].strip()
        
        procs =  Procedure.objects.filter( label__icontains=query, active=True ).order_by( "label" );
        
        for v in procs:
            res.append( v.label )

        
        # add procedures that we match via keywords
        user = User.loadUserFromSession( request )
        procs = get_procedures_for_query( user, request.POST['query'] )        

        my_pprint( procs )
        
        for p in procs:
            
            if not p.label in res:
                res.append( p.label + " (" + query + ")")

        res = sorted( set( res ))
            
            
         
    return HttpResponse( json.dumps( res ), 
                         content_type="application/json")
    



def custom_404( request ):
    
    user  = User.loadUserFromSession( request )
    
    
    template = loader.get_template('pcl/404.html')
    context = Context( {
                        "user":     user
                    } )
    
    return HttpResponse(template.render(context))
    
    
    
    