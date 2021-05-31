"""16. Write a Python program to add the digits of a positive integer
repeatedly until the result has a single digit.
Input : 48
Output : 3
For example given number is 59, the result will be 5.
Step 1: 5 + 9 = 14
Step 1: 1 + 4 = 5    """

input=48
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

while first_loop>=10:
    second_loop=digits(first_loop)
    print(second_loop)
    first_loop=second_loop
    continue
