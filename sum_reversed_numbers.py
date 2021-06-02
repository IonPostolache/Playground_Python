"""22. Write a Python program to compute the sum of the two reversed
numbers and display the sum in reversed form.
Input : 13, 14
Output : 27
Note : The result will not be unique for every number for example 31 is a reversed
form of several numbers of 13, 130, 1300 etc. Therefore all the leading zeros will be omitted     """


inputno=[13,14]
print(inputno)

def reversef(n):
    return n[::-1]

firstrev=reversef(str(inputno[0]))
secondrev=reversef(str(inputno[1]))
sumrev=int(firstrev)+int(secondrev)
#print(sumrev)
sumstring=str(sumrev)
sumnonrev=reversef(sumstring)
print(sumnonrev)
