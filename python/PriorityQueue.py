import random

class PriorityQueue:
	def __init__(self):
		self.heap = []
		self.size = 0

	def append(self, num):

		child = self.size
		self.heap.append(num)
		self.size += 1

		while child > 0:
			parent = (child - 1) // 2
			if self.heap[child] < self.heap[parent]:
				self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
				child = parent
			else:
				break



	def pop(self):
		assert self.heap
			
		val = self.heap[0]
		self.size -= 1
		self.heap[0], self.heap[self.size] = self.heap[self.size], None

		i = 0
		while True:
			leftChild = 2 * i + 1
			rightChild = 2 * i + 2
			if leftChild >= self.size:
				break

			if rightChild >= self.size:
				if self.heap[i] <= self.heap[leftChild]:
					break
				else:
					self.heap[i], self.heap[leftChild] = self.heap[leftChild], self.heap[i]
					break

			if self.heap[i] <= self.heap[leftChild] and self.heap[i] <= self.heap[rightChild]:
				break
			if self.heap[leftChild] <= self.heap[rightChild]:
				self.heap[i], self.heap[leftChild] = self.heap[leftChild], self.heap[i]
				i = leftChild
				continue
			if self.heap[rightChild] < self.heap[leftChild]:
				self.heap[i], self.heap[rightChild] = self.heap[rightChild], self.heap[i]
				i = rightChild
				continue

		return val


pqTest = PriorityQueue()
for i in range(100, 1, -1):
	pqTest.append(random.randint(1, 100))


res = []
for i in range(0, 100):
	res.append(pqTest.pop())

print(res)










