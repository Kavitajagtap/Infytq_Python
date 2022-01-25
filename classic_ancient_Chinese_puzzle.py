'''
Write a python program to solve a classic ancient Chinese puzzle.
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Sample Input                   Expected Output
 
heads-150 legs-400                100 50

heads-3 legs-11                   No solution

heads-3 legs-12                   0 3

heads-5 legs-10                   5 0

'''

# Code ->

def solve(heads,legs):
  error_msg="No solution"
  chicken_count=0
  rabbit_count=0
  #Start writing your code here
  if legs % 2 == 0 and legs > heads:
    rabbit_count = (legs // 2 ) - heads
    chicken_count = heads - rabbit_count
    print(chicken_count,rabbit_count)
  else:
   print(error_msg)

#Provide different values for heads and legs and test your program
solve(38,131)
