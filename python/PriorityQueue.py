##### TODO: Implement it! #####

class PriorityQueue:
	def __init__(self, array = None):
		if array:
			self.heap = self.heapify(array)
		else:
			self.heap = []

	def findChildren(self, i):
		leftIdx = i * 2 + 1
		rightIdx = i * 2 + 2
		
		return (leftIdx, rightIdx)

	def findParent(self, i):
		
		return (i - 1) // 2



