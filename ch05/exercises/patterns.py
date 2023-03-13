def star_pyramid(var):
    for var in range(var + 1):
       for x in range(var):
           print("*", end = '')
       print("")
def rstar_pyramid(var):
    for x in range(var):
       for var in range(var):
           print("*", end = '')
       print("")

levels = int(input("Please enter a value: "))
star_pyramid(levels)
rstar_pyramid(levels)