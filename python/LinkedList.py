class Node(object):
	def __init__(self, val, prev, post, head = False, tail = False):
		self.val = val
		self.prev = prev
		self.next = next
		self.head = head
		self.tail = tail

class DLL(object):
	

	def __init__(self):
		self.head = Node(0, None, None, head = True)
		self.tail = Node(0, None, None, tail = True)
		self.head.next = self.tail
		self.tail.prev = self.head
		self.size = 0

	def size(self):
		return self.size

	def get(self, idx):
		if idx < 0 or idx >= self.size:
			raise IndexError("Invalid index: " + idx)

		node = self.head.next
		for i in range(0, idx):
			node = node.next

		return node.val

	def remove(self, idx):
		if idx < 0 or idx >= self.size:
			raise IndexError("Invalid index: " + idx)

		node = self.head.next
		for i in range(0, idx):
			node = node.next

		node.prev.next = node.next
		node.next.prev = node.prev
		node.prev = None
		node.next = None
		self.size -= 1
		return node.val

	def insert(self, val, idx):
		if idx < 0 or idx > self.size:
			raise IndexError("Invalid index: " + idx)

		prevNode = self.head
		nextNode = self.head.next
		for i in range(0, idx):
			prevNode = prevNode.next

		newNode = Node(val, prevNode, nextNode)
		prevNode.next = newNode
		nextNode.prev = newNode
		self.size += 1
		return node.val

#### TODO: Common trick in DLL: Two pointers





