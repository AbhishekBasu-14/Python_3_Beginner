#Binary_Search
n=int(input("How many nos. ? ")) # asking for user input
l=[]
for a in range(0,n):
    x=int(input("Enter your no. "))
    l.append(x)
print("Entered list is",l) #prints the list l
l.sort() #Sorting the list using inbuilt method for lists.
print("Sorted list in ascending order is", l)
pos=0 # To store the position of the search element
first=0 #index of first element
last= n-1 #index of last element
search=int(input("Enter your search element : ")) 
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
