from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

import time
import hashlib
from random import randint

from datetime import datetime

from django.core.urlresolvers import reverse

import re

from django import template

register = template.Library()





class Tag(models.Model):
    label = models.TextField()
    
    def __unicode__(self):
        return "T: " + self.label




class Question(models.Model):    
    label    = models.TextField()
    tags     = models.ManyToManyField(Tag, blank=True, null=True)    
    userQ    = models.BooleanField(default=False)
    
    tags_txt = models.TextField( blank=True, null=True )
    active   = models.BooleanField( default=True )
    
    # populated via RAW query
    is_starred = None
    score      = None
    
    
    def __unicode__(self):
        return "Q" + `self.pk` + " " + self.label + "\n"






class UserList(models.Model):
    name       = models.CharField(max_length=100)
    ts_created = models.IntegerField()
    active     = models.BooleanField(default=True)
    hash_key   = models.CharField(max_length=50)

    questions  = models.ManyToManyField( Question,
                                         through="ListQuestionOrder",
                                         blank=True, 
                                         null=True )

    def setHashKey(self):
        self.hash_key = hashlib.md5("pepper" + `self.pk`).hexdigest()
        
        
        
        

class User(models.Model):
    
    GENDER_MALE = "M"
    GENDER_FEMALE = "F"
    GENDER_NOT_SAY = " "
    
    ROLE_ADMIN = "A"
    ROLE_USER = "U"
    ROLE_DOCTOR = "D"

    
    email = models.CharField(max_length=100, unique=True)
    name  = models.CharField(max_length=100, blank=True, null=True)
    
    alias = models.CharField(max_length=100, blank=True, null=True)
    
    pwd_hash    = models.CharField(max_length=100, blank=True, null=True)
    token_login = models.CharField(max_length=100, blank=True, null=True)
    token_reset = models.CharField(max_length=100, blank=True, null=True)
    
    gender = models.CharField( max_length=1,
                               default=GENDER_NOT_SAY)
    
    role = models.CharField( max_length=1,
                             default=ROLE_USER)
    
    bday = models.DateField(blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)
    
    ts_created = models.IntegerField(default=0)
    ts_last_login = models.IntegerField(default=0)
    
    verified = models.BooleanField(default=False)
    
    lists = models.ManyToManyField(UserList)
    
    active = models.BooleanField(default=True)
    
    
    
    def __unicode__(self):
        return self.email
    
    
    def getToken(self, x):
        
        s = "salt" + self.email + "pepper" + `self.pk` + x
        return hashlib.md5(s).hexdigest()    
    
    
    def generateTokenLogin(self):
        self.token_login = self.getToken(`randint(0, 10000)`)

    
    def generateTokenReset(self):
        self.token_reset = self.getToken(`randint(0, 10000)`)
    

    def touchTSLastLogin(self):
        self.ts_last_login = int(time.time())
        
            
    def setPwd(self, pwd):
        self.pwd_hash = self.getToken(pwd)
    
    
    def changePwd(self, old, new, cnew):
        
        if self.passwordOk( old ) and new == cnew:
            self.setPwd( new )
            self.save()
            return True
        else:
            return False

    
    def passwordOk(self, pwd):
        return self.getToken( pwd ) == self.pwd_hash

    
    
    
    @staticmethod
    def verifyUser( token ):
        try:    
            u = User.objects.get( token_login=token )
            u.verified = True
            u.save()
            return True
        except:
            return False


        
    @staticmethod
    def resetPwd( token, pwd, cpwd):
        
        if pwd != cpwd:
            return None
        
        try:
            user = User.objects.get( token_reset = token )
        except:
            return None
            
        user.setPwd( pwd )
        user.generateTokenReset()
        user.save()
        
        return user

    
    @staticmethod
    def createUser(e, n, pwd):
        
        u = None
        
        try:
            u = User(email=e, name=n)
            u.save()
            # need to save first to get the ID
            u.setPwd(pwd)            
            u.generateTokenLogin()             
            u.generateTokenReset()
            u.touchTSLastLogin()
            
            u.ts_created = int(time.time())
                        
            u.save()
            
        except Exception as e:
            u = None                
            
        return u
    

    
    @staticmethod
    def loadUserFromSession(request):
    
        if  not "uid" in request.session:
            
            # try finding the user via the cookie token
            if not "t" in request.COOKIES:            
                return None
            
            try:
                user = User.loginUser( request, 'token' )
                return user
            
            except:
                return None
            
        try:
            return User.objects.get( pk=request.session['uid'], active=True )
        except:
            del request.session['uid']
            
            return None



    @staticmethod
    def loadUserFromEmail(email):
    
        try:
            return User.objects.get( email=email, active=True )
        except:        
            return None


    @staticmethod
    def loadUserFromResetToken( token ):
    
        try:
            return User.objects.get( token_reset=token, active=True )
        except:        
            return None



    @staticmethod
    def loginUser( req, src='email' ):
        
        try:
            if src == "email":
                user = User.loadUserFromEmail( req.POST['email'] )
                if not user.passwordOk( req.POST['pwd'] ):
                    return None        
                
            elif src == 'token':
                if not "t" in req.COOKIES: return None
                t = req.COOKIES['t']                
                user = User.objects.get( token_login=t, 
                                         active=True )
                
        except Exception as ex:
            #pprint.pprint( ex )
            return None            
        
    
        user.touchTSLastLogin()
        user.save()

        req.session['uid'] = user.pk;
        
        return user;
    
    def get_forum_display_name(self):
        
        if self.name != None and len( self.name.strip() ) > 0:
            return self.name
        else:
            return "Anon"
        
        
    forum_display_name = property( get_forum_display_name )
    


        
    def get_display_name_email(self):
        
        if self.name != None and len( self.name.strip() ) > 0:
            return self.name
        else:
            return self.email
        
        

        

class ListQuestionOrder(models.Model):
    list     = models.ForeignKey(UserList)
    question = models.ForeignKey(Question)
    val      = models.FloatField()
    def __unicode__(self):
        return "LO" + `self.list.pk` + " " + `self.question.id` + " " + `self.val` + "\n"







class ForumArea(models.Model):    
    label = models.CharField( max_length=100 )
    url   = models.CharField( max_length=100 )
    
    count_procs   = models.IntegerField( blank=True, default=0 )
    count_topics  = models.IntegerField( blank=True, default=0 )
    count_posts   = models.IntegerField( blank=True, default=0 )

    sort_order    = models.IntegerField( blank=True, default=0 )

    def __unicode__(self):
        return self.label


    def get_absolute_forum_url(self):
        
        u = reverse('pcl:forumProcs', args=[self.url] )
        if u[:4] == "/pcl":
            u = u[4:]
        return u
    
    absolute_forum_url = property( get_absolute_forum_url )

    




class Procedure(models.Model):
    label     = models.TextField()
    active    = models.BooleanField(default=True)
    tags      = models.ManyToManyField(Tag, blank=True, null=True) 
    descr     = models.TextField(blank=True, null=True)

    area      = models.ForeignKey( ForumArea, 
                                   blank=True, null=True,
                                   related_name='procedures' )
    count_topics = models.IntegerField( blank=True, default=0 )
    
    questions = models.ManyToManyField( Question,
                                        through="ProcedureQuestionScore", 
                                        blank=True, 
                                        null=True )

    forum_url = models.CharField( max_length=500, 
                                  blank=True, 
                                  null=True  )    

    
    def __unicode__(self):
        return "P" + `self.pk` + " " + self.label


    def save(self, *args, **kwargs):
        
        super(Procedure, self).save(*args, **kwargs) 

        if self.forum_url == None or len( self.forum_url.strip() ) == 0:
            self.forum_url = self.create_absolute_forum_url()
            super(Procedure, self).save(*args, **kwargs)             

        
        
        


    def create_absolute_forum_url(self):
        
        t = re.sub( "([^\w])", "-", self.label.strip().lower() )
        
        myId = self.id
        if myId == None:
            myId = 1
        
        u = reverse('pcl:forumTopics', args=[myId, t] )
        if u[:4] == "/pcl":
            u = u[4:]

        return u




    def get_absolute_forum_url(self):
        
        if self.forum_url == None or len( self.forum_url.strip() ) == 0:
            self.forum_url = self.create_absolute_forum_url()
            self.save()
        
        return self.forum_url




        
    absolute_forum_url = property( get_absolute_forum_url )




    
    
    def get_search_forum_url(self):
        return "/search/" + self.label
    
    absolute_search_url = property( get_search_forum_url )

    


class ProcedureQuestionScore( models.Model ):
    
    procedure = models.ForeignKey( Procedure )
    question  = models.ForeignKey( Question  )
    score     = models.IntegerField( default=100 )
    
    def __unicode__(self):
        return "Score: P" + `self.procedure.id` + " Q" + `self.question.id` + "   " + `self.score` 
    


class ProcedureQuestionScoreInline(admin.TabularInline):
    model = ProcedureQuestionScore
    extra = 1    
    

class ProcedureAdmin(admin.ModelAdmin):
    inlines = (ProcedureQuestionScoreInline,)

class QuestionAdmin(admin.ModelAdmin):
    inlines = (ProcedureQuestionScoreInline,)
    
    
        
        
# todo: rename to ContactSubmission or so        
class Contact(models.Model):
    
    txt     = models.TextField( blank=True, null=True )
    uid     = models.ForeignKey(User, blank=True, null=True)
    email   = models.CharField( max_length=100, blank=True, null=True)    
    created = models.DateTimeField(blank=True, default=datetime.now)
    
    def __unicode__(self):
        return self.txt
    
    
    
    
    
    
class Vote(models.Model):
    question  = models.ForeignKey(Question)
    user      = models.ForeignKey(User)
    procedure = models.ForeignKey(Procedure)
        
    val = models.SmallIntegerField( default=0 )
    ts  = models.IntegerField( default=0 )
    
    def __unicode__(self):
        return  "U" + `self.user.id` + " Q" + `self.question.id` + " P" + `self.procedure.id` + " " + "V" + `self.val` + "\n"
    

    
    



class ForumTopic(models.Model):
    
    title   = models.CharField( max_length=100 )    
    created = models.DateTimeField(blank=True, default=datetime.now)
    
    post_count    = models.IntegerField(blank=True, default=0)    

    last_post_ts  = models.DateTimeField( blank=True, default=datetime.now )
    last_post     = models.ForeignKey( 'ForumPost' )
    
    procedure = models.ForeignKey( Procedure, related_name='topics')
    
    user = models.ForeignKey( User )
    
    forum_url = models.CharField( max_length=500, 
                                  blank=True, 
                                  null=True  )    



    
    
    def add_post(self, body, user ):
        
            txt = "\n".join( body.splitlines() )
            
            p = ForumPost( body   = txt,
                           topic  = self,
                           user   = user )
            
            p.save()
            
            self.post_count    = self.posts.count()
            self.last_post_ts  = p.created
            self.last_post     = p
            self.save()
    
    
    
    def flag(self, user ):
        flag = ForumTopicFlag( topic = self, 
                               user = user )
        flag.save()

    

    def __unicode__(self):
        return self.title



    def save(self, *args, **kwargs):
        
        super(ForumTopic, self).save(*args, **kwargs) 

        if self.forum_url == None or len( self.forum_url.strip() ) == 0:
            self.forum_url = self.create_absolute_forum_url()
            super(ForumTopic, self).save(*args, **kwargs)             




    def create_absolute_forum_url(self):
        
        t = re.sub( "([^\w])", "-", self.procedure.label.strip().lower() )
        
        u = reverse('pcl:forumTopic', args=[ self.procedure.id,
                                             t,
                                             self.id] )
        if u[:4] == "/pcl":
            u = u[4:] 

        return u




    def get_absolute_forum_url(self):
        
        if self.forum_url == None or len( self.forum_url.strip() ) == 0:
            self.forum_url = self.create_absolute_forum_url()
            self.save()
        
        return self.forum_url

    absolute_forum_url = property( get_absolute_forum_url )



        
                
        



class ForumPost(models.Model):
    
    topic   = models.ForeignKey( ForumTopic, related_name='posts')
    user    = models.ForeignKey( User )

    body    = models.TextField( default='' )
    
    created = models.DateTimeField( blank=True, default=datetime.now )
    

    def __unicode__(self):
        return 'T: ' + self.topic.title




class ForumTopicFlag(models.Model):
    
    created = models.DateTimeField( blank=True, default=datetime.now )    
    topic   = models.ForeignKey( ForumTopic, related_name='flags')    
    user    = models.ForeignKey( User )

    def __unicode__(self):
        return 'Flag: ' + self.topic.title



import pcl.signals


