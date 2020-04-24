# cook your dish here
import math
T=int(input())
for _ in range(T):
    n,k,s = map(int,input().split())
    total= k*s
    sundays= s//7 #no. of sundays
    total_days= (s-sundays) #available days for chocolate
    if total_days*n >= total:
        print(math.ceil(total/n))
    else:
        print(-1)
    
