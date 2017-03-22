#coding:utf-8
import sys
import webbrowser
import os
import time
import subprocess
import logging
'''
一键打开工作中需要的程序
'''
logging.basicConfig(level=logging.DEBUG,filename='logs.log',filemode='w',
format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
logging.info('开始打开网页程序')
try:
	url='http://bug.dev.xjh.com/'
	webbrowser.open_new_tab(url)
	time.sleep(2)
	os.system('start '+'D:\\zookeeper-3.3.6\\bin\\zkServer.cmd')
	#subprocess.Popen('D:\zookeeper-3.3.6\bin\zkServer.cmd')
	time.sleep(2)
	subprocess.Popen('D:\\software\\eclipse\\eclipse.exe')
	time.sleep(2)
	subprocess.Popen('D:\\Program\\PLSQLDeveloper\\plsqldev.exe')
	time.sleep(2)
	os.system('D:\\QQ\\Bin\\QQScLauncher.exe')
	os.system('D:\\software\\MailMaster\\Start.exe')
	#subprocess.Popen(r"D:\\Program\\Notepad++\\notepad++.exe xjhconfig.txt")
	logging.info('结束打开网页程序')
except Exception as e:
	logging.error('打开程序错误')
	print(e)

