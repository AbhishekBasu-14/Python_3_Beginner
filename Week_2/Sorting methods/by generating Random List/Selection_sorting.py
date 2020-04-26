import numpy as np
import time

l=list(np.random.randint(0, 10**5, 10000)) #This list has 10000 random integers from 0 to 100000
n=len(l)
print("Generated random list is", l)
print("")

def selectionSort(l):
  sel_start=time.time() # time calculation begins for selection sort
  for i in range(n-1):
    min=i #assuming the first indexed element of the list is smallest
    for j in range(i+1, n): # i+1 because the first index shifts as the list is sub-divided and we are working on the unsorted list
      if l[min]>l[j]: # < : descending , > : ascending (here, we have implemented ascending order sorting)
        min = j 
    l[i], l[min] = l[min], l[i]
  print("Time taken in seconds is", time.time()-sel_start) # gives the time elapsed in seconds

selectionSort(l) #calling the function
print("Selection sorted list is",l) # final sorted list
