rate = float(input("Please enter the current Euro to Dollar exchange rate: "))
amount = float(input("Please enter an amount to be exchanged: "))
total = amount*rate
serviceFee = 3.00
result = total - serviceFee
print("Your balance is: $", result, " (accounting for service fees).")
