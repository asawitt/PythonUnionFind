class UnionFind:
	def __init__(self):
		self.parent = {}
		self.rank = {}

	def make_set(self,x):
		self.parent.setdefault(x,x)
		self.rank.setdefault(x,0)

	def find(self,x):
		to_reattach = set()
		if x not in self.parent:
			return None
		while self.parent[x] != x:
			to_reattach.add(x)
			x = self.parent[x]
		for leaf in to_reattach:
			self.parent[leaf] = x
		return x

	def union(self,x,y):
		x_root = self.find(x)
		y_root = self.find(y)
		if x_root is None or y_root is None or x_root == y_root:
			return
		x_rank = self.rank[x_root]
		y_rank = self.rank[y_root]

		if x_rank < y_rank:
			self.parent[x_root] = y_root
		elif y_rank < x_rank:
			self.parent[y_root] = x_root
		else:
			self.parent[y_root] = x_root
			self.rank[x_root] += 1
