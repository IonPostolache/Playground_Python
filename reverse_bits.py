"""19. Write a Python program to reverse the bits of an integer (32 bits unsigned).
Input : 1234
Output : 1260388352
For example, 1234 represented in binary as 10011010010 and returns 1260388352 which
represents in binary as 1001011001000000000000000000000.     """


number=int(input("Type the number > "))
#print(number)
bits=bin(number)
print(bits)
print("{0:b}".format(number))
#int(string, base)
print(int("10011010010", 2))
reversed=bits[-1:1:-1]
print(reversed)
reversed=reversed+(32-len(reversed))*"0"
print(reversed)
print("Output:", int("01001011001000000000000000000000", 2))
