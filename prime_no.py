#This function checks the prime numbers within a range
def prime(x,y):
    for a in range(x, y):
        for b in range(x, a):
            if a % b == 0:
                print(a, "is not a prime number,", a,"equals",b,"*",a//b,".")
                break
        else:
            print(f"{a} is a prime number.")

prime(2,22)