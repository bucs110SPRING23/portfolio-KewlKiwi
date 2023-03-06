def star_pyramid():
    var = int(input("Please enter a value: "))
    for var in range(var + 1):
       for x in range(var):
           print("*", end = '')
       print("")
def rstar_pyramid():
    var = int(input("Please enter a value: "))
    for x in range(var):
       for var in range(var):
           print("*", end = '')
       print("")

star_pyramid()
rstar_pyramid()