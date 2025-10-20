''' 3.1.6 **LAB** Variables - Questions and answers

## Scenario

Using one of the comparison operators in Python, write a simple two-line program that takes the parameter `n` as input, which is an integer, and prints `False` if `n` is less than `100`, and `True` if `n` is greater than or equal to `100`.

Don't create any `if` blocks (we're going to talk about them very soon). Test your code using the data we've provided for you.

## Test Data

**Sample input:**
```
55
```

**Expected output:**
```
False
```

**Sample input:**
```
99
```

**Expected output:**
```
False
```

**Sample input:**
```
100
```

**Expected output:**
```
True
```

**Sample input:**
```
101
```

**Expected output:**
```
True
```

**Sample input:**
```
-5
```

**Expected output:**
```
False
```

**Sample input:**
```
+123
```

**Expected output:**
```
True
```
'''

''' # Version 1
n = float(input("Type a number: ))
print(n >= 100)

'''

# Version 2
def greater_than_or_equal_to_100(n):
    return = n >= 100

def test_code():
    input = [55, 99, 100, 101, -5, +123]
    output = [False, False, True, True, False, True]
    for _ in range(len(input)):
        if greater_than_or_equal_to_100(input[_]) == output[_]:
            print(f"Success! Is {input[_]} greater than or equal to 100? {output[_]}!")
        else:
            print(f"Error! Is {input[_]} greater than or equal to 100? {output[_]}?")

#test_code()
print(greater_than_or_equal_to_100(float(input("Type a number: "))))
