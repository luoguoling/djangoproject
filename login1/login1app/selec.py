__author__ = 'Administrator'
#from django.db import connection
#import  MySQLdb
#conn = MySQLdb.connect(
#    host='127.0.0.1',
#    user='root',
#    passwd='abc123?',
#    db='login1',
#    port=3306,
#    charset='utf8')
#print conn
#def mysql():
#    cxn = conn.cursor()
#    sql = '''select * from login1app_login1'''
#    cxn.execute(sql)
#    r1 = cxn.fetchone()
#    print r1
#    cxn.close()
#    conn.close()
#if __name__ == '__main__':
#    mysql()
from login1app.models import login1
raw_sql = 'insert into login1app_login1 (id,username,password) values (3,"roling33","aaawrwer")'
a = login1.objects.raw(raw_sql)