"""12. Write a Python program to find the single number in a list that doesn't occur twice.
Input : [5, 3, 4, 3, 4]
Output : 5   """

inputlist=[5, 3, 4, 3, 4]
print(f"Input: {inputlist}")
#uniquelist=[]

for i in inputlist:
    counter=inputlist.count(i)
    #print(counter)
    if counter==1:
        #uniquelist.append(i)
        print(i)

#print(uniquelist)
