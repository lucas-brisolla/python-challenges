def factorNumber(n):
    if n == 1:
        return 1
    else:
        return n * factorNumber(n-1)

num = int(input("Type a number: "))
result = factorNumber(num)
print(f"The {num} factored is {result}")
