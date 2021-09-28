import fileinput

if __name__ == '__main__':
    in_str = next(fileinput.input())
    chars = 0
    is_unique = True
    for i in range(len(in_str)):
        j = 1 << ord(in_str[i])
        if chars & j:
            is_unique = False
            break
        chars |= j
    print(str(is_unique))
