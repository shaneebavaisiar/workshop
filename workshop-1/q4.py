# Question 4: First Before Second Letter
# You are given three inputs: a string, one letter, and a second letter.
# Check if every instance of the first letter occurs before every instance of the second letter.
# ===================================================================================================
s=input('enter the string:')
first_letter=input('enter the first letter:')
second_letter=input('enter the second letter:')
for i in range(len(s)):
    if s[i]==second_letter:
        a=i
        break
for i in range(a,len(s)):
    if s[i]==first_letter:
        print('false')
        break
else:
    print('true')


