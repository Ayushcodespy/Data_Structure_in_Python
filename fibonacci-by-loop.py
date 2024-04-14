num1 = 0
num2 = 1

num = int(input("Enter length of the series :"))
num = num - 2

print(num1)
print(num2)

for x in range(num):
    fibo = num1 + num2

    print(fibo)
    num1 = num2
    num2 = fibo

print("\nFibonacci Series is obtained")