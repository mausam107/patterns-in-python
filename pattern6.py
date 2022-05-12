n=int(input("Enter the no."))
for i in range(0,n):
    for j in range(0,n-i):
        print(' ',end=' ')
    k=i+1
    while k>0:
        print(k,end=' ')
        k=k-1
    
    if i>=1:
        for l in range(1,i+1):
            print(l+1,end=" ")

    print('\n')
