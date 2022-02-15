'''
Write a python function, find_pairs_of_numbers() which accepts a list of positive integers with no repetitions and returns count of pairs of numbers in the list that adds up to n.
The function should return 0, if no such pairs are found in the list.

Sample Input  :  1.  [1, 2, 7, 4, 5, 6, 0, 3], 6            2. [3, 4, 1, 8, 5, 9, 0, 6], 9

Expected Output :             3                                             4

'''
# Code ->

def find_pairs_of_numbers(num_list, n):
    # Remove pass and write your logic here
    count = 0
    for i in num_list:
        for j in num_list[num_list.index(i)+1:]:
            if i+j  == n:
                count = count + 1
            else:
                pass
    return count
num_list = [1, 2, 7, 4, 5, 6, 0, 3]
n = 6
print(find_pairs_of_numbers(num_list, n))
