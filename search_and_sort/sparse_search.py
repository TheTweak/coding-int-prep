'''
Given a sorted array of strings that is interspersed with empty string, write a method to find a location of a given string.
Example:

ball, ["at", "", "", "", "ball", "", "", "", "cat"]
output: 4
'''


def skip_empty(n: list[str], start: int, end: int) -> int:
	'''
	Finds first non empty element on interval [start, end], going from end->lower
	and returns its index. Returns -1 if no non empty elemnts found.
	'''
	if start > end:
		return -1



def search(n: list[str], el: str, l: int, h: int) -> int:
	if l > h:
		return -1

	m = (l + h) // 2
	x = n[m]
	if x == '':
		m = skip_empty(n, l, m - 1)