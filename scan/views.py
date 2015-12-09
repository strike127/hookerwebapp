from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from scan.forms import ScanForm
from scan.models import Scan

# Create your views here.
def request_scan(request):
    if request.method == 'POST' or request.method == None:
        form = ScanForm(request.POST)
        user = request.user
        print(user)
        if form.is_valid():
            form = form.save(commit=False)
            form.name = user
            form.email = user.email
            form.current_status = 'Ordered'
            form.save()
            return HttpResponseRedirect('/scan_requested/')
    args = {}
    args.update(csrf(request))
    args['form'] = ScanForm()
    return render(request,'scan.html',args)

def scan_requested(request):
    return render(request, 'scan_requested.html')

def scan(request):
    if request.user.is_superuser():
        return render(request, "loggedin.html", {"obj": Scan.objects.all()})
    else:
        return render(request, "loggedin.html", {"obj": Scan.objects.filter(name = request.user.username)})
    # return render(request, "scantable.html", {"scan": Scan.objects.all()})
    # return render(request, "scantable.html", {"scan": Scan.objects.filter(compound = 'f18').values('name')})