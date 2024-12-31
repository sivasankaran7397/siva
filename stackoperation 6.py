
stack = []

a=(input("enter the element"))
b=(input("enter the element"))
c=(input("enter the element"))
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)


print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

