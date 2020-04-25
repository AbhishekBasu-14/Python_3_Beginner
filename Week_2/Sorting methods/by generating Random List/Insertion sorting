import numpy as np
import time

l=list(np.random.randint(0, 10**5, 10000)) #This list has 10000 random integers from 0 to 100000
n=len(l)
print("Generated random list is", l)
print("")

def insertionSort(l):
  ins_start=time.time() # time calculation begins for insertion sort
  for i in range(1,n):
    t=l[i] # setting value to a temporary variable
    j=i-1 # for shifting index position by 1 to the left, now values will be compared.
    while j>=0 and t<l[j]: # this looping includes index [0] and compares the value with the previous element 
      l[j+1]=l[j] # swap the values
      j=j-1 # decrementing counter variable j
    l[j+1]=t # setting to temporary variable
  print("Time taken in seconds is", time.time()-ins_start) # gives the time elapsed in seconds

insertionSort(l) #calling the function 
print("Insertion sorted list is",l) # final sorted list
