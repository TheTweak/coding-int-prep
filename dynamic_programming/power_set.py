'''
Write a method to return all subsets of a set.

s={1 2 3 4}
s1={1}
s2={2}
s3={3}
s4={4}

s5={1 2}
s6={1 3}
s7={1 4}
s8={2 3}
s9={2 4}
s10={3 4}

{1 2 3}
{1 2 4}
{1 3 4}
{2 3 4}
'''


def subsets(s: list[set], el) -> list[set]:
    result = [set([el])]
    for x in s:
        x_ = set(x)
        x_.add(el)
        result.append(x_)
    return result


def power_set2_(result: list[set], el) -> None:
    new_subsets = subsets(result, el)
    result.extend(new_subsets)


def power_set2(orig: set) -> list[set]:
    result = []
    for el in orig:
        power_set2_(result, el)
    return result[:-1]


if __name__ == '__main__':
    orig = set([1, 2, 3, 4, 5, 6])
    powerset = power_set2(orig)
    for s in powerset:
        print(s)
