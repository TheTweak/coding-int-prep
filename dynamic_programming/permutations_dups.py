'''
Write a method to compute all permutations of a string whose characters are
not necessarily unique. The list of permutations should not have duplicates.
'''

class Permutations:
    def __init__(self, string):
        self.letters = list(string)
        self.visited = set()

    def perm_(self, stack, permutations, start):
        if start == len(self.letters):
            permutation = ''.join(stack)
            if not permutation in self.visited:
                permutations.append(permutation)
                self.visited.add(permutation)
            return

        for i in range(start, len(self.letters)):
            stack.append(self.letters[i])
            self.letters[i], self.letters[start] = self.letters[start], self.letters[i]
            self.perm_(stack, permutations, start + 1)
            self.letters[i], self.letters[start] = self.letters[start], self.letters[i]
            stack.pop()
                    
    def permutations(self) -> list[str]:
        result = []
        self.perm_([], result, 0)
        return result
            

if __name__ == '__main__':
    ps = Permutations('aba').permutations()
    for p in ps:
        print(p)
    print(len(ps))
