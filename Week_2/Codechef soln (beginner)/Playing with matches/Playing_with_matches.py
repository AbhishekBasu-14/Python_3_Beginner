# cook your dish here
T=int(input())
d={'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6} #dictionary with key and value
for i in range(T):
    m,n=map(int,input().split())
    sum=m+n
    count=0
    for j in str(sum): #check each digit using string index
        if j in d:
            count=count+d[j]
    print(count)
