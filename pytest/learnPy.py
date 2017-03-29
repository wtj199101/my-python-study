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
	# print(dict)# {2: 33, 'a': 22} #顺序反了
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