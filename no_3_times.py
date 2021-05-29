"""13. Write a Python program to find the single element in a list
where every element appears three times except for one.
Input : [5, 3, 4, 3, 5, 5, 3]
Output : 4"""


inputlist=[5, 3, 4, 3, 5, 5, 3]
print(f"Input: {inputlist}")
#uniquelist=[]

for i in inputlist:
    counter=inputlist.count(i)
    #print(counter)
    if counter==1:
        uniquelist.append(i)
        print(i)

#print(uniquelist)
