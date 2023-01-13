import sys
import os


def prime(s):
   
    if s < 2:
        return False
    for i in range(2,s):
        if s % i == 0:
            return False
    else: 
        return True      

no = int(input("Enter a number\n>>: "))
if prime(no):
    print(prime(no))
    print(no, "is prime")
else:
    print(prime(no))
    print(no, "isn't prime")

def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))