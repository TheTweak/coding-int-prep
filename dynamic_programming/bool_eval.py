'''
Given a bool expression, consisting of the symbols:
- 1
- 0
- &
- |
- ^ (XOR)

and a desired boolean value, implement a function to
count the number of ways parenthesizing the expression
to get the desired output.

Ex:

countEval("1^0|0|1", false) -> 2
countEval("0&0&0&1^1|0", true) -> 10

Recursive expression:

countEval("1^0|0|1", f) = countEval("(1)^(0|0|1)", f) + 
countEval("(1^0)|(0|1)", f) + ...

then:

countEval("(1)^(0|0|1)", f) = countEval(left=1, f) * countEval(right=0|0|1, f)

'''

def count_eval(expr: str, expected: bool) -> int:
    if not len(expr):
        return 0

    if len(expr) == 1:
        if (expected and expr == '1') or (not expected and expr == '0'):
            return 1
        return 0

    result = 0
    for i in range(1, len(expr), 2):
        left_expr = expr[:i]
        right_expr = expr[i+1:]

        left_true = count_eval(left_expr, True)
        left_false = count_eval(left_expr, False)
        right_true = count_eval(right_expr, True)
        right_false = count_eval(right_expr, False)

        op = expr[i]
        if op == '^':
            if expected:
                result += left_true*right_false + left_false*right_true
            else:
                result += left_true*right_true + left_false*right_false
        elif op == '|':
            if expected:
                result += left_true*right_true + left_true*right_false + \
                    left_false*right_true
            else:
                result += left_false*right_false
        elif op == '&':
            if expected:
                result += left_true*right_true
            else:
                result += left_false*right_true + left_true*right_false + \
                    left_false*right_false

    return result


if __name__ == '__main__':
    solution = count_eval('1^0|0|1', False)
    assert solution == 2
    assert count_eval('0&0&0&1^1|0', True) == 10
