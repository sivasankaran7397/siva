                                                                                                                                                                                                                                                                                                                                                                                   # Python program to

from collections import deque

stack = deque()

a=(input("enter the elament"))
b=(input("enter the elenment"))
c=(input("enter the element"))

stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack:')
print(stack)




print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)



