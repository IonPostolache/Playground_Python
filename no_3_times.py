"""13. Write a Python program to find the single element in a list
where every element appears three times except for one.
Input : [5, 3, 4, 3, 5, 5, 3]
Output : 4"""

input=[5,3,4,3,5,5,3]
print(f"Input: {input}")

for i in input:
    counter=input.count(i)
    if counter==1:
        print(i)

