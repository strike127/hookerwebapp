from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class myRegistrationForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True)

    
    def __init__(self, *args, **kwargs):
        super(myRegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'full_name', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            
    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(myRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        
        return user