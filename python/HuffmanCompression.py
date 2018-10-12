import heapq
import collections

class HuffmanCompression
	class Trie:

		## if letter == "", then it's not a leaf

		def __init__(self, letter, count, left = None, right = None):
			
			self.letter = letter
			self.count = count
			self.left = left
			self.right = right

			self.encode = ""
			

		def __eq__(self, other):
			return self.count == other.count

		def __lt__(self, other):
			return self.count < other.count

		def __gt__(self, other):
			return self.count > other.count

		def isLeaf(self):
			return letter != ""

	def __init__(self, string):
		self.string = string
		self.root = None
		self.dict = {}
		self.bits = ''

	def buildTieTree(self):
		counter = collections.Counter(self.string)
		heap = []
		for letter, count in counter.items():
			heapq.heappush(heap, Trie(letter, count))

		while len(heap) > 1:
			a = heapq.heappop(heap)
			b = heapq.heappop(heap)
			heapq.heappush(heap, Trie("", a.count + b.count, a, b))

		node = heapq.heappop(heap)
		if node.isLeaf:
			self.root = Trie("", node.count, a, None)
		else:
			self.root = node

	def encode(self):
		queue = collections.deque()
		queue.append(self.root)
		while queue:
			node = queue.popleft()
			if node.isLeaf:
				self.dict[node.letter] = node.encode
				continue
			if node.left:
				node.left.encode = node.encode + "0"
				queue.append(node.left)
			if node.right:
				node.right.encode = node.encode + "1"
				queue.append(node.right)


	def compress(self):
		self.bits = ''
		for char in self.string:
			self.bits += self.dict[char]
		return self.bits

	def decompress(self):
		string = ''
		pointer = self.root
		for bit in self.bits:
			if bit == "0":
				pointer = pointer.left
			else:
				pointer = pointer.right
			if pointer.isLeaf:
				string += pointer.char
				pointer = self.root
		return string


