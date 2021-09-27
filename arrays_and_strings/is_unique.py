import fileinput

if __name__ == '__main__':
    in_str = next(fileinput.input())
    chars = [0 for _ in range(256)]
    is_unique = True
    for i in range(len(in_str)):
        j = ord(in_str[i])
        if chars[j]:
            is_unique = False
            break
        chars[j] = 1
    print(str(is_unique))
