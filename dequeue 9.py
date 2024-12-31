from collections import deque
q = deque()
a=(input("enter the elemnt: "))
b=(input("enter the element: "))
c=(input("enter the element: "))

q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)
