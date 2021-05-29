"""12. Write a Python program to find the single number in a list that doesn't occur twice.
Input : [5, 3, 4, 3, 4]
Output : 5
###
13. Write a Python program to find the single element in a list where every
element appears three times except for one.
Input : [5, 3, 4, 3, 5, 5, 3]
Output : 4
###
14. Write a Python program to find the single element appears once in a list
where every element appears four times except for one.
Input : [1, 1, 1, 1, 2, 2, 2, 2, 3]
Output : 3
###
15. Write a Python program to find two elements appear once in a list where
all the other elements appear exactly twice in the list.
Input : [1, 2, 1, 3, 2, 5]
Output :[5, 3]   """

#This code is working for all the above exercises.
inputlist=[5, 3, 4, 3, 4, 4, 1, 1, 1, 1, 8]
print(f"Input: {inputlist}")
uniquelist=[]

for i in inputlist:
    counter=inputlist.count(i)
    if counter==1:
        uniquelist.append(i)

print(uniquelist)
