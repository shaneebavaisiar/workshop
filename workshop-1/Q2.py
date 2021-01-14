# Question 2: Find Sum of the Series Given a natural number n (where 1≤n≤9), find the sum of the series having n
# number of numbers such that the series is n,nn,nnn,…nnn…n times.Hence, the required sum isn+nn+nnn+⋯+nnn…n
n=int(input('enter the number:'))
i=0
sum=0
total=0
while i<n:
    sum+=n*(10**i)
    total=total+sum
    i+=1
    print(sum)
print('total:',total)


