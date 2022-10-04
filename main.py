"""Solves and prints the solution to Feynman's long division problem"""


from itertools import product


def cond_test(num, A, state):
	"""Tests whether the inputted number matches a particular state.
	A state is a string of 0s and 1s where 0 is a dot and 1 is an A"""
	return ''.join(str(int(i == A)) for i in str(num)) == state


def solve():
	"""Solves Feynman's long division problem. Returns (divisor, quotient)"""
	for divisor in range(100, 1_000):
		
		# Test for a valid divisor, and simultaneously initialise A
		if not cond_test(divisor, A := str(divisor)[1], "010"):
			continue
		
		# Let the quotient be xyAz, and then for each valid x
		for x in (digits := set(range(10)) - {int(A)}):
			
			# Test quotient first digit * divisor = line 2 (and initialise)
			if not cond_test(l2 := x * divisor * 1_000, A, "0011000"):
				continue
			
			# For remaining possibilities of quotient
			for y, z in product(digits, digits): # Cartesian product
				dividend = divisor * (quotient := int(f"{x}{y}{A}{z}"))
				
				# Set the numbers on lines four and six respectively
				l4 = y * divisor * 100
				l6 = int(A) * divisor * 10

				# Test all lines for validity
				if all(( # d represents the remainder throughout process
					cond_test(d := dividend, A, "0000100"), # Line 1
					cond_test(d := d - l2, A, "000100"), 	# Line 3
					cond_test(l4, A, "00100"), 		# Line 4
					cond_test(d := d - l4, A, "00000"), 	# Line 5
					cond_test(l6, A, "01000"), 		# Line 6
					cond_test(d := d - l6, A, "0000") 	# Line 7
				)):
					return (divisor, quotient)


if __name__ == '__main__':
	d, q = solve()
	print(f"divisor={d}, quotient={q}") # Prints: divisor=484, quotient=7289
