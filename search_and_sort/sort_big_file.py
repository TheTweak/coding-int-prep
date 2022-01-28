import tempfile
import sys
import os


BUFFER_SIZE_LINES = 3
TMP_SMALLER_FILENAME = 'tmp_smaller.txt'
TMP_LARGER_FILENAME = 'tmp_larger.txt'
DEBUG = False


def write_from_buffer(buffer: list[str], file) -> int:
    lines_written = 0
    for b in buffer:
        file.write(b)
        lines_written += 1
    buffer.clear()
    return lines_written


def read_to_buffer(buffer: list[str], file) -> bool:
    while True:
        line = file.readline()
        if not line:
            return bool(len(buffer))
        buffer.append(line)
        if len(buffer) == BUFFER_SIZE_LINES:
            return True


def skip_lines(file, n: int) -> None:
    lc = 0
    while lc < n:
        file.readline()
        lc += 1


def print_file(file) -> None:
    if not DEBUG:
        return
    file.seek(0, 0)
    print()
    for l in file.readlines():
        print(l, end='')
    print()
    file.seek(0, 0)


def print_debug(str):
    if DEBUG:
        print(str)
    

def __sort__(file_name: str, l: int, h: int) -> None:
    if l > h:
        return

    f = open(file_name, 'r+')
    print_file(f)

    f_larger = open(TMP_LARGER_FILENAME, 'w')
    f_smaller = open(TMP_SMALLER_FILENAME, 'w')
    
    mid = (l + h) // 2
    skip_lines(f, mid)
    mid_line = f.readline()
    mid_line_debug = mid_line.replace('\n', '')
    print_debug(f'mid_line is {mid_line_debug} mid={mid} l={l} h={h}')
    
    buffer_smaller = []
    buffer_larger = []
    
    f.seek(0, 0)
    skip_lines(f, l)
    l_pos = f.tell()
    line_count = l
    while line_count <= h:            
        line = f.readline()

        if line_count == mid:
            line_count += 1
            continue

        line_count += 1
        if not line:
            break

        if line > mid_line:
            buffer_larger.append(line)
        else:
            buffer_smaller.append(line)

        if len(buffer_larger) == BUFFER_SIZE_LINES:
            write_from_buffer(buffer_larger, f_larger)

        if len(buffer_smaller) == BUFFER_SIZE_LINES:
            write_from_buffer(buffer_smaller, f_smaller)

    write_from_buffer(buffer_larger, f_larger)
    write_from_buffer(buffer_smaller, f_smaller)

    f.seek(l_pos, 0)

    f_smaller.close()
    f_smaller = open(TMP_SMALLER_FILENAME, 'r')
    print_debug('smaller:')
    print_file(f_smaller)
    
    pivot_pos = l
    while read_to_buffer(buffer_smaller, f_smaller):
        pivot_pos += write_from_buffer(buffer_smaller, f)

    f.write(mid_line)

    f_larger.close()
    f_larger = open(TMP_LARGER_FILENAME, 'r')
    print_debug('larger:')
    print_file(f_larger)
    
    while read_to_buffer(buffer_larger, f_larger):
        write_from_buffer(buffer_larger, f)

    f_larger.close()
    f_smaller.close()
    f.close()

    print_debug(f'pivot pos = {pivot_pos}')
    f_debug = open(file_name, 'r')
    print_file(f_debug)
    f_debug.close()
    print_debug('--------------')


    __sort__(file_name, l, pivot_pos - 1)
    __sort__(file_name, pivot_pos + 1, h)


def sort(file_name: str) -> None:
    with open(file_name) as f:
        total_lines = 0
        while f.readline():
            total_lines += 1
        __sort__(file_name, 0, total_lines - 1)
    os.remove(TMP_LARGER_FILENAME)
    os.remove(TMP_SMALLER_FILENAME)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <file_name>')
        sys.exit(1)
    sort(sys.argv[1])

