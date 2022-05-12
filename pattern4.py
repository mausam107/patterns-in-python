n=int(input("Enter No."))
for i in range(0,n):
    for j in range(0,n-i):
        print(' ',end=' ')
    for k in range(0,n):
        print('*',end=' ')
    print('\n')