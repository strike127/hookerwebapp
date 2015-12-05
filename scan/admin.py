from django.contrib import admin

# Register your models here.
from .forms import ScanForm
from .models import Scan

class RequestScanAdmin(admin.ModelAdmin):
    list_display = ["__str__", "name", "subject", "compound", "date_for_scan", "time_for_scan", "request_date", "request_time", "updated_date", "updated_time", "current_status"]
    form = ScanForm
        
admin.site.register(Scan, RequestScanAdmin)
    
    