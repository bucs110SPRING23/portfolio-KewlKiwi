import random
#def find_max(x, y, z):
#
#    max = x
#    if y > max:
#        max = y
#    if z > max:
#        max = z
    
#    print(max)

#for _ in range(3):
#    print("Please enter 3 numbers: ")
#    a = int(input(": "))
#    b = int(input(": "))
#    c = int(input(": "))
#    find_max(a, b, c)

#def foo(x, y, z):
#    print(x, y, z)

#foo(1, 2, 3)

#def bar(x=0, y=2, z=3):
#    print(x, y, z)

#bar(z=1, x=2)

#def foo():
#    local_var = 5 #local scope
#    x = 2 #deleted when function ends, parameters are local variables

#global_var = 5 #global scope

#f(x) = y     functions muct return a value

#def bar(x=None):
#    if x is None:
#        x = 5*2


def foo():
    x = 5
    return [x, 6]
    print("This will never print")

#y, z = foo()
#print(y, z)

def my_func(x=0):
    return x + x

#my_func(5)

def powerof(x=0, p=0):
   power = p
   y = x**power
   return y

power = 2
result = powerof(5, 3)
#print(result)

def foo2(x):
    return x*2

#nested functions execute from the inside out
print("2", foo2(abs(random.randint(1, 100))))


#global variable issues:
#name collisions, global variables never leave memory
var = 1

def start():
    print(var)

def main():    #starts on main function, everything in global scope should go in main (elimiates global scope)
    print(var)


#only thing in global space is call to main - at the end of the program
main()
