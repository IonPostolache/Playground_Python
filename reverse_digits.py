"""18. Write a Python program to reverse the digits of an integer.
Input : 234
Input : -234
Output: 432
Output : -432   """

integerno=int(input("What integer you want to reverse? > "))
#removing leading zero
if integerno%10==0:
    integerno/=10
#transform to integer just in case it comes as float
integernoi2=int(integerno)
#transform to string
string=str(integernoi2)

#taking care of the leading minus
if string[0]=="-":
    string_minus=string[1:]
    string_to_reverse=string_minus[::-1]
    complete_reversed=string[0]+string_to_reverse
    #solving the situation without minus
else:
    string_minus = string[:]
    string_to_reverse = string_minus[::-1]
    complete_reversed = string_to_reverse

print(complete_reversed)

