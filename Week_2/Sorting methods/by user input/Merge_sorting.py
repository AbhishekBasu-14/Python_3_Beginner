#Merge_Sort
import time
def mergeSort(l): 
	if len(l) >1: 
		mid = len(l)//2 #Finding the mid of the array 
		L = l[:mid] # first half 
		R = l[mid:] # second half 

		mergeSort(L) # Sorting the first half 
		mergeSort(R) # Sorting the second half 

		i = j = k = 0
		
		# merging sorted half array
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				l[k] = L[i] 
				i+=1
			else: 
				l[k] = R[j] 
				j+=1
			k+=1
		
		while i < len(L): #to check if all elements are used
			l[k] = L[i] 
			i+=1
			k+=1
		
		while j < len(R): 
			l[k] = R[j] 
			j+=1
			k+=1

n=int(input("How many nos. ? ")) # asking for user input
l=[]
for a in range(0,n):
    x=int(input("Enter your no. "))
    l.append(x)
print("Entered list is",l) #prints the list l
start=time.time() # time calculation begins
mergeSort(l) #calling the function
print("Time taken in seconds is", time.time()-start) # gives the time elapsed in seconds
print("The sorted array is",l)
