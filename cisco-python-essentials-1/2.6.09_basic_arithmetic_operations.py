''' 2.6.9 **LAB** Simple input and output

## Scenario

Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.

The results have to be printed to the console.

You may not be able to protect the code from a user who wants to divide by zero. That's okay, don't worry about it for now.

Test your code - does it produce the results you expect?

We won't show you any test data - that would be too simple.
'''

def test_code():
    input_list = [1, 10, 100, -5]
    output_list = [0.6000000000000001, 0.09901951266867294, 0.009999000199950014, -0.19258202567760344]
    for i in range(0,len(input_list)):
        input = input_list[i]
        output = output_list[i]
        if main(input) == output:
            print(f"Success! {input} returns {output}")
        else:
            print(f"Error! {input} does NOT result in {output}")

def main(x):
    y = 1/(x + 1/(x + 1/(x + 1/x)))
    return y

test_code()

#x = float(input("Enter value for x: "))

#y = 1/(x + 1/(x + 1/(x + 1/x)))

#print("y =", y)

