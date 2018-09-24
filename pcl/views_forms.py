

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field

from crispy_forms.bootstrap import AppendedText, FormActions




class FormProfile(forms.Form):
    
    name    = forms.CharField(max_length=100, help_text="(optional)", required=False)
    zipcode = forms.DecimalField( min_value=0, 
                                  max_value=99999, 
                                  help_text="(optional)", 
                                  required=False )
    
    
    bday    = forms.DateField( label="Birthday", 
                               help_text="(optional)", 
                               required=False )

    gender  = forms.ChoiceField( choices=[ ("M", "Male"), 
                                           ("F", "Female"),
                                           (" ","Rather not say" ) ] )
    
    act     = forms.CharField( required=True,
                               widget=forms.HiddenInput,
                               initial="prof" )
    

    def __init__(self, *args, **kwargs):
        super( FormProfile, self).__init__(*args, **kwargs )
        self.helper = FormHelper()
        self.helper.form_id = 'id-profileForm'
        self.helper.form_class = 'form form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '/user/profile/'

        self.helper.layout = Layout(
            Fieldset(
                'My Profile',
                'name',
                'zipcode',
                'gender',
                'bday',
                "act"
            ),
            # Field('id_bday', id="id_bday" ), #, data_date_format="mm/dd/yyyy" ),
            # AppendedText('id_bday', '<i class="icon-th"></i>'),
            
            ButtonHolder(
                Submit('submit', 'Save', css_class='btn-success')
            )
        )
        



class FormProfileChangePwd(forms.Form):
    
    old     = forms.CharField( min_length=4, 
                               required=True,
                               widget=forms.PasswordInput,
                               label="Current Password" )
    
    new     = forms.CharField( min_length=4, 
                               required=True,
                               widget=forms.PasswordInput,
                               label="New Password" )
    
    cnew    = forms.CharField( min_length=4, 
                               required=True,
                               widget=forms.PasswordInput,
                               label="Confirm New Password" )
    
    act     = forms.CharField( required=True,
                               widget=forms.HiddenInput,
                               initial="pwd" )
    

    def __init__(self, *args, **kwargs):
        super( FormProfileChangePwd, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-profileChangePwd'
        self.helper.form_class = 'form form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '/user/profile/'

        self.helper.layout = Layout(
            Fieldset(
                'Change Password',
                'old',
                'new',
                'cnew',
                "act"
            ),
            # Field('id_bday', id="id_bday" ), #, data_date_format="mm/dd/yyyy" ),
            # AppendedText('id_bday', '<i class="icon-th"></i>'),
            
            ButtonHolder(
                Submit('submit', 'Change Password', css_class='btn-success  pull-right')
            )
        )








class FormForgotPwd(forms.Form):
    
    email    = forms.EmailField()
    

    def __init__(self, *args, **kwargs):
        super(FormForgotPwd, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-formForgot'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '/user/forgot/'

        self.helper.layout = Layout(
            Fieldset(
                '',
                'email'
            ),
            ButtonHolder(
                Submit('submit', 'Send Recovery Instructions', css_class='btn-success')
            )
        )
        





class FormResetPwd(forms.Form):
    
    pwd      = forms.CharField(widget=forms.PasswordInput(), label="Password")
    cpwd     = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")
    token    = forms.CharField(widget=forms.HiddenInput() )

    def __init__(self, *args, **kwargs):
        super(FormResetPwd, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-formReset'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '/user/reset/set/'

        self.helper.layout = Layout(
            Fieldset(
                '',
                'pwd',
                "cpwd",
                "token"
            ),
            ButtonHolder(
                Submit('submit', 'Reset Password', css_class='btn-success')
            )
        )
        
        
        
