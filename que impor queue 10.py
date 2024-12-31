from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize())

a=(iput("enter the element"))
b=(input("enter the element"))
c=(input("entr the element"))

q.put('a')
q.put('b')
q.put('c')

print("\nFull:", q.full()) 
print("\nElements dequeued from the queue")

print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())
