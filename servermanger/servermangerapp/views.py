#coding:utf-8
from django.shortcuts import render
import socket,re,commands
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from multiprocessing import Pool
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from code import handle_uploaded_file
from codemysql import handle_uploaded_filemysql
from django.http import HttpResponse
from forms import UploadFileForm
from forms import UploadFileFormmysql
from models import ServerManger
from forms import LoginForm
def socket_send(ip,javadir,agent,zone):
    md5command = "md5sum /var/ftp/qmrserver/files_md5.txt"
    status,output = commands.getstatusoutput(md5command)
    filesmd5 = re.split(" ",output)[0]
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,1002))
    remote_command = "update_java,dlkjiDte76EQ093634lkfey34lkkjiye,%s,%s" %(javadir,filesmd5)
    sock.send(remote_command)
    result = sock.recv(2048)
    sock.close()
    if int(result) == 0:
        print "%s %s update java successful" %(agent,zone)
        a = "%s %s update java successful" % (agent,zone)
    else:
        print "%s %s update java fail" % (agent,zone)
        a = "%s %s update java fail" % (agent,zone)
    return a
def socket_sendgamedata(ip,gamedatadbname,gamedatadbport,agent,zone):
    md5command = "md5sum /var/ftp/gamedata/game_data.sql"
    status,output = commands.getstatusoutput(md5command)
    filesmd5 = re.split(" ",output)[0]
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,1002))
    remote_command = "update_gamedata,dfjedfei15ADFEpoi9340dAEgee0e,%s,%s,%s" %(gamedatadbname,gamedatadbport,filesmd5)
    sock.send(remote_command)
    result = sock.recv(2048)
    sock.close()
    if int(result) == 0:
#        print "%s %s update game_data successful" %(agent,zone)
        a = "%s %s update game_data successful" % (agent,zone)
    else:
#        print "%s %s update game_data fail" %(agent,zone)
        a = "%s %s update game_data fail" % (agent,zone)
    return a
def list(request):
    server_mangers = ServerManger.objects.all().order_by('zone').filter(zone__gt=69)
    agent = 'hgpupugame'
    if request.method == 'POST':
        server_list = request.POST.getlist('chk_list')
        action = request.POST['value']
        pool = Pool(processes=10)
        result = []
        print 'Server list:%s' % server_list
        print type(server_list)
        servers = ServerManger.objects.values('ip','gamedatadbname','gamedatadbport','agent','zone','javadir','wwwdir').filter(zone__in=server_list)
        for item in servers:
            if action == u'更新版本':
                print 'javadir is %s' % item['javadir']
                res = pool.apply_async(socket_send,(item['ip'], item['javadir'], agent, item['zone'],))

            return render_to_response('list.html',{'result':result},context_instance=RequestContext(request))
    return render_to_response('list.html',{'list': server_mangers},context_instance=RequestContext(request))
def view(request):
    return render_to_response('a.html')
def view1(request):
    return render_to_response('d.html')
def view2(request):
    return render_to_response('b.html')
def view4(request):
    list = ServerManger.objects.all().order_by('zone')
    return render_to_response('list4.html',RequestContext(request,{'list':list}))
def view3(request):
    server_mangers = ServerManger.objects.all().order_by('zone').filter(zone__gt=69)
    agent = 'hgpupugame'
    if request.method == 'POST':
        server_list = request.POST.getlist('chk_list')
        action = request.POST['value']
        pool = Pool(processes=10)
        result = []
        print 'Server list:%s' % server_list
        print type(server_list)
        servers = ServerManger.objects.values('ip','gamedatadbname','gamedatadbport','agent','zone','javadir','wwwdir').filter(zone__in=server_list)
        for item in servers:
           # if action == u'更新版本':
            #    print 'javadir is %s' % item['javadir']
            #    res = pool.apply_async(socket_send,(item['ip'], item['javadir'], agent, item['zone'],))
            #    result.append(res.get(timeout=20))
    #    return render_to_response('list.html',{'result':result},context_instance=RequestContext(request))
    #return render_to_response('list.html',{'list': server_mangers},context_instance=RequestContext(request))
            if action == u'更新数据库':
#                print 'gamedatadbname is %s' % item['gamedatadbname']
                res = pool.apply_async(socket_sendgamedata,(item['ip'],item['gamedatadbname'],item['gamedatadbport'],agent,item['zone'],))
                #result.append(res.get(timeout=20))
            return render_to_response('list1.html',{'result':result},context_instance=RequestContext(request))
    return render_to_response('list1.html',{'list': server_mangers},context_instance=RequestContext(request))
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['file'])
                html = u"<html><body>Upload Success</body></html>"
                return HttpResponse(html)
            except:
                html=u"<html><body>没有选择文件!!!</body></html>"
                return HttpResponse(html)
        else:
            return HttpResponseRedirect('list')
    else:
        form = UploadFileForm()
        return render_to_response('upload.html',RequestContext(request,{'form':form}))
def uploadmysql(request):
    if request.method == 'POST':
        form = UploadFileFormmysql(request.POST, request.FILES)
        if form.is_valid():
            try:
                handle_uploaded_filemysql(request.FILES['file'])
                html = u"<html><body>Upload Success</body></html>"
                return HttpResponse(html)
            except:
                html=u"<html><body>没有选择文件!!!</body></html>"
                return HttpResponse(html)
        else:
            return HttpResponseRedirect('list')
    else:
        form = UploadFileFormmysql()
        return render_to_response('uploadmysql.html',RequestContext(request,{'form':form}))

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login1.html',RequestContext(request,{'form':form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')



            user = auth.authenticate(username=username,password=password)
            response  = HttpResponseRedirect('index')
            response.set_cookie('username',username,max_age=3600)
#            return response

            if user is not None and user.is_active:
                auth.login(request,user)
                print request.user
                return render_to_response('a.html',RequestContext(request))
            else:
                return render_to_response('login1.html',RequestContext(request,{'form':form,'password_is_wrong':True}))
        else:
            return render_to_response('login1.html',RequestContext(request,{'form':form,}))


def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
    #        password = request.POST.get('password','')
   #         user = auth.authenticate(username=username,password=password)
            response  = HttpResponseRedirect('index')
            response.set_cookie('username',username,max_age=300)
            return response


def index(request):
    username = request.COOKIES.get('username','')
    return render_to_response('b.html',{'username':username})


#def index(request):
#    response = set_session()
 #   username = request.COOKIES.get('username','')

  #  return render_to_response('b.html',{'username':username})
def logout(request):
#    response = HttpResponse('logout!!!')
#    response.delete_cookie('username')
#    return response
    auth.logout(request)
    return HttpResponseRedirect('login')
