#Bubble_Sort
import time # module for calculating time required by this algorithm
def bubbleSort(l):
  start=time.time() # time calculation begins
  for i in range(n): # loops n no. of times for n no. of user inputs
      for j in range(n-i-1): # loops for comparing every 2 consecutive elements
          if l[j]>l[j+1]: # < : descending , > : ascending (here, we have implemented ascending order sorting)
              t=l[j] 
              l[j]=l[j+1]
              l[j+1]=t
  print("Time taken in seconds is", time.time()-start) # gives the time elapsed in seconds
n=int(input("How many nos. ? ")) # asking for user input
l=[]
t=0 # temporary variable for swapping
for a in range(0,n):
    x=int(input("Enter your no. "))
    l.append(x)
print("Entered list is",l) #prints the list l
bubbleSort(l) #calling the function
print("The sorted list is",l) # final sorted list
