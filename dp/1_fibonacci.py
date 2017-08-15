# top down
class fibonacci:
	def __init__(self,n,a,b):
		self.n = n
		self.arr = [None for _ in xrange(n+1)]
		self.arr[0]=0
		self.arr[1]=a
		self.arr[2]=b
	def getValue(self,n):
		if self.arr[n] != None:
			return self.arr[n]
		v1 = self.arr[n-1]
		v2 = self.arr[n-2]
		if v1==None:
			v1=self.getValue(n-1)
		if v2 == None:
			v2 = self.getValue(n-2)
		self.arr[n] = v1+v2
		print self.arr[n]
		return self.arr[n]
	def getValue2(self):
		return self.getValue(self.n)

#bottom up
class fibonacci2:
	def __init__(self,n,a,b):
		self.n = n
		self.arr = [None for _ in xrange(n+1)]
		self.arr[0]=0
		self.arr[1]=a
		self.arr[2]=b
	def bottomUp(self):
		for i in xrange(3,self.n+1):
			self.arr[i] = self.arr[i-1]+self.arr[i-2]
			print self.arr[i]
	def getValue2(self):
		self.bottomUp()
		return self.arr[self.n]

# optimized solution
class fibonacci3:
	def __init__(self,n,a,b):
		self.n = n
		self.a=a
		self.b=b
	def bottomUp(self):
		count = self.n-2
		while count>0:
			print self.a,self.b
			self.a,self.b=self.b,self.a+self.b
			count-=1
		return self.b
	def getValue2(self):
		return self.bottomUp()
n=10-1
#f1=fibonacci2(n,1,1)
f1=fibonacci3(n,1,1)
print f1.getValue2()

