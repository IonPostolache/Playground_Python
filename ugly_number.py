"""24. Write a Python program to check whether a given number is an ugly number.
Input : 12
Output : True
Ugly numbers are positive numbers whose only prime factors are 2, 3 or 5.
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ... shows the first 10 ugly numbers.
7, 11 and 13 are not ugly numbers as their prime factors are other than 2, 3 and 5.
The number 14 is not ugly because in its prime factor the 7 will come.
Note: 1 is typically treated as an ugly number
24.1. Given a number n, the task is to find n’th Ugly number."""

number=int(input("what is the number: > "))
print(number)

if number%2==0:
    result=number/2
    print(result)
    if result%2==0:
        continue
