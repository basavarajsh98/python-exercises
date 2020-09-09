"""
Scope:
1)Input the letter
2)Convert the input letter to lowercase
3)Input the sentence
4)Convert the input sentence to lowercase
5)Extract words from sentence
6)Initialize the flag
6)Check if any word in the sentence doesn't start with the inputted letter and set the flag accordingly
7)Write the conditions to print the score based on the number of words in the sentence
"""

#input the letter
letter = input("Enter the letter: ")
#convert the input letter to lowercase
letter = letter.lower()
#input the sentence
sentence = input("Enter the sentence: ")
#convert the input sentence to lowercase
sentence = sentence.lower()
# to extract words from sentence
words = sentence.split() 
flag = 1
for word in words:
    # set the flag value to 0 if any word in the sentence doesn't start with the inputted letter
    if word.startswith(letter) == False:
        flag = 0
# The sentence should contain minimum 3 words and maximum any number of words.
if (flag == 1 & (len(words) >= 3)):
    if len(words) == 3:
        # For a minimum of three words a score of 2 is given
        print("Good, You get a score of 2")
    else:
        # Calculate the additional words
        factor = len(words) - 3
        # Each additional word gets a score of 2
        score = 2 + (factor*2)
        print("Good, You get a score of ", score)
else:
    # The sentences with less than minimum words gets no score
    print("No score")
