'''
You are given an array of ints. Peak is an element with adj. elements less than this element.
Valley is an element with adj. element >= than this element. Re arrange the elements in the array
in such a way that it would consist of alternating peaks and valleys.

Ex: [5, 3, 1, 2, 3]

[5 3 3 2 1]
[5 1 3 2 3]
out: [5, 1, 3, 2, 3]
'''

def peaks_and_valleys(a: list[int]) -> list[int]:
  result = [0 for _ in range(len(a))]
  a = sorted(a)
  l = 0
  h = len(a) - 1
  i = 0
  while l < h:
    result[i] = a[h]
    i += 1
    result[i] = a[l]
    i += 1
    l += 1
    h -= 1
  result[i] = a[h]
  return result


def peaks_and_valleys_in_place(a: list[int]) -> None:
  a = sorted(a, reverse=True)
  l = 1 # 0th element is in its final place already
  h = len(a) - 1
  while l < h:
    tmp = a[l]
    a[l] = a[h]
    a[h] = tmp
    l += 2
    h -= 1
  return a


if __name__ == '__main__':
  a = [5, 3, 1, 2, 3]

  b = peaks_and_valleys(a)
  print(b)

  a = peaks_and_valleys_in_place(a)
  print(a)