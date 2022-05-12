n=int(input("Enter the number: "))

for i in range(0,n):
    for j in range(0,n-i):
        print(' ',end=' ')
    for j in range(0,i+1):
        print("*",end=" ")
    if i>=1:
        for j in range(0,i):
            print('*',end=" ")
    print('\n')
for i in range(0,n):
    for j in range(0,i+1):
        print(' ',end=' ')
    for j in range(0,n-i):
        print("*",end=" ")
    if i<n-1:
        for j in range(0,n-i):
            print('*',end=" ")
    print('\n')