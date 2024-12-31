L1= [2,4,6,8,10,12]
x=8 # element that we want to be found
i=0 # pointer
while i<len(L1):
 if L1[i]==x:
    print(f'element {x} present at {i}th position')
 break
i+=1
if i>=len(L1):
    print('Element is not present')


