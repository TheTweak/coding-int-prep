import fileinput

if __name__ == '__main__':
    in_str = next(fileinput.input())
    original = str(in_str)
    compressed = []
    cnt = 0
    pc = original[0]

    for i in range(len(original)):
        c = original[i]
        if c != pc:
            compressed.append(pc)
            compressed.append(str(cnt))
            cnt = 1
        else:
            cnt += 1
        pc = c

    if len(compressed) > len(original):
        print(original)
    else:
        print(''.join(compressed))
