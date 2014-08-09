__author__ = 'Administrator'
import sys,time
j = '#'
if __name__ == '__main__':
	for i in  range(1,100):
		j += '#'
		sys.stdout.write(str(int((i/60)*100))+'%  ||'+j+'->'+"\r")
		sys.stdout.flush()
		time.sleep(0.1)
print

