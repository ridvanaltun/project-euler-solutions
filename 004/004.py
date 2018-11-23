def ispol(num):
	if str(num)[::-1] == str(num):
		return True
	else:
		return False

n =0

def find_tree_digit_largest_polidrome():
	global n
	for a in range(999, 100, -1):
		for b in range(a, 100, -1):
			if a*b > n:
				if ispol(a*b):
					n = a*b


find_tree_digit_largest_polidrome()
print(n)