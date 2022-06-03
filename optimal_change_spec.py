# Write your tests here!
from optimal_change import optimal_change as calc


print("1:", calc(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

print("2:", calc(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

# Custom tests
print("3:", calc(21.99, 100) == "The optimal change for an item that costs $21.99 with an amount paid of $100 is 1 $50 bill, 1 $20 bill, 1 $5 bill, 3 $1 bills, and 1 penny.")
print("4:", calc(75.38, 200) == "The optimal change for an item that costs $75.38 with an amount paid of $200 is 1 $100 bill, 1 $20 bill, 4 $1 bills, 2 quarters, 1 dime, and 2 pennies.")
print("5:", calc(98.76, 100) == "The optimal change for an item that costs $98.76 with an amount paid of $100 is 1 $1 bill, 2 dimes, and 4 pennies.")
print("6:", calc(0.29, 1) == "The optimal change for an item that costs $0.29 with an amount paid of $1 is 2 quarters, 2 dimes, and 1 penny.")
print("7:", calc(4.55, 5) == "The optimal change for an item that costs $4.55 with an amount paid of $5 is 1 quarter, and 2 dimes.")
print("8:", calc(4.99, 5) == "The optimal change for an item that costs $4.99 with an amount paid of $5 is 1 penny.")
print("9:", calc(5, 5) == "No change due.")
print("10:", calc(6, 5) == "You owe $1")
