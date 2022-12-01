#Xabien Loor
#CS-175L
#vowelConsonant.py

def vowel(sentence):
    v_count = 0
    vowels = ['a','e','i','o','u']
    for letter in sentence:
        if letter in vowels:
            v_count += 1
    return v_count
def consonant(sentence):
    c_count = 0
    vowels = ['a','e','i','o','u',' ', '.', ',']
    for letter in sentence:
        if letter not in vowels:
            c_count += 1
    return c_count
        

def main():
    user = str(input('Enter a string: '))
    sentence = user.lower()
    consonant(sentence)
    vowel(sentence)
    print('The string you entered includes',vowel(sentence),'vowels and',consonant(sentence),'consonants.')

if __name__ == '__main__':
    main()




#Write a program with a function that accepts a string and returns the number of vowels that the string contains. The application should have another function that returns the number of consonants in the same string. The application should let the user enter a string and then display the number of vowels and consonants it contains.

#Submit your program directly to the Quiz 2 dropbox. Put your name, class code, and program name at the top of your code as you do with other assignments.

#Program name: vowelConsonant

#Console input/output: (your program must do these things)

#Enter a string: Function displays the character that appears most frequently in the string. If several characters have the same highest frequency, displays the first character with that frequency.

#The string you entered includes 48 vowels and 102 consonants.
