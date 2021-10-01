'''
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only
one call to isSubstring (e.g. "waterbottle" is a rotation of "erbottlewat")
'''

def is_substring(s1: str, s2: str) -> bool:
    return s2 in s1


'''
0. check if s1 and s2 have equal length
1. find beginning of s1 in s2
2. check if 0:beg_s2 is a substring of s1
O(n)=n O(1) space
'''
def is_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
        else:
            i = max(0, i-1)
        j += 1

    return is_substring(s1, s2[:-i])


def is_rotation_simple(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return is_substring(s1+s1, s2)


if __name__ == '__main__':
    s1 = 'waterbottle'
    s2 = 'erbottlewat'

    assert is_rotation(s2, s1)
    assert is_rotation_simple(s2, s1)

    s1 = 'waterbwttle'
    s2 = 'erbwttlewat'

    assert is_rotation(s2, s1)
    assert is_rotation_simple(s2, s1)

    s1 = 'water'
    s2 = 'ertaw'

    assert not is_rotation(s2, s1)
    assert not is_rotation_simple(s2, s1)

