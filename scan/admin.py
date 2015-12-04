from django.contrib import admin

# Register your models here.
from .forms import ScanForm
from .models import Scan

class RequestScanAdmin(admin.ModelAdmin):
    list_display = ["__str__", "name", "subject", "compound", "date", "time", "updated_date", "updated_time", "currstat"]
    form = ScanForm
        
admin.site.register(Scan, RequestScanAdmin)
    
    