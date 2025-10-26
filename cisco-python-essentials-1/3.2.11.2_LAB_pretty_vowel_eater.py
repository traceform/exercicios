''' 3.2.11 **LAB** The _continue_ statement - the Pretty Vowel Eater

## Scenario

Your task here is even more special than before: you must redesign the (ugly) vowel eater from the previous lab and create a better, upgraded (pretty) vowel eater! Write a program that uses:

- a `for` loop;
- the concept of conditional execution (_if-elif-else_)
- the `continue` statement.

Your program must:

- ask the user to enter a word;
- use ==`user_word = user_word.upper()`== to convert the word entered by the user to upper case; we'll talk about **string methods** and the `upper()` method very soon - don't worry;
- use conditional execution and the `continue` statement to "eat" the following vowels _A_, _E_, _I_, _O_, _U_ from the inputted word;
- assign the uneaten letters to the `word_without_vowels` variable and print the variable to the screen.

Look at the code in the editor. We've created `word_without_vowels` and assigned an empty string to it. Use concatenation operation to ask Python to combine selected letters into a longer string during subsequent loop turns, and assign it to the `word_without_vowels` variable.

Test your program with the data we've provided for you.

  

## Test data:

**Sample input:**
```
Gregory
```

**Expected output:**
```
GRGRY
```

**Sample input:**
```
abstemious
```

**Expected output:**
```
BSTMS
```

**Sample input:**
```
IOUEA
```

**Expected output:**
```
 
```
'''

'''
# Version 1
user_word = input("Enter a word: ")
alt_word = user_word.upper()
vowels = ['A','E','I','O','U']

word_without_vowels = ''
for letter in alt_word:
    if letter in vowels:
        continue
    word_without_vowels += letter
print(word_without_vowels)

'''

# Version 2
try:
    user_word = input("Enter a word: ")
    alt_word = user_word.upper()
    vowels = ['A','E','I','O','U']

    word_without_vowels = ''
    for letter in alt_word:
        if letter in vowels:
            continue
        word_without_vowels += letter
    print(word_without_vowels)
except KeyboardInterrupt:
    print("\nProgram terminated.")
except:
    print("Error!")