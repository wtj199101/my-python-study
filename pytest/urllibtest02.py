#coding=utf-8
import urllib.request,urllib.parse,urllib.error
import http.cookiejar

__author__='wtj'
'''
这个学习blogcookie登录的例子 博客地址 ：http://blog.csdn.net/pipisorry/article/details/47948065
'''
cookie_file='cookie.txt'
cookie=http.cookiejar.MozillaCookieJar(cookie_file)
cookie.load(cookie_file,ignore_discard=True,ignore_expires=True)
print(cookie)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
get_url = 'http://acm.hit.edu.cn/hoj/problem/solution/?problem=1'  
req=urllib.request.Request(get_url)
res=opener.open(req)
with open("cookieTest2.html","wb+") as f:
	f.write(res.read())