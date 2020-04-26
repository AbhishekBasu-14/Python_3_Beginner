import numpy as np
import time

l=list(np.random.randint(0, 10**5, 10000)) #This list has 10000 random integers from 0 to 100000
n=len(l)
print("Generated random list is", l)
print("")

def bubbleSort(l):
  bubble_start=time.time() # time calculation begins for bubblesort
  for i in range(n): # loops n no. of times for n no. of user inputs
      for j in range(n-i-1): # loops for comparing every 2 consecutive elements
          if l[j]>l[j+1]: # < : descending , > : ascending (here, we have implemented ascending order sorting)
              t=l[j] 
              l[j]=l[j+1]
              l[j+1]=t
  print("Time taken in seconds is", time.time()-bubble_start) # gives the time elapsed in seconds

bubbleSort(l) #calling the function
print("Bubble sorted list is",l) # final sorted list
