# Question 3: Power Ranger
# Given 3 inputs n, minimum, & maximum, find the number of
# values raised to the nth power that lie in the range [minimum, maximum], inclusive.
# ==================================================================================================
n=int(input('enter the number:'))
minimum=int(input('enter the minimum range:'))
maximum=int(input('enter the maximum range:'))
count=0
for i in range(maximum+1):
    if i**n in range(minimum,maximum+1):
        count+=1
        print(i)
        i+=1
print('count:',count)
