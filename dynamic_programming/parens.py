'''
Implement an algorithm to print all possible valid combinations of n open and closed parentheses.
Example:

n = 3

((()))
()()()
(())()
()(())
(()())
'''


'''

paren(3)
    paren_('(', 1, 0, [], 3)
        paren_('((', 2, 0, [], 3)
            paren_('(((', 3, 0, [], 3)
                paren_('((()', 3, 1, [], 3)
                    paren_('((())', 3, 2, [])
                        paren('((()))', 3, 3, ['((()))'])
            paren_('(()', 2, 1)
                paren('(()(', 3, 1)
                    paren('(()()', 3, 2)
                        paren('(()())')

'''


def paren_(p: list[str], nop: int, ncl: int, result: list[str], n):
    if nop == ncl == n:
        result.append(''.join(p))
        return

    if nop < n:
        p.append('(')
        paren_(p, nop + 1, ncl, result, n)
        p.pop()

    if ncl < nop:
        p.append(')')
        paren_(p, nop, ncl + 1, result, n)
        p.pop()
    

def paren(n: int) -> list[str]:
    result = []
    paren_(['('], 1, 0, result, n)
    return result

    
if __name__ == '__main__':
    ps = paren(4)
    for p in ps:
        print(p)    
