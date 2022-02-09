'''
You are reading a stream if ints, implement data structures to calculate rank of X (number of elements <= X).
Operations:

track(x) - called for each element in the stream
rank(x) - count of elements <= x, not including x

Ex:

5, 1, 4, 4, 5, 9, 7, 13, 3

rank(1) = 0
rank(3) = 1 // 1
rank(4) = 3 // 1, 4, 3
'''

class IntRankDict:
  def __init__(self):
    self.stats = {}

  def track(self, x):
    exists = x in self.stats
    if exists:
      self.stats[x] += 1
    else:
      self.stats[x] = 1

    for k in self.stats:
      if k > x:
        self.stats[k] += 1
      elif not exists and k < x:
        self.stats[x] += 1

  def rank(self, x):
    if not x in self.stats:
      return 0

    return self.stats[x] - 1


class Node:
  def __init__(self, value):
    self.right = None
    self.left = None
    self.left_size = 0
    self.value = value

  def insert(self, value):
    if value <= self.value:
      self.left_size += 1
      if self.left:
        self.left.insert(value)
      else:
        self.left = Node(value)
    elif value > self.value:
      if self.right:
        self.right.insert(value)
      else:
        self.right = Node(value)
    
  def rank(self, value):
    if self.value == value:
      return self.left_size
    elif value < self.value:
      if self.left:
        return self.left.rank(value)
      else:
        return -1
    else:
      if self.right:
        return self.left_size + 1 + self.right.rank(value)
      else:
        return -1


class IntRankBTree:
  def __init__(self):
    self.root = None

  def track(self, x):
    if self.root:
      self.root.insert(x)
    else:
      self.root = Node(x)

  def rank(self, x):
    if self.root:
      r = self.root.rank(x)
      return r if r != -1 else 0
    return 0


if __name__ == '__main__':
  stream = [5, 1, 4, 4, 5, 9, 7, 13, 3]

  rank_dict = IntRankDict()
  rank_tree = IntRankBTree()
  for s in stream:
    rank_dict.track(s)
    rank_tree.track(s)

  print(rank_dict.rank(1))
  print(rank_dict.rank(3))
  print(rank_dict.rank(4))

  print(rank_tree.rank(1))
  print(rank_tree.rank(3))
  print(rank_tree.rank(4))
  
