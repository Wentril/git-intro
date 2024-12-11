print("Hello world")

print("Hi")


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# function to add two numbers
def add(a, b):
    return a + b


# function to subtract two numbers
def subtract(a, b):
    return a - b


if __name__ == "__main__":
    print(factorial(5))
    print(add(2, 3))
    print(subtract(5, 2))