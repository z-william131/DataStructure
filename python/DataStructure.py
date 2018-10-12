############### Stack ###############

stack = []
size = len(stack)
stack.append(1)
stack.append(2)
stack.pop() # return 2


############### Queue ###############

queue = []
size = len(queue)
queue.append(1)
queue.append(2)
queue.pop(0) # return 1

############### Deque ###############

import collections
dq = collections.deque()
dq.appendleft(1)
dq.append(2)
dq.append(3)
assert dq[1] == 2
dq.popleft()
dq.pop()

############### Heap ###############

import heapq

pq = []
heapq.heappush(pq, 1)
heapq.heappop(pq)

############### String ###############

abc = "abc"
abc_list = list(abc)

## if not found, return -1
assert "apple".find("l") == 3 

## if sep == None: 
## words are separated by arbitrary strings of whitespace characters
split_lst = "Hello world!".split() 
join_lst = "_".join(abc_list)

############### Set ###############

s1 = set()
s1 = {1,2,3, 4}
s1.add("haha")
assert "haha" in s1
s1.remove("haha")

s2 = set([3,4,5])

s3 = s1.union(s2)
assert len(s3) == 5

s4 = s1.intersection(s2)
assert len(s4) == 2

s5 = s1.difference(s2)
assert len(s5) == 2

s6 = s1.symmetric_difference(s2)
assert len(s6) == 3

############### Dictionary ###############

dic = {}
dic["a"] = "1"
dic.pop("a")
keys = dic.keys()
for key, value in dic.items():
	pass

############### Tuple ###############

## just to remember it is immutable
tup = (1,2,3)

