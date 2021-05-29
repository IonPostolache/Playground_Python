"""16. Write a Python program to add the digits of a positive integer
repeatedly until the result has a single digit.
Input : 48
Output : 3
For example given number is 59, the result will be 5.
Step 1: 5 + 9 = 14
Step 1: 1 + 4 = 5    """

input=988779999777597987987098670986098799999978
print(f"Input: {input}")

def digits(n):
    numberdef=0
    string = str(n)
    for i in string:
        integerdef=int(i)
        numberdef=numberdef+integerdef
    return numberdef

first_loop=digits(input)
print(first_loop)

if first_loop>=10:
    second_loop=digits(first_loop)
    print(second_loop)

if second_loop>=10:
    third_loop=digits(second_loop)
    print(third_loop)
