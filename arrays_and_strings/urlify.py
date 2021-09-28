import fileinput


def count_tail(s: list) -> int:
    cnt = 0
    for i in range(len(s)-1, 0, -1):
        if s[i] == ' ':
            cnt += 1
        else:
            break
    return cnt


if __name__ == '__main__':
    in_str = list(next(fileinput.input()))[:-1]
    print(in_str)
    ws_cnt = count_tail(in_str)
    print(ws_cnt)
    len_wo_ws = len(in_str) - ws_cnt
    len_full = len(in_str) - 1
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

