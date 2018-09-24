
from django.test import TestCase

from pcl.models import User

from random import randint

class SimpleTest(TestCase):

    @staticmethod
    def __createUser():
        
        name  = "userTst" + `randint(0, 10000000 )`
        email = name + "@gmail.com"
        p     = "Pwd" + name + "Pwd"

        u = User.createUser(e = email, n=name, pwd=p)        

        return ( u, p ) if not u is None else None




    def test_user_create_user(self):
        
        
        name  = "userTst" + `randint(0, 10000000 )`
        email = name + "@gmail.com"
        p     = "Pwd" + name + "Pwd"
         
        u = User.createUser(e = email, n=name, pwd=p)
        
        self.assertNotEqual( None, u )
        u.delete()
          
        
    def test_user_load_user_by_email(self):
        
        u, pwd = SimpleTest.__createUser()
        
        self.assertNotEqual( None, u )        
                
        try:
            u2 = User.loadUserFromEmail( u.email )
            self.assertNotEqual( None, u2 )
        except:
            pass
        
        u.delete()
        
             
    def test_user_change_password_new_ok(self):
                
        u, pwd = SimpleTest.__createUser()
        
        pwd_new = "newpwd" + `randint(100000, 100000000000)`
        
        res = u.changePwd( pwd, pwd_new, pwd_new )
        
        self.assertEqual( True, res )
        
        u2 = User.loadUserFromEmail( u.email )
        
        self.assertEqual( True, u2.passwordOk( pwd_new ) )
        
        
        u.delete()
        
                
    def test_user_change_password_new_pwd_not_matching(self):
                
        u, pwd = SimpleTest.__createUser()
        
        pwd_new = "newpwd" + `randint(100000, 100000000000)`
        
        res = u.changePwd( pwd, pwd_new, pwd_new + "blub" )
        
        self.assertEqual( False, res )
        
        u2 = User.loadUserFromEmail( u.email )
        
        self.assertEqual( False, u2.passwordOk( pwd_new ) )
        
        u.delete()
             
        
    def test_user_check_password_ok(self):
                
        u, pwd = SimpleTest.__createUser()
        
        res = u.passwordOk( pwd )
        
        self.assertEqual( True, res )
        
        u.delete()
                
        
    def test_user_verify_ok(self):
        
        u, pwd = SimpleTest.__createUser()
        
        self.assertEqual( True, User.verifyUser( u.token_login ) )

        u2 = User.loadUserFromEmail( u.email )
        
        self.assertEqual( True, u2.verified )
        
        u.delete()
        
        
    def test_user_verify_fails(self):
        
        u, pwd = SimpleTest.__createUser()
        
        self.assertEqual( False, User.verifyUser( "123" ) )
        
        u2 = User.loadUserFromEmail( u.email )
        
        self.assertEqual( False, u2.verified )
        
        u.delete()



    def test_create_and_delete_many_users(self):

        users = []

        for _ in range( 500 ):        
            u, pwd = SimpleTest.__createUser()
            users.append( u )
            
        for u in users: 
            u.delete()

        self.assertEqual( len( users ), 500 )

        
        
        
        
        