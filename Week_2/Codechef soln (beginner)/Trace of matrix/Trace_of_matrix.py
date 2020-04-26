# cook your dish here
T=int(input())
for i in range(T):
    n = int(input()) 
    R=C=n #square matrix
    matrix = [list(map(int, input().split())) for i in range (n)] #listing 3x3 sq matrix from user input
    m=0 #for max value in each iteration
    for i in range (R):
        tr1=0
        tr2=0
        for j in range (C):
            tr1+=matrix[i+j][j] 
            tr2+=matrix[j][i+j]
            if max([tr1,tr2])>m:
                m=max([tr1,tr2])
        C=C-1
    print(m)
