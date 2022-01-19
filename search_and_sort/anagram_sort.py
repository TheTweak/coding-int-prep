'''
Sort array of strings such that anagrams are next to each other.
'''

def create_key(s: str) -> str:
    return ''.join(sorted(s))


def sort_anagrams(a: list[str]) -> list[str]:
    anagrams_map = {}

    for word in a:
        k = create_key(word)
        anagrams_map.setdefault(k, []).append(word)

    result = []
    for _, v in anagrams_map.items():
        result.extend(v)

    return result


if __name__ == '__main__':
    words = ['fluster', 'dog', 'adobe', 'restful', 'god', 'abode', 'test']
    sorted_words = sort_anagrams(words)
    print(sorted_words)
