"""16. Write a Python program to add the digits of a positive integer
repeatedly until the result has a single digit.
Input : 48
Output : 3
For example given number is 59, the result will be 5.
Step 1: 5 + 9 = 14
Step 1: 1 + 4 = 5    """

iinput=48
print(f"Input: {iinput}")

while iinput>9:
    string = str(iinput)
    count=0
    for i in range(0, len(string)):
        count=count+int(string[i])
        iinput=count

print(count)
