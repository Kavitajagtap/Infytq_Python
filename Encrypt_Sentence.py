'''
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change
Note: 
Assume that the sentence would begin with a word and there will be only a single space between the words.
Perform case sensitive string operations wherever necessary.

Sample Input                                   Expected Output

the sun rises in the east                   eht snu sesir ni eht stea

'''
# Code ->

def encrypt_sentence(sentence):
    vowel_set = "aeiouAEIOU"
    final_list=[]
    word=sentence.split()
    for i in range(0,len(word)):
        if((i%2)==0):
            final_list.append(word[i][::-1])
        else:  
            vowels = []
            consonants = []
            for letter in word[i]:
                if letter in vowel_set:
                    vowels.append(letter)
                else:
                    consonants.append(letter)
            new_string = "".join(consonants) + "".join(vowels)
            final_list.append(new_string)
    return " ".join(final_list)
sentence="the sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)

