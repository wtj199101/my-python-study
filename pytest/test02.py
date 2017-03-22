class Persion:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print(name,age)
	def persionInfo(self):
		print(self.name,self.age)
	def persionInfo2(self,name,age):
		print(name,age)
		#print(name,age)
if __name__=="__main__":
	c=Persion("zhangsan",22)
	c.persionInfo()
	c.persionInfo2("goods","hello")
	print(dir(c))
	delattr(c,"name")
	print(dir(c))