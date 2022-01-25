'''
Given a sorted array of strings that is interspersed with empty string, write a method to find a location of a given string.
Example:

ball, ["at", "", "", "", "ball", "", "", "", "cat"]
output: 4
'''


def skip_empty(n: list[str], l: int, h: int) -> int:
	'''
	Finds first non empty element on interval [l, h], going from h->l
	and returns its index. Returns -1 if no non empty elemnts found.
	'''
	if l > h:
		return -1

	m = (l + h) // 2
	if n[m] != '':
		return m
	else:
		return skip_empty(n, l, m - 1)


def get_new_middle(n: list[str], l: int, h: int) -> int:
	m = (l + h) // 2
	m_ = skip_empty(n, l, m - 1) # try left half
	if m_ != -1:
		return m_
	return skip_empty(n, m + 1, h) # try right half


def search(n: list[str], el: str, l: int, h: int) -> int:	
	if l >= h:
		return -1

	m = (l + h) // 2
	if n[m] == '':
		m = get_new_middle(n, l, h)
		if m == -1:
			return -1
	
	x = n[m]
	if x == el:
		return m
	elif x > el:
		return search(n, el, l, m - 1)
	else:
		return search(n, el, m + 1, h)


if __name__ == '__main__':
	n = ["at", "", "", "", "ball", "", "", "", "cat"]
	i = search(n, 'ball', 0, len(n))
	print(f'i={i}')
	assert i == 4

	i = search(n, 'at', 0, len(n))
	print(f'i={i}')
	assert i == 0

	i = search(n, 'dog', 0, len(n))
	print(f'i={i}')
	assert i == -1

	i = search(n, 'cat', 0, len(n))
	print(f'i={i}')
	assert i == 8