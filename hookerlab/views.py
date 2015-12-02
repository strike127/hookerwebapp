from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

def home(request):
    context = {}
    template = "home.html"
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
         return HttpResponseRedirect('/loggedin/')
    else:
         return HttpResponseRedirect('/invalid/')
    
def loggedin(request):
    context = {'full_name':request.user.username}
    template = "loggedin.html"
    return render(request, template, context)

def invalid_login(request):
    return render(request, 'invalid_login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')