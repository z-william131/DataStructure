string = "akkhdafkjadf"
counter = collections.Counter(string)

import random
for x in range(10):
	print random.randint(-3, x)



def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)
