from data import *


def prompt():
    return input("What would you like? (espresso, latte, cappuccino): ")


def printReport(ingredients, money):
    print(f"Water: {ingredients['water']}ml")
    print(f"Milk: {ingredients['milk']}ml")
    print(f"Coffee: {ingredients['coffee']}g")
    print(f"Money: ${money}")


def checkResources(coffee, ingredients):
    isWater = ingredients["water"] > coffee["ingredients"]["water"]
    isMilk = ingredients["milk"] > coffee["ingredients"]["milk"]
    isCoffee = ingredients["coffee"] > coffee["ingredients"]["coffee"]
    if not isWater or not isMilk or not isCoffee:

        if not isWater and not isMilk and not isCoffee:
            print("Sorry there is not enough water, milk and coffee.")
        elif not isWater and not isMilk:
            print("Sorry there is not enough water and milk.")
        elif not isMilk and not isCoffee:
            print("Sorry there is not enough milk and coffee.")
        elif not isWater and not isCoffee:
            print("Sorry there is not enough water and coffee.")
        else:
            if not isWater:
                print(f"Sorry there is not enough water.")
            if not isMilk:
                print(f"Sorry there is not enough milk.")
            if not isCoffee:
                print(f"Sorry there is not enough coffee.")

        return False
    else:
        return True


def processTransaction(coffee, ingredients):
    print("Please insert coins.")

    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickles = int(input("How many nickels? : "))
    pennies = int(input("How many pennies? : "))

    totalDollars = ((25 * quarters) + (10 * dimes) + (5 * nickles) + pennies) / 100;

    if totalDollars < coffee["cost"]:
        print("Sorry that's not enough money. Money refunded")
    elif totalDollars >= coffee["cost"]:
        ingredients["water"] = ingredients["water"] - coffee["ingredients"]["water"]
        ingredients["milk"] = ingredients["milk"] - coffee["ingredients"]["milk"]
        ingredients["coffee"] = ingredients["coffee"] - coffee["ingredients"]["coffee"]

        if totalDollars > coffee["cost"]:
            print(f"Here is ${totalDollars - coffee['cost']} in change.")
        print("Here is your espresso ☕️...Enjoy!")
        return coffee["cost"]

    return 0


def transaction(coffee, ingredients, money):
    if checkResources(coffee, ingredients):
        return processTransaction(coffee, ingredients)
    return 0


def coffeeMachine():
    ingredients = resources
    money = 0

    option = 'on'

    while True:
        option = prompt()

        if option == 'off':
            return
        elif option == 'report':
            printReport(ingredients, money)
        else:
            coffee = MENU[option]
            money += transaction(coffee, ingredients, money)


coffeeMachine()
