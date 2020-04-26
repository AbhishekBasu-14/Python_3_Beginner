# cook your dish here
T=int(input())
for i in range(T):
    s,w1,w2,w3= map(int,input().split())
    if(s>=(w1+w2+w3)): #clearly 1 strike is enough
        print("1")
    elif(s>=(w1+w2) or s>=(w2+w3)): #2 strikes
        print("2")
    else: 
        print("3")
        
    
