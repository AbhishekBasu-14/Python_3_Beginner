#Linear_Search 
#using Random List
import numpy as np
import time

l=list(np.random.randint(0, 100, 10)) #This list has 10000 random integers from 0 to 100000
n=len(l)
print("Generated random list is", l)
print("")

pos= -1 #for position of element
search=int(input("Enter search element: "))
start=time.time()
for i in range(0,n):
  if l[i]==search:
    pos=i
if pos > -1:
  print("Element found at index position",pos)
else:
  print("Element not found")
print("Time taken in seconds is", time.time()-start) # gives the time elapsed in seconds
