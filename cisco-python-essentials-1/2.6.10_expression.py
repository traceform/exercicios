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
    input_list = [1, 10, 100, -5]
    output_list = [0.6000000000000001, 0.09901951266867294, 0.009999000199950014, -0.19258202567760344]
    for i in range(0,len(input_list)):
        input = input_list[i]
        output = output_list[i]
        if math_expression(input) == output:
            print(f"Success! {input} returns {output}")
        else:
            print(f"Error! {input} does NOT result in {output}")

def math_expression(x):
    y = 1/(x + 1/(x + 1/(x + 1/x)))
    return y

#test_code()
print("y =", math_expression(float(input("Enter value for x: "))))
