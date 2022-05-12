n=int(input("Enter the number: "))
for i in range(0,n):
    for j in range(0,n-i):
        print(' ',end=' ')
    for k in range(0,i+1):
        print(k+1,end='   ')
    print('\n')