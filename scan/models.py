from django.db import models

# Create your models here.
class Scan(models.Model):
    #request scan fields
    subject = models.CharField(max_length = 10)
    current_status = models.CharField(max_length=20)
    CHOICES = (
        ('C11','C11'),
        ('F18','F18')
        )
    compound = models.CharField(max_length=3, choices=CHOICES)
    name = models.CharField(verbose_name="full name", max_length=30)
    email = models.EmailField(max_length=120)
    date_for_scan = models.CharField(max_length = 30)
    time_for_scan = models.CharField(max_length = 30)
    request_date = models.DateField(auto_now_add=True, auto_now=False)
    updated_date = models.DateField(auto_now_add=False, auto_now=True)
    request_time = models.TimeField(auto_now_add=True, auto_now=False)
    updated_time = models.TimeField(auto_now_add=False, auto_now=True)
    
    #fields for synthesize
    init_activity = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    synthesize_time = models.CharField(max_length = 30)
    synthesize_time_auto = models.TimeField(auto_now_add=False, auto_now=True)
    
    #field for perform scan
    toi_activity = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    scan_time = models.CharField(max_length = 30)
    scan_time_auto = models.TimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return self.email
    
