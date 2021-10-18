'''
An animal shelter, which holds only dogs and cats, operates on a strictly FIFO basis.
People must adopt either the oldest (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a cat or a dog (and will receive the oldest
animal of that type). Create the data structures to maintain this system, and implement
operations:
    enqueue
    dequeue_any
    dequeue_dog
    dequeue_cat
You may use the built in linked list type.

Solution:

    brute force:

    Maintain a single queue for all types of animals. dequeue_cat/dog iterates the
    queue from head to tail, until the necessary type is found. Use linked list 
    to implement the queue.

    O(N):
     enqueue: 1
     dequeue_any: 1
     dequeue_cat/dog: N

     improvements:

    dequeue_cat/dog in O(1)?

    maintain separate queues for cats and dogs. maintain the oldest animal
    separately.

    set oldest animal on first enqueue;
    on dequeue_any:
        


'''
from enum import Enum
from datetime import datetime

class AnimalType(Enum):
    CAT = 0
    DOG = 1


class Animal:
    def __init__(self, anim_type: AnimalType):
        self.type = anim_type
        self.created = datetime.now()

    def __eq__(self, other) -> bool:
        return self.type == other.type and self.created == other.created


class Node:
    
    def __init__(self):
        self.next = None
        self.value = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, value: Animal) -> Node:
        if not self.head:
            self.head = Node()
            self.head.value = value
            return self.head
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = Node()
            tail.next.value = value
            return tail.next



class AnimalShelter:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, animal: Animal) -> None:
        self.queue.add(animal)

    def dequeue_any(self) -> Animal | None:
        if not self.queue.head:
            return None
        result = self.queue.head
        self.queue.head = result.next
        return result.value

    def dequeue_animal(self, anim_type: AnimalType) -> Animal | None:
        if not self.queue.head:
            return None
        node = self.queue.head
        prev_node = None
        while node and node.value.type != anim_type:
            prev_node = node
            node = node.next
        if not node:
            return None
        if prev_node:
            prev_node.next = node.next
        return node.value

    def dequeue_cat(self) -> Animal | None:
        return self.dequeue_animal(AnimalType.CAT)

    def dequeue_dog(self) -> Animal | None:
        return self.dequeue_animal(AnimalType.DOG)


if __name__ == '__main__':
    shelter = AnimalShelter()
    assert not shelter.dequeue_any()

    cat = Animal(AnimalType.CAT)
    shelter.enqueue(cat)
    assert shelter.dequeue_any() == cat

    shelter.enqueue(Animal(AnimalType.DOG))
    shelter.enqueue(Animal(AnimalType.DOG))
    shelter.enqueue(Animal(AnimalType.DOG))
    shelter.enqueue(cat)
    shelter.enqueue(Animal(AnimalType.CAT))
    shelter.enqueue(Animal(AnimalType.DOG))
    assert shelter.dequeue_cat() == cat

    shelter = AnimalShelter()
    dog = Animal(AnimalType.DOG)
    shelter.enqueue(Animal(AnimalType.CAT))
    shelter.enqueue(Animal(AnimalType.CAT))
    shelter.enqueue(dog)
    shelter.enqueue(Animal(AnimalType.CAT))
    shelter.enqueue(Animal(AnimalType.CAT))
    assert shelter.dequeue_dog() == dog
