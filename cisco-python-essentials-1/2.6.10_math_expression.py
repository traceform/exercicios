''' 2.6.10 **LAB** Operators and expressions

## Scenario

Your task is to complete the code in order to evaluate the following expression:

![Math expression](https://www.netacad.com/content/pe1/1.0/courses/content/m2/en-US/assets/ae5d9dec1dda05fda93912c1d7191ee42d10c8e5.png)

The result should be assigned to y. Be careful - watch the operators and keep their priorities in mind. Don't hesitate to use as many parentheses as you need.

You can use additional variables to shorten the expression (but it's not necessary). Test your code carefully.

  

# Test Data

**Sample input:**
```
1
```

**Expected output:**
```
y = 0.6000000000000001
```

**Sample input:**
```
10
```

**Expected output:**
```
y = 0.09901951266867294
```

**Sample input:**
```
100
```

**Expected output:**
```
y = 0.009999000199950014
```

**Sample input:**
```
-5
```

**Expected output:**
```
y = -0.19258202567760344
```
'''

def test_code():
    """Tests the code with predefined values"""
    input_list = [1, 10, 100, -5, 0, 'a', True, False]
    output_list = [0.6000000000000001, 0.09901951266867294, 0.009999000199950014, -0.19258202567760344, None, None, 0.6000000000000001, None]
    for i in range(0,len(input_list)):
        input = input_list[i]
        output = output_list[i]
        result, msg = math_expression(input)
        if result == output:
            print(f"Success! {input} returns {output}")
        else:
            print(f"Error! {input} does NOT result in {output}")

def math_expression(x):
    """Evaluates the math expression with a given number"""
    y, msg = None, None
    try:
        y = 1/(x + 1/(x + 1/(x + 1/x)))
    except ZeroDivisionError:
        msg = "Error! Division by zero is not allowed!"
    except:
        msg = "Something went wrong!"
    return y, msg

#test_code()

if __name__ == "__main__":
    y, msg = math_expression(float(input("Enter value for x: ")))
    if y is None:
        print(msg)
    else:
        print("y =", y)
