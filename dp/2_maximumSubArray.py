#bottom up
class maxSubArr:
	def __init__(self,arr):
		self.arr = arr
		self.n = len(arr)
		self.max1=arr[0]
		self.stack=arr[0]
	def bottomUp(self):
		for i in xrange(1,self.n):
			if self.stack<0:
				self.stack=self.arr[i]
			else:
				if self.arr[i]+self.stack>=0:
					self.stack+=self.arr[i]
				else:
					self.stack = self.arr[i]
			self.max1=max(self.max1,self.stack)
	def getValue(self):
		self.bottomUp()
		return self.max1
arr=[2, -9, 5, 1, -4, 6, 0, -7, 8]
m1 = maxSubArr(arr)
print m1.getValue()