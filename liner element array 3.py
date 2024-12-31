def linear_search(L, key, i):
  if i >= len(L):
return -1;
  if L[i] == key:
return i
 return linear_search(L, key, i + 1)
L = [1, 2, 3, 4, 5, 6, 7]
key = 5
x = linear_search(L, key, 0)
if x != -1:
  print('List : ', L)
  print(f'Element {key} is available on index : {x}')
else:
	print(The element is not present)
