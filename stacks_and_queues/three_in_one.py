'''
Describe how you could use single array to implement 3 stacks.

brute force:

    - split array into 3 parts
    - when capacity is reached for 1st or 2nd part, reallocate the rest of the parts
      to increase 1st or 2nd part capacity

time: O(N)=N
space: O(N)=N
------
offset:
    - 1st stack would have elements 0, 3, 6
    - 2nd stack: 1, 4, 7
    - 3rd stack: 2, 5, 8

    adding element:
    - set arr[pointer] = el
    - move pointer += 3

    pop:
    - element = arr[pointer]
    - move pointer -= 3

time: O(N)=1
space: O(N)=3*N
'''
