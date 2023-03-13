

num1 = int(input("Please enter an upper limit:"))
for _ in range(num1 + 1):
    print(_)
    if _ % 3 == 0 and _ % 5 == 0:
     print("fizzbuzz")
    elif _ % 3 == 0:
        print("fizz")
    elif _ % 5 == 0:
       print("buzz")

