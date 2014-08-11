__author__ = 'Administrator'

MEDIA_ROOT = "D:/django/servermanger"
import zipfile,os
from django.http import HttpResponse

def handle_uploaded_file(f):
    name = "%s" % f.name
    destination = open('%s/%s' % (MEDIA_ROOT, name), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    unziplog(f)

def unziplog(f):

    finallog = ''
    name = "%s" % f.name
    print name
    if not zipfile.is_zipfile(name):
        errors = u"<html><body><I>can not unzip the uplog,please make sure the upfile is .zip</I></body></html>"
        return HttpResponse(errors)
    else:
        try:
            f = zipfile.ZipFile('%s/%s' % (MEDIA_ROOT, name), 'r')
            for name in f.namelist():
                finallog = name
                f.extract(finallog,'qmrserver')
        except Exception:
            errors = u"<html><body><I>unzip log file failed</I></body></html>"
            return HttpResponse(errors)
	    os.remove(f)
        return True