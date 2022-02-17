'''
Write a recursive function, is_palindrome() to find out whether a string is a palindrome or not. The function should return true, if it is a palindrome. Else it should return 
false. 

'''
Code -->

def is_palindrome(word):
    if(len(word.lower()) == 0):
        return True
    elif(word.lower()[0] == word.lower()[-1]):
        return is_palindrome(word.lower()[1:-1])
    else:
        return False
result=is_palindrome("Nitin")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
