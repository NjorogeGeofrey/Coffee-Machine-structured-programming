MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
machine_on = True
while machine_on:


    # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
    Money = {
        "quarters" : 0.25,
        "dimes" : 0.10,
        "nickles" : 0.05,
        "pennies" : 0.01,
    }


    def espresso():
        Data = MENU["espresso"]
        Ingredients = Data["ingredients"]
        Water = Ingredients["water"]
        Coffee = Ingredients["coffee"]
        Cost = Data["cost"]
        return([Water, Coffee, Cost])


    def latte_cappuccino (drink):
        Data = MENU[drink]
        Ingredients = Data["ingredients"]
        Water = Ingredients["water"]
        Milk = Ingredients["milk"]
        Coffee = Ingredients["coffee"]
        Cost = Data["cost"]
        return([Water, Milk, Coffee, Cost])


    def report():
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")



    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if answer == "espresso":
        Drink1 = espresso()
        if Drink1[0] > resources["water"]:
            print(f" Unfortunately there is no enough water to make your espresso")
        elif Drink1[1] > resources["coffee"]:
            print(f"Unfortunately there is no enough coffee to make your espresso")
        elif Drink1[0] <= resources["water"] and Drink1[1] <= resources["coffee"]:

            print("Please insert coins. ")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            money_put_in = (quarters * Money["quarters"]) + (dimes * Money["dimes"]) + (nickles * Money["nickles"]) + (
                    pennies * Money["pennies"])
            if Drink1[-1] > money_put_in:
                print(
                    f"That's not enough. An espresso costs ${Drink1[-1]} and the amount you have entered is {money_put_in}")
            elif money_put_in > Drink1[-1]:
                change = money_put_in - Drink1[-1]
                print(f"Here is ${round(change, 2)}  in change")
                print("Here is your espresso ☕Enjoy!")
                resources["water"] = resources["water"] - Drink1[0]
                resources["coffee"] = resources["coffee"] - Drink1[1]
                resources["money"] = resources["money"] + Drink1[-1]


    elif answer == "latte":
        Drink2 = latte_cappuccino(answer)
        if Drink2[0] > resources["water"]:
            print(f" Unfortunately there is no enough water to make your latte")
        elif Drink2[1] > resources["milk"]:
            print(f"Unfortunately there is no enough milk to make your latte")
        elif Drink2[2] > resources["coffee"]:
            print(f"Unfortunately there is no enough coffee to make your latte")
        elif Drink2[0] < resources["water"] and Drink2[1] < resources["milk"] and Drink2[2] < resources["coffee"]:

            print("Please insert coins. ")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            money_put_in = (quarters * Money["quarters"]) + (dimes * Money["dimes"]) + (nickles * Money["nickles"]) + (
                    pennies * Money["pennies"])

            if Drink2[-1] > money_put_in:
                print(
                    f"That's not enough. An latte costs ${Drink2[-1]} and the amount you have entered is {money_put_in}")
            elif money_put_in > Drink2[-1]:
                change = money_put_in - Drink2[-1]
                print(f"Here is ${round(change, 2)}  in change")
                print("Here is your latte ☕Enjoy!")
                resources["water"] = resources["water"] - Drink2[0]
                resources["milk"] = resources["milk"] - Drink2[1]
                resources["coffee"] = resources["coffee"] - Drink2[2]
                resources["money"] = resources["money"] + Drink2[-1]


    elif answer == "cappuccino":
        Drink3 = latte_cappuccino(answer)

        if Drink3[0] > resources["water"]:
            print(f" Unfortunately there is no enough water to make your cappuccino")
        elif Drink3[1] > resources["milk"]:
            print(f"Unfortunately there is no enough milk to make your cappuccino")
        elif Drink3[2] > resources["coffee"]:
            print(f"Unfortunately there is no enough coffee to make your cappuccino")
        elif Drink3[0] < resources["water"] and Drink3[1] < resources["milk"] and Drink3[2] < resources["coffee"]:
            print("Please insert coins. ")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            money_put_in = (quarters * Money["quarters"]) + (dimes * Money["dimes"]) + (nickles * Money["nickles"]) + (
                        pennies * Money["pennies"])

            if Drink3[-1] > money_put_in:
                print(
                    f"That's not enough. An cappuccino costs ${Drink3[-1]} and the amount you have entered is {money_put_in}")
            elif money_put_in > Drink3[-1]:
                change = money_put_in - Drink3[-1]
                print(f"Here is ${round(change, 2)}  in change")
                resources["water"] = resources["water"] - Drink3[0]
                resources["milk"] = resources["milk"] - Drink3[1]
                resources["coffee"] = resources["coffee"] - Drink3[2]
                resources["money"] = resources["money"] + Drink3[-1]
                print("Here is your cappuccino ☕Enjoy!")


    elif answer == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")


    machine = input("Did you want to place an order? Type 'y' to place an order 'n' to turn off the machine: ").lower()
    if machine == 'n':
        machine_on = False


