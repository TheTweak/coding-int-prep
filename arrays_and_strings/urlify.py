import fileinput


def count_tail(s: list) -> int:
    cnt = 0
    for i in range(len(s)-1, 0, -1):
        if s[i] == ' ':
            cnt += 1
        else:
            break
    return cnt


def count_ws(s: list) -> int:
    cnt = 0
    for c in s:
        if c == ' ':
            cnt += 1
    return cnt


if __name__ == '__main__':
    in_str = list(next(fileinput.input()))[:-1]
    len_wo_ws = len(in_str)

    # count whitespaces
    ws_cnt = count_ws(in_str)

    # appen empty chars to acquire enough space for
    # %20
    for i in range(ws_cnt):
        in_str.append(' ')
        in_str.append(' ')
    len_full = len(in_str)-1

    # moving backwards through original string
    # substitute ws with %20
    # move everything else to fill gaps in new string
    for i in range(len_wo_ws-1, 0, -1):
        c = in_str[i]
        if c == ' ':
            in_str[len_full] = '0'
            in_str[len_full-1] = '2'
            in_str[len_full-2] = '%'
            len_full -= 3
        else:
            in_str[len_full] = in_str[i]
            len_full -= 1
    print(''.join(in_str))

