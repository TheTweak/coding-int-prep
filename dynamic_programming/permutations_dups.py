'''
Write a method to compute all permutations of a string whose characters are
not necessarily unique. The list of permutations should not have duplicates.
'''

class Permutations:
    def __init__(self, string):
        self.letters = list(string)
        self.visited = set()

    def perm_(self, letters: list[str], result, permutations):
        if not len(letters):
            permutation = ''.join(result[0])
            if not permutation in self.visited:
                permutations.append(permutation)
                self.visited.add(permutation)
            return

        for l in letters:
            result[0].append(l)
            letters_copy = letters.copy()
            letters_copy.remove(l)
            self.perm_(letters_copy, result, permutations)
            result[0].pop()
                    
    def permutations(self) -> list[str]:
        result = []
        self.perm_(self.letters, [[]], result)
        return result
            

if __name__ == '__main__':
    ps = Permutations('abab').permutations()
    for p in ps:
        print(p) 

    print()
