'''
Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.

Sample Input                                 Expected output

"I like Python"                                  lieyon                               
"Java is a very popular language"

'''

# Code ->

#lex_auth_012693825794351104168

def find_common_characters(msg1,msg2):
    msg3 = ""
    for i in msg1:
       if(i in msg2 and i not in msg3 and i != " "):
           msg3+=i
    if len(msg3) == 0:
        return -1
    return msg3

msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
