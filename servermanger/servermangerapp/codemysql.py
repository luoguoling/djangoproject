__author__ = 'Administrator'
MEDIA_ROOT = "D:/django/"
import zipfile,os
from django.http import HttpResponse

def handle_uploaded_filemysql(f):
    name = "%s" % f.name
    destination = open('%s/%s' % (MEDIA_ROOT, name), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
