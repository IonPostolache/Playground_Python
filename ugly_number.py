"""24. Write a Python program to check whether a given number is an ugly number.
Input : 12
Output : True
Ugly numbers are positive numbers whose only prime factors are 2, 3 or 5.
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ... shows the first 10 ugly numbers.
7, 11 and 13 are not ugly numbers as their prime factors are other than 2, 3 and 5.
The number 14 is not ugly because in its prime factor the 7 will come.
Note: 1 is typically treated as an ugly number
24.1. Given a number n, the task is to find n’th Ugly number."""

number=int(input("what is the number: "))
prime_factors=[2,3,5]

def main():
    number1=number
    if number == 1 or number in prime_factors:
        print(1 == True)
        return
    flag=True
    while flag:
        if number1%2==0:
            result = number1 / 2
            if result in prime_factors:
                print(result in prime_factors)
                return
            number1=result
        elif number1 % 3 == 0:
            result = number1 / 3
            if result in prime_factors:
                print(result in prime_factors)
                return
            number1=result
        elif number1%5==0:
            result=number1/5
            if result in prime_factors:
                print(result in prime_factors)
                return
            number1=result
        else:
            print(number1 in prime_factors)
            return
            #flag=False

main()