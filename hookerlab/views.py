from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from hookerlab.forms import myRegistrationForm
from scan.views import scan
from scan.models import Scan

def home(request):
    title = ''
    template = "home.html"
    context = {}
    if request.user.is_authenticated():
        title = request.user.username
        if request.user.is_superuser:
            context = {
                "full_name":title,
                "obj_order": Scan.objects.filter(current_status = 'Ordered'),
                "obj_synth": Scan.objects.filter(current_status = 'Synthesized'),
            }
        else:
            context = {
                "full_name":title,
                "obj_order": Scan.objects.filter(name = title, current_status = 'Ordered'),
                "obj_synth": Scan.objects.filter(name = title, current_status = 'Synthesized'),
            }
        template = 'loggedin.html'
        return render(request, template, context)
    return render(request, template, context)

# def login(request):
#     context = {}
#     context.update(csrf(request))
#     template = "login.html"
#     return render(request, template, context)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
         auth.login(request,user)
         return HttpResponseRedirect('/')
    else:
         return HttpResponseRedirect('/invalid/')
    
def loggedin(request):
    context = {'full_name':request.user.username,}
    template = "loggedin.html"
    return render(request, template, context)

def invalid_login(request):
    return render(request, 'invalid_login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')

def register_user(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = myRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success/')
    args = {}
    args.update(csrf(request))
    # args['form'] = UserCreationForm()
    args['form'] = myRegistrationForm()
    return render(request,'register.html',args)

def register_success(request):
    return render(request, 'register_success.html')


