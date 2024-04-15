num1 = 0
num2 = 1

num = int(input("Enter length of the series :"))
count = num - 2

def default():
    print(num1)
    print(num2)

def fibbonacci():
    global num1, num2, count
    fibo = num1 + num2
    print(fibo)

    num1 = num2
    num2 = fibo

    count -= 1
    if(count>0):
        fibbonacci()
    else:
        print("\nFibonacci series obtained")

if(count>0):
    default()
    fibbonacci()

else:
    print("Enter number more than 2")