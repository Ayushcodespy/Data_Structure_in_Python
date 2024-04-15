
def fibonacci(count):
    if(count<=1):
        return count
    else:
        return fibonacci(count-1) + fibonacci(count-2)
num = int(input("Enter number :"))
fibo = fibonacci(num-1) + fibonacci(num-2)

print(fibo)
