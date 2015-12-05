from django.db import models

# Create your models here.
class Scan(models.Model):
    subject = models.CharField(max_length = 10)
    compound = models.CharField(max_length = 3)
    current_status = models.CharField(max_length=20)
    
    #get from request.user
    name = models.CharField(verbose_name="full name", max_length=30)
    # name = request.user
    email = models.EmailField(max_length=120)
    # email = name.email
    request_date = models.DateField(auto_now_add=True, auto_now=False)
    updated_date = models.DateField(auto_now_add=False, auto_now=True)
    request_time = models.TimeField(auto_now_add=True, auto_now=False)
    updated_time = models.TimeField(auto_now_add=False, auto_now=True)
    date_for_scan = models.CharField(max_length = 30)
    time_for_scan = models.CharField(max_length = 30)

    def __str__(self):
        return self.email
    
