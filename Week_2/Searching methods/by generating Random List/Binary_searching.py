import numpy as np
import time

l=list(np.random.randint(0, 10**5, 10000)) #This list has 10000 random integers from 0 to 100000
n=len(l)
print("Generated random list is", l)
print("")
l.sort()
print("Sorted random list is",l)

pos=0 # To store the position of the search element
first=0 #index of first element
last= n-1 #index of last element
search=int(input("Enter your search element : ")) 
start=time.time()
found = False #bool variable to check whether search element is present or not
while first<=last and not found: #looping begins
  mid=int((first+last)/2) #finding mid index position, has to be an int type
  if l[mid]==search: # if search element is at the mid index
    found= True
    pos=mid
  else: # for a case when search element is not at mid
    if search < l[mid]: # data is sorted so if condition satisfied, search element lies in first half
      last= mid-1 # for first half
      pos=last
    else: # for second half
      first= mid+1
      pos=first
if found==False:
  print("Element not found")
else:
  print("In the sorted list, element is at index position",pos)
print("Time taken in seconds is", time.time()-start) # gives the time elapsed in seconds
