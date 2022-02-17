'''
Write a python function find_duplicates(), which accepts a list of numbers and returns another list containing all the duplicate values in the input list and the order should
be same as in the input list. If there are no duplicate values, it should return an empty list.

Sample Input :      [12,54,68,759,24,15,12,68,987,758,25,69]

Expected Output:    [12, 68]

'''

# Code -->


def find_duplicates(list_of_numbers):
    a = {i:list_of_numbers.count(i) for i in list_of_numbers}
    return sorted([k for k,v in a.items() if v > 1])

list_of_numbers=[12,54,68,759,24,15,12,68,987,758,25,69]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)


