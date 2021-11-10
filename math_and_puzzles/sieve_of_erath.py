from math import sqrt


def mark_multiples(x: int, flags: list[bool]) -> None:
    for i in range(x*x, len(flags), x):
        flags[i] = False


def get_next_candidate(x: int, flags: list[bool]) -> int:
    for i in range(x+1, len(flags)):
        if flags[i]:
            return i
    return x+1


def get_primes(n: int) -> list[int]:
    flags = [True for _ in range(n+1)]
    flags[0] = False
    flags[1] = False

    x = 2
    while x <= int(sqrt(n)):
        mark_multiples(x, flags)
        x = get_next_candidate(x, flags)

    return [i for i, f in enumerate(flags) if f]

if __name__ == '__main__':
    primes = get_primes(100)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
