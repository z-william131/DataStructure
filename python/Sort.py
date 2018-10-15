
import collections
import random

# Bubble Sort:
# Summary: Compare adjusted node and move the larger one to latter
# Time Complexity: n^2
# Space Complexity: 1

def bubbleSort(lst):
	for i in range(len(lst)):
		for j in range(1, len(lst) - i):
			if lst[j-1] > lst[j]:
				lst[j-1], lst[j] = lst[j], lst[j-1]
	return lst


# Selection Sort:
# Summary: Find min in lst[i:] to get the i-th number
# Time Complexity: n^2
# Space Complexity: 1

def selectionSort(lst):
	for i in range(len(lst)):
		min_index = i
		for j in range(i+1, len(lst)):
			if lst[j] < lst[min_index]:
				min_index = j
		lst[i], lst[min_index] = lst[min_index], lst[i]
	return lst


# Insertion Sort:
# Summary: Insert the i-th number to the lst[:i] sorted list
# Time Complexity: n^2
# Space Complexity: 1

def insertionSort(lst):
	for i in range(1, len(lst)):
		for j in range(i-1, -1, -1):
			if lst[j] > lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]
	return lst


# Merge Sort:
# Summary: Merge sorted list with length i to i * 2
# Time Complexity: n * log n
# Space Complexity: n

def mergeSort(lst):
	dq = collections.deque([[i] for i in lst]) 
	while len(dq) > 1:
		lst1 = dq.popleft()
		p1 = 0

		lst2 = dq.popleft()
		p2 = 0

		combine = []
		while p1 < len(lst1) or p2 < len(lst2):
			if p1 == len(lst1):
				combine.append(lst2[p2])
				p2 += 1
			elif p2 == len(lst2):
				combine.append(lst1[p1])
				p1 += 1
			elif lst1[p1] < lst2[p2]:
				combine.append(lst1[p1])
				p1 += 1
			else:
				combine.append(lst2[p2])
				p2 += 1
		dq.append(combine)
	return dq[0]


# Quick Sort:
# Summary: Randomly select a item and check the ones that are smaller/bigger than it.
# Time Complexity: n * log n
# Space Complexity: n

def quickSort(lst):
	dq = collections.deque()
	dq.append((0, len(lst)))
	while dq:
		start, end = dq.pop()
		if start +1 >= end:
			continue
		idx = random.randint(start, end)
		small = []
		equal = []
		large = []
		for i in range(start, end):
			if lst[i] < lst[idx]:
				small.append(lst[i])
			elif lst[i] == lst[idx]:
				equal.append(lst[i])
			else:
				large.append(lst[i])
		lst = lst[:start] + small + equal + large + lst[end:]
		dq.append((start, start+len(small) + 1))
		dq.append((start + len(small) + len(equal), end))
	return lst


# Radix Sort:
# Summary: Sort by index
# Time Complexity: n^digit
# Space Complexity: n

def radixSort(lst):
	base = 1
	digitBox = [[] for _ in range(10)]
	for i in lst:
		digitBox[i // base % 10].append(i)

	temp = [[] for _ in range(10)]
	while (base < max(lst)):
		base *= 10
		for digitLst in digitBox:
			for num in digitLst:
				temp[num // base % 10].append(num)
		digitBox = temp
		temp = [[] for _ in range(10)]
	return digitBox[0]




