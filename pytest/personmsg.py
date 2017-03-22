 # -*- coding: utf-8 -*-
import os,urllib
from urllib import request,parse
import io
from _io import StringIO
from bs4 import BeautifulSoup
import  sqlite3 
__author__='wtj'
#os.popen("echo off")
_curpath=os.getcwd();#z这个不带\\
#os.chdir('C:\\Users\\Administrator\\Desktop\\pyTest\\pytest')
#print(_curpath)
#print(_curpath.read()+'py.log')

with open(_curpath+'\\py.log','a+',encoding='utf-8')  as f :
	#print(f.readline())
	#print(os.getlogin())
	#print(os.getpid())
	#print(os.getcwdb())
	#print(os.listdir('.'))
	response =urllib.request.urlopen("http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201608/t20160809_1386477.html")
	#response.encode="utf-8"
	html=BeautifulSoup(response.read(),"html.parser")
	#response.read();

	div=html.find_all('p',class_='MsoNormal');
	#print(div2)
	#print(html.prettify())
	#print(div)
	conn=sqlite3.connect('C:\\Users\\Administrator\\Desktop\\test.db')
	conn.execute('drop table if exists personmsg;')
	conn.execute('create table personmsg (id  integer primary key  AUTOINCREMENT not null,code text not null,address text not null);')
	list2=[]
	for k in div:	
		list1=[]
		for ch in k.children:
			if(ch.string==None):
				list1.append(ch.contents[0])			
			else:
				list1.append(ch.string.strip())
		list2.append(list1)
	#print(len(list2));
	#print(list2)
	for dist in list2 :
		#print (dist)
		conn.execute("insert into  personmsg (code,address)values(?,?);",dist)
		f.write(','.join(dist)+"\n")
	#doc=BeautifulSoup(str(div),"html.parser")
	#print(div)
	#f.write(str(div))
	conn.commit()
	res=conn.execute('select * from personmsg limit 10;')
	print(res.fetchall())
	conn.close()


