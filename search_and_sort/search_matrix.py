'''
Implement function to search in a matrix, where all columns and rows are sorted
in ascending order.
'''

def search_diag(l: int, h: int, m, x) -> int:
  '''
  works for square matrices only!
  binary search for x along main diagonal. returns diagonal  
  '''
  if l == h:
    return l

  mid = (l + h) // 2

  if x > m[mid][mid]:
    return search_diag(mid + 1, h, m, x)
  elif x < m[mid][mid]:
    return search_diag(l, mid - 1, m, x)
  else:
    return mid


def bin_search(l: int, h: int, arr, x) -> int:
  if l > h:
    return -1

  mid = (l + h) // 2
  if arr[mid] == x:
    return mid
  elif arr[mid] > x:
    return bin_search(l, mid - 1, arr, x)
  else:
    return bin_search(mid + 1, h, arr, x)


def search(m, x) -> (int, int):
  diag = search_diag(0, len(m) - 1, m, x)

  row = m[diag]
  col = []
  for r in range(len(m)):
    col.append(m[r][diag])
  c = bin_search(0, len(m) - 1, row, x)
  r = bin_search(0, len(m) - 1, col, x)
  return r if r != -1 else diag, c if c != -1 else diag


if __name__ == '__main__':
  size = 100
  matrix = [[0 for _ in range(size//10)] for _ in range(size//10)]
  i = 0
  for r in range(size//10):
    for c in range(size//10):
      matrix[r][c] = i
      i += 1
  
  r, c = search(matrix, 31)
  assert (r, c) == (3, 1)
