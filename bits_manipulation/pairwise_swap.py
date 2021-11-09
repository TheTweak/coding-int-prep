'''
Write a program to swap odd and even bits in an integer with as few instructions as possible, e.g.
bits 0 and 1 are swapped, bit 2 and bit 3 are swapped and so on.


xor:

1010
1001
----
0011

0123456789
1011010101
shift >>:
a=0101101010
put 1st bit back:

1101101010

now 1st=0
3rd=2nd
5th=4th

shift <<:
1011010101
0110101010
  0123456789
a=0101101010
b=0110101010

merge a&b, taking odd from a, and even from b

1011010101
0111101010

0111101010


'''

def pairwise_swap(a: int) -> int:
  odds = int('0'+bin(a >> 1).split('b')[1], 2)
  evens = a << 1
  odds_mask = int('010101010101', 2)
  evens_mask = int('101010101010', 2)
  result = (odds & odds_mask) | (evens & evens_mask)
  return result

if __name__ == '__main__':
  a = int('110101001101', 2)
  print(bin(a))
  print(bin(pairwise_swap(a)))
