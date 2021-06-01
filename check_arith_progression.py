"""20. Write a Python program to check a sequence of numbers is an arithmetic progression or not.
Input : [5, 7, 9, 11]
Output : True
In mathematics, an arithmetic progression or arithmetic sequence is a sequence of numbers
such that the difference between the consecutive terms is constant.
For example, the sequence 5, 7, 9, 11, 13, 15 ... is an arithmetic progression with common difference of 2. """

input_list=[5,7,9,11]
print(input_list)
truelist=[]
for i in range(0, (len(input_list)-2)):
    dif=input_list[i+1]-input_list[i]
    bool=((input_list[i+1]-input_list[i])==(input_list[i+2]-input_list[i+1]))
    truelist.append(bool)
    #print(dif)
#print(truelist)
print(False not in truelist)

