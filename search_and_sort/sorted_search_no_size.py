'''
You are given an array like data structure Listy which lacks a size method. It does
have elementAt(i) method that returns the element at index i in O(1) time. If i is
beyond the bounds of the data, it returns -1.
Given a Listy, that contains sorted, positive integers, find index of element x.
If x occurs multiple times, you may return any index.
'''

class Listy:
	def __init__(self, data: list[int]):
		self.__data__ = data

	def element_at(self, i: int) -> int:
		if i >= len(self.__data__) or i < 0:
			return -1

		return self.__data__[i]


def search(listy: Listy, el: int, l: int, h: int) -> int:
	if h < l:
		return -1

	m = (l + h) // 2
	x = listy.element_at(m)
	if x == -1 or el < x:
		return search(listy, el, l, m - 1)
	elif x == el:
		return m
	elif x < el:
		return search(listy, el, m + 1, 2 * h)


if __name__ == '__main__':
	l = Listy([1, 2, 3, 6])
	i = search(l, 6, 0, 2)
	print(f'i={i}')
	assert i == 3

	i = search(l, 10, 0, 2)
	print(f'i={i}')
	assert i == -1

	i = search(l, 1, 0, 2)
	print(f'i={i}')
	assert i == 0

	l = Listy([1, 1, 1, 1])
	i = search(l, 6, 0, 2)
	print(f'i={i}')
	assert i == -1

	i = search(l, 1, 0, 2)
	print(f'i={i}')	
