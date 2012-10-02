#!/usr/bin/python
import os,sys

def sender(num,msg):
	str='echo %s | gammu sendsms text %s' %(msg,num)
	os.system(str)
	print "Msg sent to %s is successfully" %(num)
	
#store the message in msg variable
msg=sys.argv[2]
if len(msg)>160:
	print 'send only 160 chars'
else:
	msg.strip()

tfile=sys.argv[1]
t=tfile.split('.')
#check the file type 
if t[-1]!='txt':
	sender(sys.argv[1],msg)
else:	
	#open the contacts file	
	f=open(tfile,'r')
	#read line by line
	for line in f.readlines():
		line=line.split(', ')
		num=line[2]
		sender(num,msg)
	f.close()	
	#print "Finished Everything, Good Bye ! \n\n\n"
	#os.system('echo "Your ODOC Sending Task is Completed" | gammu --sendsms text 8015376450')
