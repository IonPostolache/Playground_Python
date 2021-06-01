""" 21. Write a Python program to check a sequence of numbers is a geometric progression or not.
Input : [2, 6, 18, 54]
Output : True
In mathematics, a geometric progression or geometric sequence is a sequence of numbers
where each term after the first is found by multiplying the previous one by a fixed,
non-zero number called the common ratio.
For example, the sequence 2, 6, 18, 54, ... is a geometric progression with common
ratio 3. Similarly, 10, 5, 2.5, 1.25, ... is a geometric sequence with common ratio 1/2.    """

def geom_progression(n):
    commonr=n[1]/n[0]
    for i in range(0, (len(n)-1)):
        if not n[(i+1)]/n[i]==commonr:
            return False
    return True

print(geom_progression([2,6,18,54]))
print(geom_progression([10, 5, 2.5, 1.25]))
print(geom_progression([2,6,18,55]))

