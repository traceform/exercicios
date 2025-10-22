''' 3.2.10 **LAB** The _continue_ statement - the Ugly Vowel Eater

## Scenario

The `continue` statement is used to skip the current block and move ahead to the next iteration, without executing the statements inside the loop.

It can be used with both the <code>while</code> and <code>for</code> loops.

Your task here is very special: you must design a vowel eater! Write a program that uses:

- a `for` loop;
- the concept of conditional execution (_if-elif-else_)
- the `continue` statement.

Your program must:

- ask the user to enter a word;
- use ==`user_word = user_word.upper()`== to convert the word entered by the user to upper case; we'll talk about **string methods** and the `upper()` method very soon - don't worry;
- use conditional execution and the `continue` statement to "eat" the following vowels _A_, _E_, _I_, _O_, _U_ from the inputted word;
- print the uneaten letters to the screen, each one of them on a separate line.

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

''' # Version 1
user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in ['A','E','I','O','U']:
        continue
    print(letter)

'''

'''
# Version 2
user_word = input("Enter a word: ").upper()
vowels = ['A','E','I','O','U']

for letter in user_word:
    if letter in vowels:
        continue
    print(letter)

'''

# Version 3
try:
    user_word = input("Enter a word: ")
    alt_word = user_word.upper()
    vowels = ['A','E','I','O','U']
    
    for letter in alt_word:
        if letter in vowels:
            continue
        print(letter)
except KeyboardInterrupt:
    print("\nProgram terminated.")
except:
    print("Something went wrong!")
