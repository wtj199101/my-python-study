#coding=utf-8
#mport urllib.request,urllib.parse,urllib.error
#import http.cookiejar
import sqlite3 
import subprocess
import win32crypt

__author__='wtj'
'''
这个学习blogcookie登录的例子 博客地址 ：http://blog.csdn.net/pipisorry/article/details/47948065
'''
def get_chrome_cookies(url):
	WIN_COOKIES_DIR='C:\\Users\\Administrator\\AppData\\Local\\Google\Chrome\\User Data\Default\\Cookies'
	CUR_COOKIES_DIR='.\phython_chrome_cookie'
	subprocess.call(['copy',WIN_COOKIES_DIR,CUR_COOKIES_DIR],shell=True)
	conn=sqlite3.connect(CUR_COOKIES_DIR)
	for row in conn.execute('select host_key,name,path,value,encrypted_value from cookies'):
		print(row[0])
		if row[0] !=url:
			continue
		print(row[0])
		ret=win32crypt.CryptUnprotectData(row[4],None,None,None,0)
		print([ret[1].decode()])
		#ret_dict[row[1]]=ret[1].decode()
	conn.close()
