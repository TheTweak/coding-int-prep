'''
Design and implement a hash table which uses linked lists to handle collisions.
'''
class Node:
    pass

class Node:
    def __init__(self, item):
        self.item = item
        self.next: Node = None


class LinkedList:
    def __init__(self):
        self.head: Node = None

    def append(self, item) -> None:
        if not self.head:
            self.head = Node(item)
            return

        n = self.head
        while n.next:
            n = n.next
        n.next = Node(item)


class HashTable:
    def __init__(self, capacity: int = 32):
        self.buckets = [LinkedList() for _ in range(capacity)]
        self.size = 0

    def __get_bucket(self, key) -> LinkedList:
        h = hash(key)
        return self.buckets[h%len(self.buckets)]

    def set(self, key, value) -> None:
        bucket = self.__get_bucket(key)
        n = bucket.head
        while n:
            if n.item[0] == key:
                n.item = (key, value)
                return
            
            n = n.next
        bucket.append((key, value))
        self.size += 1

    def get(self, key) -> object:
        bucket = self.__get_bucket(key)
        n = bucket.head
        while n:
            if n.item[0] == key:
                return n.item[1]
            
            n = n.next
        return None

    def remove(self, key) -> None:
        bucket = self.__get_bucket(key)
        n = bucket.head
        prev = n
        while n:
            if n.item[0] == key:
                self.size -= 1
                if prev == n:
                    bucket.head = None
                else:
                    prev.next = n.next
                break
            
            prev = n
            n = n.next


if __name__ == '__main__':
    ht = HashTable()
    ht.set('a', 31337)
    assert ht.get('a') == 31337
    ht.set('a', 123)
    assert ht.get('a') == 123
    ht.remove('a')
    assert ht.get('a') is None
    ht.set('b', 3)
    ht.set('c', 5)