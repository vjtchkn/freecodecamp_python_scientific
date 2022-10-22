import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print("Food after withdrawal:", food.get_balance())
food.withdraw(1000)
print("Food after overdrawal:", food.get_balance())

clothing = budget.Category("Clothing")
food.transfer(50, clothing)
print("Food after transfer:", food.get_balance())
print("Clothing after transfer:", clothing.get_balance())
clothing.withdraw(25.55)
print("Clothing after withdrawal:", clothing.get_balance())
clothing.withdraw(100)
print("Clothing after overdrawal:", clothing.get_balance())

auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print("Auto after withdrawal:", auto.get_balance())

print(food)
print(clothing)

print(create_spend_chart([clothing, auto, food]))

# Run unit tests automatically
main(module="test_module", exit=False)
