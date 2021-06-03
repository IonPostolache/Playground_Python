"""23. Write a Python program where you take any positive integer n, if n is even,
divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1
to obtain 3n + 1. Repeat the process until you reach 1.
Input : 12
Output : [12, 6.0, 3.0, 10.0, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0]
According to Wikipedia, the Collatz conjecture is a conjecture in mathematics
named after Lothar Collatz, who first proposed it in 1937.
The conjecture is also known as the 3n + 1 conjecture.
The conjecture can be summarized as follows. Take any positive integer n.
If n is even, divide it by 2 to get n / 2. If n is odd, multiply it by 3 and
add 1 to obtain 3n + 1. Repeat the process (which has been called
"Half Or Triple Plus One") indefinitely. The conjecture is that no matter
what number you start with, you will always eventually reach 1.
Example :
For instance, starting with n = 12, one gets the sequence 12, 6, 3, 10, 5, 16, 8, 4, 2, 1.
n = 19, for example, takes longer to reach 1: 19, 58, 29, 88, 44, 22, 11,
34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.     """

number=int(input("What is the number? > "))
result=number
outputlist=[]

while result>=1:
    outputlist.append(result)
    if result==1:
        break
    if result%2==0:
        divided=result/2
        result=divided
        continue
    elif result%2!=0:
        multiplied=(result*3)+1
        result=multiplied
        continue
    if result<1:
        break

print(outputlist)

