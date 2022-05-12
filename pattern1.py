n=int(input('Enter the size of pattern: '))
m=int(input('Enter 1 for simple pattern / Enter 0 for inverted pattern: '))
while True:
    if m==1:
        for i in range(0,n):
            for j in range(0,i+1):
                print("*",end=' ')
            print('\n')
        break

    elif m==0:
        for i in range(0,n):
            for j in range(0,n-i):
                print("*",end=' ')
            print('\n')
        break

    else:
        print('Wrong input!!!!')
        m=int(input('Enter again (between 0 or 1): '))

