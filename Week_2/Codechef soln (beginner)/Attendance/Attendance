#cook your dish here
T=int(input())
for i in range(T):
    n=int(input()) #no. of names
    first_name=[] #list of first name
    last_name=[] #list of surname
    for i in range(n):
        name=input().split() #splitting user input name for adding in 2 different arrays
        first_name.append(name[0])
        last_name.append(name[1])
    for j in range(len(first_name)):
        if first_name.count(first_name[j])>1: #count() gives no. of times an element repeats
            print(first_name[j],last_name[j])
        else:
            print(first_name[j])
