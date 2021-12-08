'''
Recursive multiply 2 positive integers without using * operator.
Allowed to use +, -, bit shift.
'''
 
def multiply_(a: int, b: int, result) -> None:
    if b == 1:
        result[0] += a
        return
    
    if b & 1:
        result[0] += a
        b -= 1
    else:
        a <<= 1
        b >>= 1
    
    multiply_(a, b, result)


def multiply(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    result = [0]
    multiply_(a, b, result)
    return result[0]


if __name__ == '__main__':
    assert multiply(2, 2) == 2*2
    assert multiply(2, 3) == 2*3
    assert multiply(1, 0) == 1*0
    a = multiply(512, 234)
    b = 512*234
    print(f'actual = {a}')
    print(f'expected = {b}')
    assert a == b