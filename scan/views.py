from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from scan.forms import ScanForm
from scan.models import Scan
from scan.forms import SynthesizeForm

# Create your views here.
def request_scan(request):
    if request.method == 'POST' or request.method == None:
        form = ScanForm(request.POST)
        user = request.user
        if form.is_valid():
            form = form.save(commit=False)
            form.name = user
            form.email = user.email
            form.current_status = 'Ordered'
            form.init_activity = '0.00'
            form.toi = '0.00'
            form.save()
            return HttpResponseRedirect('/scan_requested/')
    args = {}
    args.update(csrf(request))
    args['form'] = ScanForm()
    return render(request,'scan.html',args)

def scan_requested(request):
    return render(request, 'scan_requested.html')

def synthesize_request(request):
    if request.method == 'POST' or request.method == None:
        inst = Scan.objects.get(id = '_check')
        form = SynthesizeForm(request.POST, instance=inst)
        user = request.user
        if form.is_valid():
            form = form.save(commit=False)
            form.current_status = 'Synthesized'
            form.save()
            return HttpResponseRedirect('/synthesized/')
    args = {}
    args.update(csrf(request))
    args['form'] = SynthesizeForm()
    return render(request,'synthesis.html',args)

def synthesized(request):
    return render(request, 'synthesized.html')


def scan(request):
    if request.user.is_superuser():
        return render(request, "loggedin.html", {"obj": Scan.objects.all()})
    else:
        return render(request, "loggedin.html", {"obj": Scan.objects.filter(name = request.user.username)})
    # return render(request, "scantable.html", {"scan": Scan.objects.all()})
    # return render(request, "scantable.html", {"scan": Scan.objects.filter(compound = 'f18').values('name')})