def find_max(x, y, z):

    max = x
    if y > max:
        max = y
    if z > max:
        max = z
    
    print(max)

for _ in range(3):
    print("Please enter 3 numbers: ")
    a = int(input(": "))
    b = int(input(": "))
    c = int(input(": "))
    find_max(a, b, c)

