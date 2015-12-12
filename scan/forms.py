from django import forms
from .models import Scan

class ScanForm(forms.ModelForm):
    class Meta:
        model = Scan
        # fields = ['email', 'name', 'subject', 'compound', 'current_status', 'date_for_scan', 'time_for_scan']
        fields = ['subject', 'compound', 'date_for_scan', 'time_for_scan']
        # exclude = ['email', 'name', 'current_status']
        
        help_texts = {
            'subject': 'Group to which this message belongs to',
            'compound': 'C11/F18',
        }
    # def clean_email(self):
    #     return self.cleaned_data['email'] or None
    # def clean_name(self):
    #     return self.cleaned_data['name'] or None
    # def clean_subject(self):
    #     return self.cleaned_data['subject'] or None
    # def clean_current_status(self):
    #     return self.cleaned_data['current_status'] or None
    # def clean_date_for_scan(self):
    #     return self.cleaned_data['date_for_scan'] or None
    # def clean_time_for_scan(self):
    #     return self.cleaned_data['time_for_scan'] or None
    # def clean_init_activity(self):
    #     return self.cleaned_data['init_activity'] or None
    # def clean_init_toi(self):
    #     return self.cleaned_data['toi'] or None

class SynthesizeForm(forms.ModelForm):
    class Meta:
        model = Scan
        # fields = ['email', 'name', 'subject', 'compound', 'current_status', 'date_for_scan', 'time_for_scan']
        fields = ['init_activity', 'synthesize_time']
        # exclude = ['email', 'name', 'current_status']
        
        help_texts = {
            'subject': 'Group to which this message belongs to',
            'compound': 'C11/F18',
        }
        
class PerfScanForm(forms.ModelForm):
    class Meta:
        model = Scan
        # fields = ['email', 'name', 'subject', 'compound', 'current_status', 'date_for_scan', 'time_for_scan']
        fields = ['toi_activity', 'scan_time']
        # exclude = ['email', 'name', 'current_status']
        
        help_texts = {
            'subject': 'Group to which this message belongs to',
            'compound': 'C11/F18',
        }
    
    # def save(self, commit=True):
    #     scan = super(ScanForm, self).save(commit=False)
    #     scan.email = self.cleaned_data['email']
    #     
    #     if commit:
    #         scan.save()
    #     
    #     return scan