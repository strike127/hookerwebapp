from django import forms
from .models import Scan

class ScanForm(forms.ModelForm):
    class Meta:
        model = Scan
        fields = ['email', 'name', 'subject', 'compound', 'currstat']
        
    def save(self, commit=True):
        scan = super(ScanForm, self).save(commit=False)
        scan.email = self.cleaned_data['email']
        
        if commit:
            scan.save()
        
        return scan