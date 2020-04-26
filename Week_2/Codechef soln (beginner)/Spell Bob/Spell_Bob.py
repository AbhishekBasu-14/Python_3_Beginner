# cook your dish here
# cook your dish here
T=int(input())
for i in range(T):
    u=input() #upper letter
    l=input() #lower letter
    l1=[u[0],l[0]] #set 1
    l2=[u[1],l[1]] #set 2
    l3=[u[2],l[2]] #set 3
    if ('b'in l1) and ('o'in l2)and('b'in l3):
        print('yes')
    elif ('b'in l1)and('b'in l2)and('o' in l3):
        print('yes')
    elif ('o'in l1)and('b'in l2)and('b'in l3):
        print('yes')
    else:
        print('no')
    
