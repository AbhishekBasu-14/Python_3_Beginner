#Insertion_Sort
import time # module for calculating time required by this algorithm
def insertionSort(l):
  start=time.time() # time calculation begins
  for i in range(1,n):
    t=l[i] # setting value to a temporary variable
    j=i-1 # for shifting index position by 1 to the left, now values will be compared.
    while j>=0 and t<l[j]: # this looping includes index [0] and compares the value with the previous element 
      l[j+1]=l[j] # swap the values
      j=j-1 # decrementing counter variable j
    l[j+1]=t # setting to temporary variable
  print("Time taken in seconds is", time.time()-start) # gives the time elapsed in seconds
n=int(input("How many nos. ? ")) # asking for user input
l=[]
for a in range(0,n):
    x=int(input("Enter your no. "))
    l.append(x)
print("Entered list is",l) #prints the list l
insertionSort(l) #calling the function
print("Sorted list is",l)
