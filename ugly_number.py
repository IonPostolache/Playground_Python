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
prime_factors=[2,3,5]

def divide(n_check, primef):
    result=n_check/primef
    print(f"the number {n_check} was divided by {primef} and the result is {result}")
    return result

for i in prime_factors:
    if number%i==0:
        extract=divide(number,i)
        print(extract)
        print(type(extract))
        #the next if needs to be in a while loop to run as many times as neccesary
        #after that we need to check the other factor
        #if number/extract in prime_factors:
            #print("the number is ugly")----this should be the final decision
        if extract%i==0:
            extract2=divide(extract,i)
            print(extract2)
            if extract2!=2 and extract2!=3 and extract2!=5:
                print("the number is not ugly")
            else:
                print("the number is ugly")
        else:
            print(f"the number is not ugly")
    else:
        print(f"the number is not ugly")

