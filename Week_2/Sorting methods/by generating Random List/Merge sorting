import numpy as np
import time

l=list(np.random.randint(0, 10**5, 10000)) #This list has 10000 random integers from 0 to 100000
n=len(l)
print("Generated random list is", l)
print("")

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


merge_start=time.time()
mergeSort(l) #calling the function
print("Merge sorted list is",l) # final sorted list
print("Time taken in seconds is", time.time()-merge_start) # gives the time elapsed in seconds
