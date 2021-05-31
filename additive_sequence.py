"""17. Write a Python program to find whether it contains an additive sequence or not.
The additive sequence is a sequence of numbers where the sum of the first two numbers is equal to the third one.
Sample additive sequence: 6, 6, 12, 18, 30
In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
Also, you can split a number into one or more digits to create an additive sequence.
Sample additive sequence: 66121830
In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
Note : Numbers in the additive sequence cannot have leading zeros.    """

sequ=[6,6,12,18,30]
print(sequ)
length=len(sequ)-2

for i in range(0, length):
    if sequ[0]==0:
        print("The additive sequence cannot have leading zeroes!")
        break
    if sequ[i]+sequ[i+1]==sequ[i+2]:
        print(f"Yes, the three numbers {sequ[i], sequ[i+1], sequ[i+2]} form an additive sequence!")
    else:
        print(f"No, the three numbers {sequ[i], sequ[i+1], sequ[i+2]} doesn't form an additive sequence!")
