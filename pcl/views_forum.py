from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.mail import EmailMessage
from django.db.models import Count
from django.shortcuts import get_object_or_404
 
from models import *

import pprint
import urllib

from common import my_pprint







def forumAreas(request):

    user  = User.loadUserFromSession( request )    
    areas = ForumArea.objects.all().order_by( 'sort_order', 'label' )
    
    # todo: cache
    for a in areas:    
        a.top_procs = Procedure.objects.filter( area=a, active=True ).order_by('-count_topics')[:2] 
        
    
    template = loader.get_template('pcl/forum_areas.html')
    context = Context( {
                        "user":     user, 
                        "areas":    areas
                    } )

    return HttpResponse(template.render(context))
    
    

    
def forumProcedures(request, area):

    user  = User.loadUserFromSession( request )
    
    a  = get_object_or_404( ForumArea, url = area ) 
    
    if a.sort_order == 0:
        return HttpResponseRedirect( "/forum/0-general/" )
    else:
    
        procs = Procedure.objects.filter( area__url=area, active=True ).all().order_by( 'label' ) 
        
        
    
        if len( procs ) == 0:
            return HttpResponseRedirect( '/forum/' )


        # todo: remove
        '''
        for p in procs:
            #continue        
            p.count_topics = ForumTopic.objects.filter( procedure = p ).count()
            p.save()
        '''
                 
        
        template = loader.get_template('pcl/forum_procs.html')
        context = Context( {
                            "user":     user, 
                            "procs":    procs
                        } )


    return HttpResponse(template.render(context))





def forumTopics(request, pid):

    user    = User.loadUserFromSession( request )
    
    title   = ""
    proc    = None
    proc_id = 0
    
    if pid == '0':
        a = get_object_or_404( ForumArea, sort_order=0 )
        
        title = a.label 
    else:
        proc    = get_object_or_404( Procedure, pk=pid )
                
        proc_id = proc.pk
        title   = proc.label     
        
    
     
    
    topics = ForumTopic.objects.filter( procedure__id = proc_id ).all().order_by( '-last_post_ts' )

    template = loader.get_template('pcl/forum_topics.html')
    context = Context( {
                        "user":         user,
                        "title":        title,
                        "procedure":    proc, 
                        "topics":       topics
                    } )

    return HttpResponse(template.render(context))







def forumTopic(request, tid ):

    try:        
        user = User.loadUserFromSession( request )
        
        topic = get_object_or_404( ForumTopic, pk=tid )
    
        template = loader.get_template('pcl/forum_topic.html')
        context = Context( {
                            "user":     user, 
                            "topic":    topic,
                        } )
    
        return HttpResponse(template.render(context))
        
    except Exception as ex:
        # my_pprint( ex )
        pass 
        
    
    
    return HttpResponseRedirect( '/forum/' )
    





def forumTopicDel(request, tid ):
    

    try:
        
        user = User.loadUserFromSession( request )
        
        if user == None:
            return HttpResponse( 'FAIL' )

        topic = ForumTopic.objects.get( pk=tid )

        if topic.user != user:
            return HttpResponse( 'FAIL' )

        topic.posts.all().delete()
        topic.delete()
    
        return HttpResponse( 'OK' )
        
    except Exception as ex:
        
        # my_pprint( ex )
        return HttpResponse( 'FAIL' )
    



def forumTopicFlag(request, tid ):
    
    try:        
        user = User.loadUserFromSession( request )
        
        if user == None:
            return HttpResponse( 'FAIL' )

        topic = ForumTopic.objects.get( pk=tid )

        if topic.user != user:
            return HttpResponse( 'FAIL' )

        topic.flag( user )
        
        txt = "This topic got flagged: \n\n" + "http://patientschecklist.com" + topic.absolute_forum_url

        email = EmailMessage( 'Forum Topic got flagged', 
                              txt,
                              'Patients Checklist <mail@patientschecklist.com>',
                              ['mail@patientschecklist.com',
                               'oh@patientschecklist.com']    )
        email.send()


        return HttpResponse( 'OK' )
        
    except Exception as ex:
        
        # my_pprint( ex )
        return HttpResponse( 'FAIL' )
    



def forumTopicAdd(request, pid):
    
    u = '/forum/'
    
    try:
        
        user = User.loadUserFromSession( request )
        
        if user == None:            
            return HttpResponseRedirect( u )


        # proc = Procedure.objects.get( pk=pid )        
        
        title = request.POST['title']
        body  = request.POST['body']
        
        if len( title ) > 0 and len( body ) > 0:
        
            topic = ForumTopic( title         = title,
                                procedure_id  = pid,
                                user          = user )
            
            topic.save()

            topic.add_post( body, user )
        
            u = topic.absolute_forum_url
        else:
            # failed, go back to the list of topics
            pass #u = proc.absolute_forum_url
        
        HttpResponseRedirect( u )
        
    except Exception as ex:
        # pprint.pprint( ex )
        pass
        
    return HttpResponseRedirect( u )




def forumTopicEdit(request, tid):
    
# try:
    
    user = User.loadUserFromSession( request )
    
    if user == None:
        return HttpResponseRedirect( '/forum/' )
    
    
    topic = ForumTopic.objects.get( pk=tid )
    u     = topic.absolute_forum_url

    posts = topic.posts.all().order_by( 'created' )
    
    # most cumbersome way possible to get most recent post
    # maybe at some point we'll store that in topic
    c = posts.count()
    is_first_post = ( c == 1 )
    post = posts[c - 1]
    
    
    # saving?
    if request.method == 'POST':
        
        #todo: sec checks
        
        if user != post.user:
            return HttpResponseRedirect( u )
        

        if 'title' in request.POST and is_first_post:
            topic.title = request.POST['title'].strip()
            topic.save()
        

        post.body = "\n".join( request.POST['body'].strip().splitlines() )
        post.save()
        
        return HttpResponseRedirect( u )

    
    
    
    
    template = loader.get_template('pcl/forum_topic_edit.html')
    context = Context( {
                        "user":             user, 
                        'topic':            topic,
                        "is_first_post":    is_first_post,
                        'post':             post
                    } )
            
    return HttpResponse(template.render(context))
            
# except Exception as ex:
#    my_pprint( ex ) 
    return HttpResponse( "FAIL" );
    
    



def forumPostAdd(request, tid):
    
    try:
        user = User.loadUserFromSession( request )
        
        if user == None:
            return HttpResponseRedirect( '/forum/' )
        
        
        topic = ForumTopic.objects.get( pk=tid )
                
        body  = request.POST['body'].strip()
    
        if len( body ) > 0:
        
            topic.add_post( body, user )
        
        return HttpResponseRedirect( topic.absolute_forum_url )

        
    except Exception as ex:
        pass
        # my_pprint( ex )
        
    return HttpResponseRedirect( '/forum/' )
    
    
    


def forumTopicsSearch( request, query, pid=-1, area=''):


    user   = User.loadUserFromSession( request )

    if len( query.strip() ) == 0:
        return HttpResponseRedirect( '/forum/' )


    query     = urllib.unquote( query ).strip().lower().replace( '+', " " )    
    pg_query  = "|".join( query.split() )

    topics      = None
    scope_text  = None
    scope_link  = None

    sql_query  = 'SELECT t.* FROM procedure_forum_search( %s ) as s, pcl_forumtopic as t ' 
    sql_params = [ pg_query ]
    
    # todo: improve?
    if pid != -1:
        sql_query  += " AND t.procedure_id = %s AND "
        sql_params.append( pid )

        p  = get_object_or_404( Procedure, pk=pid )
        scope_text = p.label
        scope_link = p.absolute_forum_url
        
    elif len( area.strip() ) > 0: 
        sql_query  += ", pcl_forumarea as a, pcl_procedure as p WHERE a.id = p.area_id AND a.url = %s AND p.id = t.procedure_id AND "
        sql_params.append( area )
        
        a  = get_object_or_404( ForumArea, url = area )
        scope_text = a.label
        scope_link = a.absolute_forum_url
        
        
        
    else:
        sql_query += " where "
        
    sql_query += " s.tid = t.id "


    try:                
        topics = list ( ForumTopic.objects.raw( sql_query, 
                                                sql_params ) )
        
        # my_pprint( topics )
          
    except Exception as ex:
        # my_pprint( ex )
        pass


    

    template = loader.get_template('pcl/forum_search.html')
    context = Context( {
                        "user":                 user, 
                        "topics":               topics,
                        'forum_search_query':   query,
                        'scope_text':            scope_text,
                        'scope_link':            scope_link
                    } )

    return HttpResponse(template.render(context))
    
    
    



