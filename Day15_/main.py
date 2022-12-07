# Basic coffee machine project
from data import resources, MENU, art
import os
profit = 0


def total_money():
    total = 0.25*int(input("Enter the number of quarters: "))
    total += 0.10*int(input("Enter the number of dimes: "))
    total += 0.05*int(input("Enter the number of nickles: "))
    total += 0.01*int(input("Enter the number of pennies: "))
    return total


def ingredients_are_enough(req_ingredients, available_ingredients):
    for key in req_ingredients:
        if req_ingredients[key] > available_ingredients[key]:
            return False
    return True


def make_dish(choice, resources):
    req_ingredients = MENU[choice]["ingredients"]
    if ingredients_are_enough(req_ingredients, resources):
        print(f"Here is your {choice} ☕ ☕ ")
        global profit
        profit += MENU[choice]["cost"]
        return True
    else:
        print(f"Sorry ingredients are not enough for the order.\nMoney refunded")
        return False


def calc_change(paid, order):
    to_be_paid = MENU[order]["cost"]
    if paid >= to_be_paid:
        print(f"to_be_paid:{to_be_paid}, paid:{paid}")
        print("Here is your change: $", round(paid-to_be_paid, 2))
        return True
    else:
        print(f"to_be_paid:{to_be_paid}, paid:{paid}")
        print("Not enough money for order. Money refunded")
        return False


def update_resources(resources, used):
    resources["water"] -= used["water"]
    resources["coffee"] -= used["coffee"]
    if "milk" in used.keys():
        resources["milk"] -= used["milk"]
    return resources


print(art)
loop_again = True
while loop_again:
    order = input("what would you like? (espresso/latte/cappuccino) : ")
    if order == "off":
        loop_again = False
    elif order == 'cls':
        os.system('cls')
        print(art)
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        total = total_money()
        if calc_change(total, order):
            if make_dish(order, resources):
                resources = update_resources(
                    resources, MENU[order]["ingredients"])
    else:
        print("Wrong choice....Please select again")
