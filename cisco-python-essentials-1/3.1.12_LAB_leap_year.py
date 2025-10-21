''' 3.1.12 **LAB** Essentials of the if-elif-else statement

---

## Scenario

As you surely know, due to some astronomical reasons, years may be _leap_ or _common_. The former are 366 days long, while the latter are 365 days long.

Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

- if the year number isn't divisible by four, it's a _common year_;
- otherwise, if the year number isn't divisible by 100, it's a _leap year_;
- otherwise, if the year number isn't divisible by 400, it's a _common year_;
- otherwise, it's a _leap year_.

Look at the code in the editor - it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.

The code should output one of two possible messages, which are `Leap year` or `Common year`, depending on the value entered.

It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: `Not within the Gregorian calendar period`. Tip: use the `!=` and `%` operators.

Test your code using the data we've provided.

  

## Test Data:

**Sample input:**
```
2000
```

**Expected output:**
```
Leap year
```

**Sample input:**
```
2015
```

**Expected output:**
```
Common year
```

**Sample input:**
```
1999
```

**Expected output:**
```
Common year
```

**Sample input:**
```
1996
```

**Expected output:**
```
Leap year
```

**Sample input:**
```
1580
```

**Expected output:**
```
Not within the Gregorian calendar period
```
'''

''' # Version 1
year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        msg = "Common year"
    elif year % 100 != 0:
        msg = "Leap year"
    elif year % 400 != 0:
        msg = "Common year"
    else:
        msg = "Leap year"

'''

# Version 2
def is_leap_year(year):
    if year < 1582:
        msg = "Not within the Gregorian calendar period"
    else:
        if year % 4 != 0:
            msg = "Common year"
        elif year % 100 != 0:
            msg = "Leap year"
        elif year % 400 != 0:
            msg = "Common year"
        else:
            msg = "Leap year"
    return msg

def test_code():
    sample_input = [2000, 2015, 1999, 1996, 1580]
    expected_output = ["Leap year", "Common year", "Common year", "Leap year", "Not within the Gregorian calendar period"]
    for _ in range(len(sample_input)):
        input = sample_input[_]
        output = is_leap_year(input)
        if output == expected_output[_]:
            print(f"Success! {input} is {output}")
        else:
            print(f"Error! {input} is {output}")

#print(is_leap_year(int(input("Enter a year: "))))
test_code()
