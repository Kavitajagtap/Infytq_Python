'''
Problem Statement
Write a python function find_smallest_number() which accepts a number n and returns the smallest number having n divisors.
Handle the possible errors in the code written inside the function.

Sample Input :       16

Expected Output:     120

'''

Code ->

#lex_auth_01269442760027340879
def find_divisors(num):
    divisors = []
    for i in range(1,num+1):
        if(num%i == 0):
            divisors.append(i)
    return len(divisors)
def find_smallest_number(num):
    for i in range(2,1000):
        if find_divisors(i) == num:
                return i

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
