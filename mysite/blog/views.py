from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from django.http import Http404

from models import BlogPost
from django.template.context import RequestContext
from django.shortcuts import render_to_response,render,get_object_or_404
def archive(request):
#    posts = BlogPost.objects.all()
#    t = loader.get_template("archive.html")
#    c = Context({'posts':posts})
#    return HttpResponse(t.render(c))
    try:
        raw_sql = 'select * from blog_blogpost'
        posts = BlogPost.objects.raw(raw_sql)
    except posts.DoesNotExist:
        raise Http404

    return render_to_response('archive.html',RequestContext(request,{'posts':posts}))

# Create your views here.
