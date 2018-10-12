import collections

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Edge:
	def __init__(self, first, second, weight):
		self.first = first
		self.second = second
		self.weight = weight

class Vertice:
	def __init__(self, val):
		self.val = val
		self.neighbors = []


## Input: vertice(a list of int), edge(a list of tuple: in, out), directed(boolean)

## Space: |V|^2
## Time for checking (u,v) existance: 1
## Time for checking nodes connected with n: |V|
class MatrixGraph:
	def __init__(self, vertice, edge, directed):
		self.matrix = [[0 for _ in range(len(vertice))] for _ in range(len(vertice))]
		for e in edge:
			if directed:
				self.matrix[edge[0]][edge[1]] = 1
			else:
				self.matrix[edge[0]][edge[1]] = 1
				self.matrix[edge[1]][edge[0]] = 1


## Space: |E|
## Time for checking (u,v) existance: degree of u
## Time for checking nodes connected with n: degree of u
class ListGraph:
	def __init__(self, vertice, edge, directed):
		self.graph = collections.defaultdict(set)
		for e in edge:
			if directed:
				self.graph[edge[0]].add(edge[1])
			else:
				self.graph[edge[0]].add(edge[1])
				self.graph[edge[1]].add(edge[0])


