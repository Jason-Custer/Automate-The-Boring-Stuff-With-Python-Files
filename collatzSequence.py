# Collatz Sequence

number = int(input("Enter number: "))

def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = (number * 3) +1

    while result == 1:
        print(result)
        sys.exit()

    while result != 1:
        print(result)
        number = result
        return collatz(number)

collatz(number)
