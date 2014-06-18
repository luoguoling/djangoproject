from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext
from django.forms.formsets import formset_factory
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from login1app.models import login1
from django.db import connection,transaction
from django.template import loader,Context
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html',RequestContext(request,{'form':form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                return render_to_response('index.html',RequestContext(request))
            else:
                return render_to_response('login.html',RequestContext(request,{'form':form,'password_is_wrong':True}))
        else:
            return render_to_response('login.html',RequestContext(request,{'form':form,}))
def view(request):
#    raw1_sql = 'insert into login1app_login1 (id,username,password) values (6,"roling333533","aaawrwer")'
#    posts = login1.objects.raw(raw1_sql)

    raw_sql = 'select * from login1app_login1'
    posts =  login1.objects.raw(raw_sql)

 #   posts = login1.objects.all()

#    t = loader.get_template("archive.html")
#    c = Context({'posts':posts})
    return render_to_response('archive.html',RequestContext(request,{'posts':posts}))
def sql(request):
    cursor = connection.cursor()
    cursor.execute('insert into login1app_login1 (id,username,password) values (8,"roling333533","aaa88wrwedreeeee")')
    transaction.commit_unless_managed()
    return HttpResponse('ok')
    cursor.execute('select * from login1app_login1')
    raw = cursor.fetchone()
    return render_to_response('archive.html',RequestContext({'raw':raw}))