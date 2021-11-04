'''
You have an integer and you can flip exactly one bit from a 0 to 1. Write code to
find the length of the longest sequence of 1s you could create.

Ex:

in: 1775 (or 11011101111)
out: 8

Brute force:

- convert to bits
- iterate over bits
- count 1s until reach a 0
- flip this 0, and remember position
- continue counting 1s until reach a 0
- update max_length of 1s, reset current 1s count
- start over from flip position

O(N)=N
'''


def flip_2_win(x: int) -> int:
    bits = bin(x).split('b')[1]
    longest = 0
    flip_pos = None
    ones_count = 0
    i = 0
    while True:
        if i >= len(bits):
            break

        if bits[i] == '1':
            ones_count += 1
        else:
            if flip_pos is None:
                flip_pos = i
                ones_count += 1
            else:
                i = flip_pos
                flip_pos = None
                ones_count = 0
        longest = max(longest, ones_count)
        i += 1
    print(longest)
    return longest


if __name__ == '__main__':
    assert flip_2_win(1775) == 8
    assert flip_2_win(1234) == 4
