"""hookerlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'hookerlab.views.home', name='home'),
    # url(r'^login/', 'hookerlab.views.login', name='login'),
    url(r'^auth/', 'hookerlab.views.auth_view', name='auth_view'),
    url(r'^logout/', 'hookerlab.views.logout', name='logout'),
    # url(r'^loggedin/', 'scan.views.scan', name='loggedin'),
    url(r'^invalid/', 'hookerlab.views.invalid_login', name='invalid_login'),
    url(r'^register/', 'hookerlab.views.register_user', name='register_user'),
    url(r'^register_success/', 'hookerlab.views.register_success', name='register_success'),
    # url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^request_scan/', 'scan.views.request_scan', name='requestscan'),
    url(r'^scan_requested/', 'scan.views.scan_requested', name='scanrequested'),
    url(r'^request_synthesis/(?P<current_id>\d+)/', 'scan.views.synthesize_request', name='requestsynth'),
    url(r'^synthesized/', 'scan.views.synthesized', name='synthesized'),
    url(r'^perform_scan/(?P<current_id>\d+)/', 'scan.views.perform_scan_request', name='perfScan'),
    url(r'^scan_complete/', 'scan.views.perform_scan_completed', name='scancomplete'),
    # url(r'^table/', 'scan.views.scan', name='people'),
    # url(r'^people/', 'person.views.people', name='people'),
    
    
]
