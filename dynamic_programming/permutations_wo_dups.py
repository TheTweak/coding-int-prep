'''
Write a method to compute all permutations of a string of unique characters.

s = a

result = [a]

s = ab

result = [ab, ba]

s = abc

result = [abc, bac, cab, cba, acb, bca]

brute force:

def perm(s, result):
    if not len(s):
        return
    c = pick a4nd remove a letter from s
    result.append(c)
    perm(s, result)
'''

'''

perm_([a b c], [], [])
    perm_([b c], [a], [])
        perm_([c], [a, b], [])
            perm_([], [a b c], ['abc'])
        perm_([b], [a, c], ['abc'])
            perm_([], [a, c, b], [abc, acb])
    perm_([a c], [b], [abc, acb])
        perm_([c], [b a], [abc, acb])
            perm_([], [b a c], [abc, acb, bac])

'''

class PermutationsWithoutRepetitions:
    def __init__(self, string):
        self.letters = list(string)

    def perm_(self, letters: list[str], result, permutations):
        if not len(letters):
            permutation = ''.join(result[0])
            permutations.append(permutation)        
            return

        for l in letters:
            result[0].append(l)
            letters_copy = [x for x in letters]
            letters_copy.remove(l)
            self.perm_(letters_copy, result, permutations)
            result[0].pop()
                    
    def permutations(self) -> list[str]:
        result = []
        self.perm_(self.letters, [[]], result)
        return result

class PermutationsWithRepetitions:
    def __init__(self, string):
        self.letters = list(string)

    def perm_(self, result, permutations, size):
        if not size:
            permutation = ''.join(result[0])
            permutations.append(permutation)        
            return

        for l in self.letters:
            result[0].append(l)
            self.perm_(result, permutations, size - 1)
            result[0].pop()
                    
    def permutations(self) -> list[str]:
        result = []
        self.perm_([[]], result, len(self.letters))
        return result
            

if __name__ == '__main__':
    ps = PermutationsWithoutRepetitions('abc').permutations()
    for p in ps:
        print(p) 

    print()

    psr = PermutationsWithRepetitions('abcd').permutations()
    print(len(psr))
    for p in psr:
        print(p) 
