# cook your dish here
T=int(input())
for _ in range(T):
    n, m = map(int,input().split())
    l= []
    result1,result2 = 0,0 #possible results
    for i in range(n):
        l.append(input())
    for i in range(len(l)):
        for j in range(len(l[i])):
            if (i+j)%2 == 0:
                if l[i][j] == 'R':
                    result1 += 5
                else:
                    result2 += 3
            else:
                if l[i][j] == 'R':
                    result2 += 5
                else:
                    result1 += 3
    print(min(result1,result2))
