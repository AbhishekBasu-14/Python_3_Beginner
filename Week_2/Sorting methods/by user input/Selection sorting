#Selection_Sort
import time # module for calculating time required by this algorithm
def selectionSort(l):
  start=time.time() # time calculation begins
  for i in range(n-1):
    min=i #assuming the first indexed element of the list is smallest
    for j in range(i+1, n): # i+1 because the first index shifts as the list is sub-divided and we are working on the unsorted list
      if l[min]>l[j]: # < : descending , > : ascending (here, we have implemented ascending order sorting)
        min = j 
    l[i], l[min] = l[min], l[i] # another way of swapping two elements of the list
  print("Time taken in seconds is", time.time()-start) # gives the time elapsed in seconds
n=int(input("How many nos. ? ")) # asking for user input
l=[]
for a in range(0,n):
    x=int(input("Enter your no. "))
    l.append(x)
print("Entered list is",l) #prints the list l
selectionSort(l) #calling the function
print("Sorted list is", l) # final sorted list

