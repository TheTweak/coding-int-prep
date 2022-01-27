import tempfile
import sys

BUFFER_SIZE_LINES = 3

def write_from_buffer(buffer: list[str], file) -> None:
    for b in buffer:
        file.write(b)
    buffer.clear()


def read_to_buffer(buffer: list[str], file) -> bool:
    while True:
        line = file.readline()
        if not line:
            return bool(len(buffer))
        buffer.append(line)
        if len(buffer) == BUFFER_SIZE_LINES:
            return True


def __sort__(file_name: str, l: int, h: int) -> None:
    if l >= h:
        return

    with open(file_name, 'r') as f:
        f_larger = open('tmp_larger.txt', 'w')
        f_smaller = open('tmp_smaller.txt', 'w')
        mid = (l + h) // 2
        line_count = 0
        mid_line = None
        while True:
            mid_line = f.readline()
            if line_count == mid:
                break
            line_count += 1

        print(f'mid_line is {mid_line}')
        buffer_smaller = []
        buffer_larger = []
        f.seek(0, 0)
        line_count = 0
        while True:
            line = f.readline()
            if not line or line_count > h:
                break

            if line > mid_line:
                buffer_larger.append(line)
            else:
                buffer_smaller.append(line)

            if len(buffer_larger) == BUFFER_SIZE_LINES:
                write_from_buffer(buffer_larger, f_larger)

            if len(buffer_smaller) == BUFFER_SIZE_LINES:
                write_from_buffer(buffer_smaller, f_smaller)

            line_count += 1

        write_from_buffer(buffer_larger, f_larger)
        write_from_buffer(buffer_smaller, f_smaller)

        f_write = open(file_name, 'r+')
        line_count = 0
        while line_count < l:
            f_write.readline()
            line_count += 1

        f_smaller.close()
        f_smaller = open('tmp_smaller.txt', 'r')
        while read_to_buffer(buffer_smaller, f_smaller):
            write_from_buffer(buffer_smaller, f_write)

        f_write.write(mid_line)

        f_larger.close()
        f_larger = open('tmp_larger.txt', 'r')
        while read_to_buffer(buffer_larger, f_larger):
            write_from_buffer(buffer_larger, f_write)

        f_larger.close()
        f_smaller.close()

        f_write.seek(0, 0)
        print(f_write.readlines())
        f_write.close()

        __sort__(file_name, l, mid - 1)
        __sort__(file_name, mid + 1, h)


def sort(file_name: str) -> None:
    with open(file_name) as f:
        total_lines = 0
        while f.readline():
            total_lines += 1
        __sort__(file_name, 0, total_lines)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <file_name>')
        sys.exit(1)
    sort(sys.argv[1])

