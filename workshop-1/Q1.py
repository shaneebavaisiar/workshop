# Question 1: Print a * Triangle
# =================================================
n=int(input('enter the number:'))
for i in range(0,n):
    for j in range(0,2*n-1):
        if((j+i==n-1)|(j-i==n-1)|(i==n-1)):
            print('*',end='')
        else:
            print(' ',end='')
    print()
