"""You input a number and the function created checks whether
 the number belongs to the Fibonacci sequence or not.
info: In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence,
 called the Fibonacci sequence, such that each number is the sum of the
 two preceding ones, starting from 0 and 1. That is,
F_{0}=0, F_{1}=1, and F_{n}=F_{n-1}+F_{n-2}} for n > 1.
The beginning of the sequence is thus: 0,1,1,2,3,5,8,13,21,34,55..."""

seq=[]
F0,F1=0,1
number=int(input("What number you want to check? > "))
while F1<=number:
    F0, F1=F1,F0+F1
    seq.append(F1)

print(seq)

if number in seq:
    print("Answer: Yes, the number belongs to the Fibonacci sequence.")
else:
    print("Answer: No, the number doesn't belong to the Fibonacci sequence.")
