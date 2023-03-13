
def multiply(x, y):
    var = x
    times = y
    result = 0
    for _ in range(times):
        result = var + result 
    return result

def exponentiate(x, y):
    var = x
    times = y
    result = var
    for _ in range(times - 1):
        result = multiply(result, var)
    return result

def square(x):
    return exponentiate(x, 2)

def main():
    print(multiply(5, 5))
    print(exponentiate(5, 2))
    print(square(5))


main()