from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class myRegistrationForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)

    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(myRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['username']
        
        if commit:
            user.save()
        
        return user