# Question 6: Return maximum occurring character in an input string
# Sample Input:
#     "test"
# Sample Output:
#     t
# ==========================================================================
# string=input('enter the string:')
# for i in string:
#     print(i)
s='test'
count=0
j=0
while j<=len(s):
    for i in range(len(s)):
        if s[i]==s[j]:
            count+=1
            print(count,s[i])
    j+=1

