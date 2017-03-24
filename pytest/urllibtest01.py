#coding=utf-8
import urllib.request,urllib.parse,urllib.error
import http.cookiejar

__author__='wtj'
'''
这个学习blogcookie登录的例子 博客地址 ：http://blog.csdn.net/pipisorry/article/details/47948065
'''
LOGIN_URL="http://acm.hit.edu.cn/hoj/system/login"
values={'user':'####','password':'###','submit':'Login'}
postDate=urllib.parse.urlencode(values).encode()
user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36"
headers={'User-Agent':user_agent,'Connection':'keep-alive'}
cooke_filename='cookie.txt'
cookie=http.cookiejar.LWPCookieJar(cooke_filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
request=urllib.request.Request(LOGIN_URL,postDate,headers)
try:
	response=opener.open(request)
	page=response.read()
	with open("main.html","wb+") as f :
		f.write(page)
except urllib.error.URLError as e:
	print(e.code,";",e.reason)
cookie.save(ignore_discard=True,ignore_expires=True)
#print(cookie)
for item in cookie:
	print(item.name)
	print(item.value)
get_url="http://acm.hit.edu.cn/hoj/problem/solution/?problem=1"
res=urllib.request.Request(get_url,headers=headers)

res=opener.open(res)
#print(res.read().decode())
with open("otherpage.html","wb+") as f2 :
	f2.write(res.read())
