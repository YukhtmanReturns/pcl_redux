from django.http import HttpResponse, HttpResponseServerError
from django.core.context_processors import csrf
from django.core.cache import cache
from django.core.mail import EmailMessage

from django.db.models import Count
from django.template import Context, RequestContext, loader
 
from models import User, Procedure, Question, Tag, UserList, ListQuestionOrder

import time
import json
import pprint
from common import my_pprint


from pcl.views_common import Message
from pcl.views_forms  import FormProfile, FormProfileChangePwd, FormForgotPwd, FormResetPwd


from django.views.decorators.http import require_POST, require_GET
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404




def userProfile(request):
    
    user = User.loadUserFromSession( request )
    if user is None:
        return redirect( "/" )
    
    form  = None
    pform = None
    
    if request.method == 'POST': # If the form has been submitted...
        
        if request.POST['act'] == "pwd":
            
            pform = FormProfileChangePwd(request.POST)
            if pform.is_valid(): # All validation rules pass
                
                if user.changePwd( pform.cleaned_data['old'], 
                                   pform.cleaned_data['new'],
                                   pform.cleaned_data['cnew'] ):
                    
                    msg = Message(title="Success!", text="Changed Password", type="success")
                else:
                    msg = Message(title="Error!", text="Passwords didn't match.", type="error")
                
                
                request.session['pmsg'] = msg
                    

        else:
            form = FormProfile(request.POST) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
    
                # my_pprint( form.cleaned_data )
    
                user.name    = form.cleaned_data['name']
                user.gender  = form.cleaned_data['gender']
                user.zipcode = form.cleaned_data['zipcode']
                
                user.bday = form.cleaned_data['bday']
                # my_pprint( form.cleaned_data['bday'] )
                
                user.save()
    
                msg = Message(title="Success!", text="Saved profile.", type="success")
                request.session['pmsg'] = msg
    
            return redirect( '/user/profile/' ) # Redirect after POST
            

    if form is None:            
        form = FormProfile( initial={ "gender":  user.gender,
                                      "name":    user.name,
                                      "zipcode": user.zipcode,
                                      "bday":    None if user.bday == None else user.bday.strftime( "%m/%d/%Y" )
                                       }  )
    
    if pform is None:        
        pform = FormProfileChangePwd() 
    
        
    pmsg = None
    if "pmsg" in request.session:
        pmsg = request.session['pmsg']
        del request.session['pmsg']

    template = loader.get_template('pcl/profile.html')
    context = Context( {
                        "user":   user,
                        "form":   form,
                        "pform":  pform,
                        "pmsg":   pmsg 
                        })
    
    return HttpResponse(template.render(context))





def userForgotPwd(request):

    if request.method == 'POST': 
        
        form = FormForgotPwd(request.POST)
        if form.is_valid(): 

            e    = form.cleaned_data['email']
            user = User.loadUserFromEmail( e )

            if user != None:
        
                txt_recov = "Go here: http://patientschecklist.com/user/reset/" + user.token_reset + " \n\nThank you."
    
                email = EmailMessage( 'Patients Checklist Reset Password', 
                                      txt_recov, 
                                     'Patients Checklist <mail@patientschecklist.com>',
                                      [ user.email ])
                email.send()
        
        
        
            template = loader.get_template('pcl/msg.html')
            context = Context( { 
                                "msg": "Sent an email with reset instructions to the address provided."
                                } )
            return HttpResponse(template.render(context))
            
    else:
        form = FormForgotPwd()
        
        
    template = loader.get_template('pcl/forgot.html')
    context = Context( {
                        "form": form 
                        })
    
    return HttpResponse(template.render(context))        



def userResetSet(request):


    if request.method == 'POST': 
        
        form = FormResetPwd(request.POST)
        if form.is_valid(): 

            pwd1    = form.cleaned_data['pwd']
            pwd2    = form.cleaned_data['cpwd']
            t       = form.cleaned_data['token']
            
            user = User.resetPwd( t, pwd1, pwd2 )
            
            if user is None:
                #todo: check this, 
                HttpResponse( "FAIL" )
                        
            txt_recov = "Password was reset."
            
            email = EmailMessage('Password was reset', 
                                 txt_recov,
                                 'Patients Checklist <mail@patientschecklist.com>',
                                 [ user.email ])
            email.send()
        
        
            template = loader.get_template('pcl/msg.html')
            context = Context( { 
                                "msg": "Reset your password, please login again."
                                } )
            return HttpResponse(template.render(context))
            
    
        
    template = loader.get_template('pcl/forgot.html')
    context = Context( {
                        "form": "blub" 
                        })
    
    return HttpResponse(template.render(context))        




def userResetPwd(request, token):


    if request.method == 'POST': 
        
        form = FormResetPwd(request.POST)
        if form.is_valid(): 

            pwd1    = form.cleaned_data['pwd']
            pwd2    = form.cleaned_data['pwd']
            t       = form.cleaned_data['token']
        
            user = User.resetPwd( t, pwd1, pwd2)
            if user is None:
                return HttpResponse( "FAIL" )        
                        
                        
            txt_recov = "Password was reset."
            
            email = EmailMessage( 'Password was reset', 
                                  txt_recov,
                                  'Patients Checklist <mail@patientschecklist.com>', 
                                  [ user.email ])
            email.send()
        
        
            template = loader.get_template('pcl/msg.html')
            context = Context( { 
                                "msg": "Reset your password, please login now."
                                } )
            return HttpResponse(template.render(context))
            
    else:
        
        user = User.loadUserFromResetToken( token )
            
        if user == None:
            
            template = loader.get_template('pcl/msg.html')
            context = Context( { "msg": "Invalid token." } )
            return HttpResponse(template.render(context))

            
        form = FormResetPwd( initial={"pwd": "", "cpwd": "", "token": token } )        

        
    template = loader.get_template('pcl/forgot.html')
    context = Context( {
                        "form": form 
                        })
    
    return HttpResponse(template.render(context))        



@require_POST
def userSignup(request):
        
    try: 
        '''
    if( "email" in request.POST and len( request.POST['email'] ) > 0 and 
        "pwd"   in request.POST and len( request.POST['pwd']   ) > 0 and 
        "cpwd"  in request.POST and len( request.POST['cpwd']  ) > 0 ):
        '''
            
        e  = request.POST['email']
        p  = request.POST['pwd']
        p2 = request.POST['cpwd']
        
        if p != p2 or len( p ) < 4:
            return HttpResponseServerError()
        
        
        u = User.createUser( e, None, p )
        
        request.session['uid'] = u.pk;
        
        template = loader.get_template('pcl/base_navbar.html')
        ctx = Context( {
                        "user": u
                        } )
        res = {}
        res['navbar'] = template.render( ctx )    
        res['res'] = 'OK' 
        
        resp = HttpResponse( json.dumps( res ), 
                             content_type="application/json")
        return resp
            
        
    except Exception as e:
        return HttpResponseServerError()
    



def userLogout(request):
    
    resp = redirect( "/" );
    
    if "uid" in request.session:
        del request.session['uid']
        resp.delete_cookie( "t" )


    msg = Message(title="Success!", text="You logged out successfully!", type="alert")
    request.session['msg'] = msg    
    
    return resp




@require_POST
def userLogin(request):
    
    try:
    
        if not "email" in request.POST or not "pwd" in request.POST :
            return HttpResponseServerError()
        
        remember = "remember" in request.POST
        
        user = User.loginUser( request )
    
        if user is None:
            return HttpResponseServerError()
        
        
        template = loader.get_template('pcl/base_navbar.html')
        ctx = Context( {
                        "user": user
                        } )
        
        
        res = {}
        res['navbar'] = template.render( ctx )    
        
        resp = HttpResponse( json.dumps( res ), 
                             content_type="application/json")
    
        
        if remember:
            resp.set_cookie( "t", user.token_login, 60*60*24*30 ) # 30 days
        else:
            resp.delete_cookie( "t" )
    
        '''   doing this JS side now
        
        # all good, set session data and return success        
        
        msg = Message(title="Success!", text="You logged in successfully!", type="success")
        request.session['msg'] = msg
        '''
            
            
        return resp
    except Exception as ex:
        pass
        # my_pprint( ex )




@require_POST
def userLoggedIn(request):
    
    user = User.loadUserFromSession( request )
    
    if user == None:
        return HttpResponseServerError()
    
    return HttpResponse( 'OK' )    
    
    



def userVerify(request, token):
    
    verified = User.verifyUser( token )
        
    if verified:
        msg="Thank you for verifying your account."
    else:
        msg="Couldn't verify your account, please contact support."
        
    template = loader.get_template('pcl/msg.html')
    context = Context( { 
                        "msg": msg,
                        "verified": verified
                        } )
    
    return HttpResponse(template.render(context))



def createListQuestionOrders( items, ulist_id ):

    no = 10000;
    
    # pprint.pprint( items )
        
    for qid in items:
        
        if len( qid ) == 0:
            continue
        
        o = ListQuestionOrder( list_id = ulist_id, question_id = qid, val=no )
        o.save()
        no += 10000
        
        # pprint.pprint ( o )
        
        
        
        
    


def userListAdd(request):
    
    
    reqParams = request.POST

    try:    
    
        listItems = reqParams['l'].split()
        # pprint.pprint( listItems )
        
        ulist = UserList( name=reqParams['n'], 
                          hash_key="", 
                          ts_created=int(time.time() ) )
        ulist.save()
        ulist.setHashKey()
        ulist.save()
        
        user = User.loadUserFromSession( request )
        user.lists.add( ulist )
        user.save()    
        
        createListQuestionOrders( listItems, ulist.id )
         
        user.save() 
        ulist.save()    
    
        res = { "code":    "OK",
                "listID":  ulist.id }
    
    
        return HttpResponse( json.dumps( res ), 
                             content_type="application/json" )
        
        
    except:
        return HttpResponseServerError()




def userQuestionReorder(request):

    reqParams = request.POST
    
    # pprint.pprint( reqParams )
    
    try:         
        user = User.loadUserFromSession( request )
        
        if user == None:
            return HttpResponse("FAIL");
        
        ulist = user.lists.get( pk=reqParams['lid'] )
        
        if "a" in reqParams and reqParams['a'] == "list":
        
            all_order = ListQuestionOrder.objects.select_related( 'question' ).filter(list=ulist).order_by( "val").all()
    
            all_order.delete()
            
            if reqParams['order'].find(",") != -1:
            
                order_items = reqParams['order'].strip().split(',')
            else:
                order_items = reqParams['order'].strip().split(' ')
                
                
        
            
            
            createListQuestionOrders( order_items, ulist.id )        
            print "done"
            
            
            
        else:
            all_order = ListQuestionOrder.objects.select_related( 'question' ).filter(list=ulist).order_by( "val").all()
            
            max_order = all_order.count()
        
            for pos, _ in enumerate( all_order ):
                
                q = all_order[pos].question
                
                if q.id != (int)(reqParams['qid']):
                    continue
                
                if reqParams['dir'] == "up":
                    if pos != 0:
                        
                        temp = all_order[pos-1].val
                        all_order[pos-1].val = all_order[pos].val
                        all_order[pos].val   = temp
        
                        all_order[pos].save()
                        all_order[pos-1].save()
                        break 
                else:
                    if pos != max_order-2:
                        
                        temp = all_order[pos+1].val
                        all_order[pos+1].val = all_order[pos].val
                        all_order[pos].val   = temp
                         
                        all_order[pos].save()
                        all_order[pos+1].save()
                        break 
            
        
    except Exception as ex:
        
        # pprint.pprint( ex )
        
        return HttpResponse("FAIL");

    
        
    return HttpResponse("OK")
    
    

    

    




    



def userQuestionAdd(request):
    
    
    reqParams = request.POST
    
    if not "lbl" in reqParams:
        return HttpResponse("FAIL");
    
    if not "lid" in reqParams:
        return HttpResponse("FAIL");
    
    user = User.loadUserFromSession( request )
    
    if user == None:
        return HttpResponse("FAIL");
    
    ulist = user.lists.get( pk=reqParams['lid'] ) 
    # todo: check if UserList matches user?
    q = Question( label=reqParams['lbl'] )
    q.save()
    
    all_qs = ListQuestionOrder.objects.select_related( 'question' ).filter(list=ulist).order_by( "val").all()

    new_val = all_qs[all_qs.count() - 1].val + 10000

    new_o = ListQuestionOrder(question = q, list=ulist, val=new_val)

    new_o.save()

    qs = Question.objects.filter( listquestionorder__list = ulist ).order_by("listquestionorder__val")

    template = loader.get_template('pcl/inc.list.html')
    ctx = Context( {
                    "list": ulist,
                    "questions": qs,
                    "show_list_header": True,
                    "read_only": False
                    } )

    return HttpResponse( template.render( ctx ) )





def userQuestionDel(request):
    
    
    reqParams = request.POST
    
    if not "qid" in reqParams:
        return HttpResponse("FAIL");
    
    if not "lid" in reqParams:
        return HttpResponse("FAIL");
    
    user = User.loadUserFromSession( request )
    
    if user == None:
        return HttpResponse("FAIL");
    
    ulist = user.lists.get( pk=reqParams['lid'] )
    
    # my_pprint( ulist )
    
    quest = Question.objects.get( pk=reqParams['qid'] )  
    # my_pprint( quest )

    o = ListQuestionOrder.objects.select_related( 'question' ).filter(list=ulist, question=quest )
    
    o.delete()

    # delete old questions? 

    return HttpResponse("OK")





    
def userListDel(request):
    
    
    reqParams = request.POST
    
    if not "id" in reqParams:
        return HttpResponse("FAIL");

    try:
        ulist = UserList.objects.get( pk=reqParams['id'] )
        
        user = User.loadUserFromSession( request )
    
        user.lists.remove( ulist )
    
        ulist.delete()
        
        user.save()
        
    except Exception as ex:
        # my_pprint( ex ) 
        return HttpResponse("FAIL")
        

    return HttpResponse("OK")


    
    
def userLists(request):
    
    user = User.loadUserFromSession( request )
    
    if user is None:
        return HttpResponseRedirect( "/" )
    
    lists = user.lists.all().order_by("name")
    
    
    for l in lists:
        
        l.all_qs = Question.objects.filter( listquestionorder__list = l ).order_by("listquestionorder__val")
    
    
    template = loader.get_template('pcl/lists.html')
    context = Context( {
                        "user": User.loadUserFromSession( request ), 
                        "lists": lists
                        } )
    

    return HttpResponse(template.render(context))


    
    
def userListShow( request, token ):
    
    
    l  = get_object_or_404( UserList, hash_key=token )

    q = Question.objects.filter( listquestionorder__list = l ).order_by("listquestionorder__val")
    
    template = loader.get_template('pcl/share.html')
    context = Context( {
                        "user": User.loadUserFromSession( request ), 
                        "q":    q
                        } )
    

    return HttpResponse(template.render(context))
    




def userListSend(request):

    try:
                
        u = User.loadUserFromSession( request )
        if u is None:
            raise Exception("not found")
        
        l = u.lists.get( hash_key=request.POST['sendListHK'] )

        # this lookup is for verification only really
        # the IF statement is BS        
        if l is None:
            raise Exception("not found")


        email = request.POST['sendListEmail']

        name = u.get_display_name_email()


        list_link = "http://patientschecklist.com/share/" + request.POST['sendListHK'] + "/" 

        
        subj = name + " shared a PatientsChecklist with you."

        txt  = "Hi,\n\n" + name + " shared a PatientsChecklist with you. You can access the checklist here:\n\n" + list_link + "\n\n\n" + request.POST['sendListTxt'] 
        
        # print "saved"
        email = EmailMessage( subj, 
                              txt,
                              'Patients Checklist <mail@patientschecklist.com>',
                              [ email ] );


        email.send()
        
    except Exception as ex:
        
        # pprint.pprint( ex )
        
        return HttpResponseServerError()
    
    return HttpResponse( "OK" );        

