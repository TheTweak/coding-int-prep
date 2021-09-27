import fileinput

if __name__ == '__main__':
    finput = fileinput.input()
    a = next(finput)
    b = next(finput)
    distance = 1
    if abs(len(a)-len(b)) > distance:
        print(False)

    i = 0
    j = 0
    result = True
    while i < len(a) and j < len(b):
        if a[i] != b[j]:
            if distance <= 0:
                result = False
                break
            distance -= 1
            if len(a) > len(b):
                i += 1
                continue
            elif len(a) < len(b):
                j += 1
                continue
        i += 1
        j += 1

    print(result)
