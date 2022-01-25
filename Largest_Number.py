'''
Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers. 
Note: Assume that all the numbers are two digit numbers.

Sample Input          23,34,55
 
Expected Output       553423

'''

# Code ->

def create_largest_number(number_list):
    res = ""
    for num in list(reversed(sorted(number_list))):
        res = res+ str(num)
    return (int(res))
        
number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)


 
