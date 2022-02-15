'''
A teacher is in the process of generating few reports based on the marks scored by the students of her class in a project based assessment.
Assume that the marks of her 10 students are available in a tuple. The marks are out of 25.

Write a python program to implement the following functions:

1. find_more_than_average(): Find and return the percentage of students who have scored more than the average mark of the class.

2. generate_frequency(): Find how many students have scored the same marks. For example, how many have scored 0, how many have scored 1, how many have scored 3….how many 
   have scored 25. The result should be populated in a list and returned.

3. sort_marks(): Sort the marks in the increasing order from 0 to 25. The sorted values should be populated in a list and returned.

Sample Input     : list_of_marks = (12,18,25,24,2,5,18,20,20,21)

Expected Output  : 70.0 
                   [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 0, 1, 1]
                   [2, 5, 12, 18, 18, 20, 20, 21, 24, 25] 
                   
'''

# Code ->

#lex_auth_01269438947391897654

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
   class_avg = sum(list_of_marks)/10
   count_of_student_scored_above_avg = sum(map(lambda x : x > class_avg, list_of_marks))
   return (count_of_student_scored_above_avg/10)*100

def sort_marks():
    return sorted(list_of_marks)

def generate_frequency():
    mark_frequecy_list = [0]*26
    for mark in list_of_marks:
        mark_frequecy_list[mark]+=1
    return mark_frequecy_list

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())


