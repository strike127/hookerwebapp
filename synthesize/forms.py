from django import forms
from scan.models import Scan

class SynthesizeForm(forms.ModelForm):
    class Meta:
        model = Scan
        # fields = ['email', 'name', 'subject', 'compound', 'current_status', 'date_for_scan', 'time_for_scan']
        fields = ['subject', 'compound', 'date_for_scan', 'time_for_scan']
        # exclude = ['email', 'name', 'current_status']
        
        help_texts = {
            'subject': 'Group to which this message belongs to',
            'compound': 'C11/F18',
        }

