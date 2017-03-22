#coding: utf-8
import subprocess
import os
import logging
import time
'''
一键关闭程序 并且自动关机
'''
logging.basicConfig(level=logging.DEBUG,filename='logs.log',filemode='a',
format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
p=subprocess.Popen(["tasklist"],stdout=subprocess.PIPE)
out,err=p.communicate()
killlist=['chrome.exe','QQ.exe','notepad++.exe','plsqldev.exe','eclipse.exe','eclipse.exe *32','cmd.exe','wps.exe','YoudaoNote.exe','MailMaster.exe','conhost.exe']
for line in out.splitlines():
	try:
		line=bytes.decode(line)
		
		im=line.split()[0]
		
		if im in killlist:
			logging.info('关闭的程序为:'+im)
			pid=line.split()[1]
			os.system("taskkill /F /PID "+pid)
	except:
		continue


#100秒后关机 

time.sleep(10)
os.system('shutdown -s -t 10')

