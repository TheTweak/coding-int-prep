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


def power_set_combin(orig: set) -> list[set]:
    '''
    If we represent each possible subset of orig set as a binary
    number, where 1 - means element of orig set goes into subset,
    and 0 - does not go into the subset, then we can just iterate
    from 0 to integer with bits of size=size(orig) and all 1s,
    convert each i to binary representation, and create a subset using it.
    '''
    orig = list(orig)
    result = []
    n = 1 << len(orig)
    for i in range(n):
        subset = set()
        bin_repr = i
        j = 0
        while bin_repr:
            if bin_repr & 1:
                subset.add(orig[j])
            bin_repr >>= 1
            j += 1
        result.append(subset)
    return result


if __name__ == '__main__':
    orig = set([1, 2, 3, 4])
    powerset = power_set_combin(orig)
    print(len(powerset))
    for s in powerset:
        print(s)
