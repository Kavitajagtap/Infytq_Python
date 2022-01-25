'''

Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

Provide different String values and test your program

Sample Input:       AAAABBBBCCCCCCCC         AABCCA

Expected Output       4A4B8C                 2A1B2C1A

'''
# Code ->

#lex_auth_012693816331657216161

def encode(message):
    c=1
    st=""
    for i in range(len(message)-1):
        if(message[i]==message[i+1]):
            c+=1
        else:
            st=st+str(c)+message[i]
            int(c)
            c=1
    if(len(message)==1):
        st= str(c) +message[0]
    
    else:
        st=st+str(c)+message[i+1]
        int(c)
        c=1
    return st
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)







 
