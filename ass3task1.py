def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

num=int(input("enter your number: "))
result=factorial(num)
print(f"the factorial of {num} is {result}")
input('press enter to exit')
