'''
Given a number n, write a program to find the sum of the largest prime factors of each of nine consecutive numbers starting from n.
g(n) = f(n) + f(n+1) + f(n+2) + f(n+3) + f(n+4) + f(n+5) + f(n+6) + f(n+7) + f(n+8)
where, g(n) is the sum and f(n) is the largest prime factor of n

For example,
g(10)=f(10)+f(11)+f(12)+f(13)+f(14)+f(15)+f(16)+f(17)+f(18) 
        =5 + 11 + 3 + 13 + 7 + 5 + 2 + 17 + 3 
        =66 

'''

Code ->

def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    ls = []
    for factor in list_of_factors:
        if is_prime(factor,factor//2):
            ls.append(factor)
    return max(ls)
    #Accepts the list of factors and returns the largest prime factor

def find_f(num):
    lis = find_factors(num)
    largest_pf = find_largest_prime_factor(lis)
    return largest_pf
    #Accepts the number and returns the largest prime factor of the number

def find_g(num):
    factor_sum = 0
    for i in range(num,num+9):
      factor_sum += find_f(i)
    return factor_sum
    #Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number

#Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10))

