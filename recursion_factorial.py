#  recursion_factorial function takes an argument and returns factorial of an argument

def recursion_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursion_factorial(n - 1)
    

print(recursion_factorial(5))
