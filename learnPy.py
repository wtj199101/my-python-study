#coding=utf-8
'''
学习python3基础
###http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000
'''

#1、输入和输出
	#print()
	#input()
	####python 大小写敏感

#2、 数据类型
	#整数 1
	#浮点数 2.3  超出范围 inf (无限大)
	#字符串 "sdf"   单双引号相同  \n ：换行 \t ： tab  r'' ：表示不转译 
	#  '''...'''' 表示多行内容
	#print(''' line1
	   #	lien2
	#	lie3''')
	#布尔值 True/False
	#空值 None
	#print(r'\t sdfds') \t sdfds

#3、字符串和编码
	#ord()取字符的整数
	#chr()整数转字符
	#print(ord('a')) #A65   a97
	#print(chr(97))
	#print('\u4e2d\u6587') 中文
	#encode('utf-8'),decode('utf-8')
	#print(len(b'abc'))
	#格式化 要带后面带%
	#print('hello %s,age=0%d0 %%' %('zhangsan',12))
	#print('%.2f' %3.1415926)

#4 list  && tuple
	#list:append insert pop
	# list=[1,'2']
	# list.append(3)
	# list.insert(3,'4')
	# list.pop(0)
	# list[0]=2
	# list[-1]=4
	# print(list)
	###tuple
	# t=(1)  1
	# b=(1,)  
	# print(t)  number 1
	# print(b) tuple  (1,)
	# t=(1,2,[3,4])
	# print(t)
	# t[2][0]=5
	# t[2][1]=6
	# print(t)
#5 条件判断 循环
	# if True:
	# 	print ('a');
	# else: #elif
	# 	print ('b');
	# for name in range(5):
	# 	if name==2:
	# 		continue
	# 	if name==3:
	# 		break
	# 	print (name);
	# sum=0
	# n=100
	# while n>0:
	# 	sum+=n
	# 	n-=1
	# print(sum)
#6 dict && set
	# dict={'a':22,2:33}
	# print(dict)# {2: 33, 'a': 22} #顺序反了 说明顺序不一定一致
	# print(dict[2])  #33
	# print(dict['a']) # 22
	# print('33' in dict)  #false
	# print(dict.get(2)) #33
	# print(dict.set(2,44))  #exception 'dict' object has no attribute 'set'
	###set
	# s=set([1,2,3,4,1,2,3])
	# s2=set([5,6,7,1,2])
	#add() remove()
	# print(s)
	# print(s&s2)
	# print(s | s2)
##7 函数 function
	# def my_abs(x):
	# 	if not isinstance(x,(int,float)):
	# 		raise TypeError("bad param")
	# 	if x>=0:
	# 		return x
	# 	else:
	# 		return -x
	# print(my_abs('123'))
	# def nop():
	# 	pass
	# print(nop())
	# def returnValue(x,y,c=0):
	# 	return x,y,c
	# print(returnValue(1,2))  #函数的返回值是一个元组 无返回值时自动return None
	#默认参数使用不可变变量
	#reason:
	# def _abc(l=[]):
	# 	l.append('2')
	# 	#print(l)
	# 	return l
	# print(_abc([1,2,3]))
	# print(_abc([12312,123,123]))
	# print(_abc())#['2']
	# print(_abc())#['2', '2']
	#可变参数 *number
	# def calc(*num):
	# 	sum=0
	# 	for n in num:
	# 		sum=n+sum
	# 	print( sum)
	#a=(1,2,3,4)
	#b=[1,2,3,4]
	#c=([1,2,3,4])
	#calc(1,2,3,4)
	#calc(*c) 
	#对于一个可变参数可以使元组、list、set 但是前面要加*
	#关键字参数 **kw  放入的是dict
	# def person(name,age,**kw):
	# 	print('name:%s,age:%d' %(name,age) ,'other:',kw )
	# person("zhansan",12)
	# person("lisi",15,city='beijing')
	# d={"city":"shanghai","job":"sales"}
	# person("wangwu",20,**d) #name:wangwu,age:20 other: {'job': 'sales', 'city': 'shanghai'}
	#命名关键字参数
	# def person(name,age,*,city):
	# 	print(name,age,city)
	# person("jack",24,city='shanghai')
	# d={"city":"bieji"}
	# person("jack",24,**d)
	#如果函数中有可变参数。后面的参数为命名参数
	#参数的定义顺序：必须参数、默认参数、可变参数、命名|关键字参数
	#递归函数 和尾递归优化
	# def fact(n):
	# 	if n==0:
	# 		return 1
	# 	return n*fact(n-1)
	# print(fact(100))
	# def fact_iter(num,pro):
	# 	if(num==1):
	# 		return pro
	# 	return fact_iter(num-1,num*pro)
	# print(fact_iter(100,1))
#---end 0329
#高级特性：切片，迭代，列表生成，生成器，迭代器
# l=[1,2,3]
# print(l[-1:])#3
# print(l[:1])#1
#python 没有字符串的substring 用切片就可以了。
#enumerate 可以list 变成索引元素
# for i,value in enumerate([1,2,3]):
# 	print(i,value)
#range(1,100,2)
# l=list(range(1,100,2))
# print(l)
# import os
# print([d for d in os.listdir('.')])
#生成器 generator
#迭代器Iterator
# from collections import Iterator 
# print(isinstance(iter([]),Iterator)) #Iterable  与 Iterator  
# 				#for 循环都是Iterable的  但不是iterator对象。可以通过iter()获得iterator 对象

###函数式编程
# map/reduce
# map参数：一个函数，一个iterable  iteratable 每个元素调用一次函数
# reduce ：一个函数：一个iterable iteratable 每个都调用一次函数后的结果与前面相加最终输出一个结果
# filter / sorted 过滤和排序
#返回函数 函数当成结果返回
#匿名函数
# print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#装饰器
# def log (func):
# 	def wrapper(*args,**kw):
# 		print('call %s:' %func.__name__)
# 		return func(*args,**kw)
# 	return wrapper
# @log
# def now():
# 	print('2017/03/30')
# f=now
# f()
# print(f.__name__)
#偏函数


#模块
# pip install Pillow

#面向对象
# class Student(object):
# 	def __init__(self,name,age):
# 		self.__name=name
# 		self.__age=age
# 	def print_age(self):
# 		print('name:%s,age:%d' %(self.__name,self.__age))
# b=Student("zhangsan",15)
# c=Student("lisi",20)
# b.print_age()
# c.print_age()
# b.name="wangwu"
# b.print_age()
# print(b._Student__name)
# 访问限制  __ 两个杠表示私有变量 _一个表示变量最好不要修改 _Strudent__name 可以访问私有变量 
#对应不能访问的私有变量 可以改定get set 方法
 # def get_name(self):
 #        return self.__name

 #    def get_score(self):
 #        return self.__score
# class Animal(object):
#  	def run():
#  		print ('animal is running....')
# class Dog(Animal):
#  	def run(self):
#  		print("dog is running....")
# class Cat(Animal):
#  	def run(self):
#  		print('Cat is running....')
# dog=Dog()
# dog.run()
# Cat().run()
#判断对象属性 type() | isinstance()
# 实例属性和类属性
# class Student(object):
#     name = 'Student'

#面向对象高级
#__slots__ 限制类添加的属性
# @property
class Student(object):
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self,value):
		if(not isinstance (value,int)):
			raise TypeError("value must be int")
		if value<0 or value>100 :
			raise TypeError("value must be 0~100")
		self._score=value
# s=Student()
# s.score=60
# print(s.score)
# class Student(object):
# s=Student()
# s._score=60
# print(s.score)
# @property get 属性 _score和score都是对象属性 不是类属性 这两个相同
# 多重继承
# class Dog(Mammal, Runnable):  MixIn
# 常见定制类
# __str__ print(object) 显示的字符串
# __repr__ object 命令行显示的字符串
# __iter__ 返回迭代对象 还需实现__next__取得下一个值
# __getitem__ object  类型 a()[0] 这种下标取值要实现这个方法
# __setitem__  __delitem__
# __getattr__ 当获取一个不存在的属相时，会调用这个方法

# __call__ 实例对象本身调用

# 判断一个变量是对象还是函数 callable()
# print(callable(Student()))
# class chain(object):
# 	def __init__(self,path=''):
# 		self._path=path
# 	def __getattr__(self,path):
# 		return chain('%s/%s'%(self._path,path))
# 	def __str__(self):
# 		return self._path
# 	def __call__(self,path):
# 		return chain('%s/%s'%(self._path,path))
# 	__repr__=__str__
# print(chain().status.user('sdfsd').timeline.list)  ##/status/user/sdfsd/timeline/list
# .status 调用的是 __getattr__ ,.user() 调用的是 __call__  

# enum 枚举类
# from enum import  Enum
# Month=Enum('month',('jan','Feb','Mar'))
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)
# from enum import Enum, unique

# @unique
# class Weekday(Enum):
#     Sun=9 # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
# day1=Weekday.Sun.value
# # day1=Weekday(1)
# print(day1)

# 元类
# 动态创建类
# def fn(self,name='world'):
# 	print('hello,%s'%name)
# Hello=type("Hello",(object,),dict(hello=fn))
# h=Hello()
# h.hello(name="goods")

# metaclass 元类 定义metaclass 创建类，创建实例
#metaclass 是类模板，继承type
# class ListMetaClass(type):
# 	def __new__(cls,name,bases,attrs): #cls=当前创建类对象，name=类的名字，bases=父类集合，attrs=类方法集合
# 		attrs['add']=lambda self,value:self.append(value)
# 		return type.__new__(cls,name,bases,attrs)
# class Mylist(list,metaclass=ListMetaClass):
# 	pass

# L=Mylist()
# L.add(1)
# print(L)  使用范围 orm 可以使用必须动态生成的时候使用
# 错误、调试和测试
# import logging
# import pdb
# try:
# 	# pdb.set_trace()
# 	r=10/2
# 	# assert(r)
# except Exception as e :
# 	print(e)
# 	logging.exception(e)
# 	raise  # 不带参数原样抛出
# finally:
# 	print("end")
##测试会logging  会debug 就行
# IO编程
# 文件:
# open()
# read()
# close()
# 内存：
# StringIO
# from io import StringIO
# f=StringIO()
# f.write("hello")
# print(f.getvalue())
# BytesIO 操作二进制
# os.name #nt windows posix linux
# os.version.get('path') #系统环境path
# import os
# # print(os.path.abspath('.'))#C:\Users\Administrator\Desktop\pyTest
# # os.path.join(os.path.abspath('.'),"test")#连接字符串  os.path.split() 分隔路径  os.path.splittext()得到文件扩展名
# # os.mkdir()  os.rmdir()  创建和删除目录
# print(os.path.join(os.path.abspath('.'),"learnPy.py"))
# print(os.path.splitext(os.path.join(os.path.abspath('.'),"learnPy.py"))[1])#.py
# # os.rename(a,b) || os.remove()
# print([x for x in os.listdir('.') if os.path.isdir(x)])  #['.git', 'img', 'log', 'pytest', 'validateimg']
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']) #['learnPy.py']
# pickle 序列化
# import pickle 
# d=dict(name='bob',age=20)
# pickle.dumps(d,file) 可以序列化写入文件
# pickle.loads() 反序列化
# print(d)
#json 
# import json
# d=dict(name="zhangsan",age=20)
# print(json.dumps(d))
# json.loads()

# 多进程和多线程
# linux 用 os.fork()

# import os,time,random
# # print(os.getpid())
# # print(os.getppid())
# from multiprocessing import Process
# from multiprocessing import Pool

# def long_time_task(name):
# 	print('run child procss %s (%s)'%(name,os.getpid()))
# 	start =time.time()
# 	time.sleep(random.random()*3)
# 	end =time.time()
# 	print('Task %s run %0.2f seconds'%(name,(end-start)))
# if  __name__=='__main__':
# 	print('parent proces %s.'%os.getpid())
# 	p=Pool(4)
# 	for i in range(5):
# 		p.apply_async(long_time_task,args=(i,))

	# p=Process(target=run_proc,args=('test',))
	# print('wating all subprocess done')
	# p.close()
	# p.join()
	# print('All process end')


	# subprocess 子进程   communicate 可以继续
# import subprocess
# p=subprocess.Popen(['java'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# # out,err=p.communicate(b' -version')
# # print(out.decode('utf-8'))
# print('exit Code:',p.returncode)
#线程
# import time,threading
# def loop():
# 	print('threading %s is running .'%threading.current_thread().name)
# 	n=0
# 	while n<5:
# 		n+=1
# 		print('threading %s >>>%s'%(threading.current_thread().name,n))
# 		time.sleep(3)
# 	print('thread %s end'%threading.current_thread().name)
# print('thread %s is running.'%threading.current_thread().name)
# t=threading.Thread(target=loop,name='LoopThread')
# t2=threading.Thread(target=loop,name='LoopThread2')
# t.start()
# t2.start()
# t.join()
# t2.join()
# print('thread  %s is end '%threading.current_thread().name)
# threading.local() threadLocal 跟其他语言一样保存线程变量的
# 线程因为python 有gil 全局的锁。每个线程执行一段时间放弃这个锁。下个线程才有可能拿到执行。所以只是单线程在跑。python还是用多进程
# 好点。

# 常用内建模块
# 正则
# s=r'dsfsad\--'  r不考虑转译
# print(s)
# import re
# if re.match(r'\d{3}\-\d{3,8}','010-12345'):
# 	print('ok')
# # re 编译  非贪婪配置加?
# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# print(re_telephone.match('010-12345').groups())
# print(re.match(r'^(\d+?)(0*)$', '102300').groups())
# from datetime import datetime,timedelta
# print(datetime.now())#2017-04-01 14:51:17.366733datetime.strptime()
# dates=datetime.strptime('2017-04-01 14:51:17','%Y-%m-%d %H:%M:%S')
# print(type(dates))
# strd=dates.strftime('%Y-%m-%d %H:%M:%S')
# print(type(strd))
# now=datetime.now()
# now2=now+timedelta(days=2,hours=1)
# print(now2)

# collections
# namedtuple
# OrderedDict 有序的dict  根据插入的顺序排序
# Counter 计数器

# base64 编码解码

#struct 解决二进制数据类虚拟改

#hashlib 提供了常见的摘要算法 MD5,SHA-1
# import hashlib
# md5=hashlib.md5()
# md5.update('123456'.encode('utf-8'))
# print(md5.hexdigest()) #e10adc3949ba59abbe56e057f20f883e
# sha1=hashlib.sha1()
# sha1.update('123456'.encode('utf-8'))
# print(sha1.hexdigest())#7c4a8d09ca3762af61e59520943dc26494f8941b

#itertools
# count() 自然序列不限重复
# cycle() 传入的值无线重复
# repeat()把一个值无线重复。可控次数
# chain()把一组迭代对象串联起来，形成一个更大的迭代器：
# groupby()迭代器中相邻的重复元素挑出来放在一起

#contextlib
#xml
#HTMLParser
#urllib

# 常见第三方模块
# pillow 图像 
# virtualenv 隔离的python环境

# tcp编程
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('www.baidu.com',80))

# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
# from email.mime.text import MIMEText
# msg=MIMEText('hello,world.send by python','plain','utf-8')
# from_addr=input('from:')
# password=input('password:')

# to_addr=input("to:")
# smtp_server=input("SMTP server:")
# import smtplib
# server=smtplib.SMTP(smtp_server,25)
# server.set_debuglevel(1)
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()
# smtp 发送邮件pop3接收邮件
# 数据库 sqlite mysql sqlAlchemy
# web 开发
# WSGI
# 从wsgiref模块导入:
# from wsgiref.simple_server import make_server
# # 导入我们自己编写的application函数:
# from hello import application

# # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
# httpd = make_server('', 8000, application)
# print('Serving HTTP on port 8000...')
# # 开始监听HTTP请求:
# httpd.serve_forever()

# # 框架和模板
# 协程
# asyncio 异步io