''''
Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
The ticket number should be generated as airline:src:dest:number
where

1. Consider AI as the value for airline
2. src and dest should be the first three characters of the source and destination cities.
3. number should be auto-generated starting from 101

The program should return the list of ticket numbers of last five passengers.
Note: If passenger count is less than 5, return the list of all generated ticket numbers.

'''
# Code ->

#lex_auth_012693763253788672132

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    if(no_of_passengers < 5):
        x = 1
        while(x <= no_of_passengers):
           ticket_number_list.append(('{0}:{1}:{2}:{3}'.format(airline,source[:3],destination[:3],100+x)))
           x += 1
        return ticket_number_list 
    else:
         x = no_of_passengers-5+1
         #Write your logic here
         while( x <= no_of_passengers):
           ticket_number_list.append(('{0}:{1}:{2}:{3}'.format(airline,source[:3],destination[:3],100+x)))
           x += 1
   
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",2))
