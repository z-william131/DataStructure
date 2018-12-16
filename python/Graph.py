from collections import defaultdict, deque

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Vertex:
	def __init__(self, index, weight = 0):
		self.index = index
		self.neighbor

		self.weight = weight
		self.pre = None
		self.post = None
		self.visited = False


class Graph:
	def __init__(self):
		self.graph = defaultdict(set)
		self.edges = defaultdict(int)

	def addEdge(self, u, v, weight = 1):
		self.graph[u].add(v)
		self.edges[(u, v)] = weight

	def getWeight(self, u, v):
		return self.edges[(u, v)]

	## One typical DFS problem: Topological Sort
	def topologicalSort(self):
		res = []
		def helper(index):
			visited[index] = True
			for subIndex in self.graph[index]:
				if not visited[subIndex]:
					helper(index)
			res.append(index)

		visited = [False] * len(self.graph)
		for i in range(len(self.graph)):
			if visited[i]:
				continue
			helper(i)

		return res[::-1]

	## One typical BFS problem: Shortest Path
	## Runtime: |V|log|V| + |E|
	## Space: |V|
	def dijkstra(self, start):
		V = len(self.graph)

		dis = [V] * V
		dis[start] = 0

		queue = [(V, i) for i in range(V)]
		queue.remove((V, start))
		heappush(queue, (0, start))

		while queue:
			nodeDis, node = heappop(queue)
			for i in self.graph[node]:
				if dis[i] > dis[node] + self.getWeight(node, i):
					queue.remove((dis[i], i))
					dis[i] = dis[node] + self.getWeight(node, i)
					heappush(queue, (dis[i], i))

		return dis

	## Another way to solve shortest path problem
	## Accept negative edges and can detect negative circle
	## Runtime: |V||E|
	## Space: |V|
	def bellmanford(self, start):
		V = len(self.graph)
		dis = [V] * V
		dis[start] = 0

		for i in range(V-1):
			for u, v in self.edges:
				dis[v] = min(dis[v], dis[u] + self.getWeight(u, v))

		for u, v in self.edges:
			if dis[v] > dis[u] + self.getWeight(u, v):
				print("detect negative circle")

		return dis

	## MST
	## Runtime: |E|log|E|
	## Space: |V|
	def kruskal(self):
		edge_list = []
		for edge in self.edges:
			edge_list.append((self.edges[edge], edge))
		edge_list.sort()

		## Makeset()
		V = len(self.graph)
		parent = [i for i in range(V)]
		rank = [0] * V

		def find(x):
			if x != parent[x]:
				parent[x] = find(parent[x])
			return parent[x]

		def union(x, y):
			x = find(x)
			y = find(y)
			if x == y:
				return
			if rank[x] > rank[y]:
				parent[y] = x
			else:
				parent[x] = y
				if rank[x] == rank[y]:
					rank[y] = rank[y] + 1


		result = []
		for cur_weight, cur_edge in edge_list:
			u, v = cur_edge
			if find(u) != find(v):
				result.append(cur_edge)
				union(u, v)
		return result















