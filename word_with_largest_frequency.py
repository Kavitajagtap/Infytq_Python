'''
Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.
Rules:
The word should have the largest frequency.
In case multiple words have the same frequency, then choose the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a single space between the words.
Perform case insensitive string comparisons wherever necessary.

Sample Input:     "Courage is not the absence of fear but rather the judgement that something else is more important than fear"

Expected Output    fear 2

'''
def max_frequency_word_counter(data):
    data.lower()
    words = data.split(" ")
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word] = 1
    max_freq = max(word_count.values())
    max_freq_words = []
    for word in word_count:
        if word_count[word] == max_freq:
            max_freq_words.append(word)
    if len(max_freq_words) == 1:
        print(max_freq_words[0],max_freq)
    else:
        max_length = 0
        max_word = ""
        for word in max_freq_words:
            if len(word)>max_length:
                max_length = len(word)
                max_word = word
        print(max_word,max_freq)
        
    #start writing your code here
    #Populate the variables: word and frequency


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)


#Provide different values for data and test your program.
data="Listen to the big clock Tick tock tick"
max_frequency_word_counter(data)



