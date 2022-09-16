import math

coffee_size = ""
coffee_size_value = 0

while coffee_size != "small" or "medium" or "large":

    coffee_size = input("Do you want small, medium, or large? ")

    if coffee_size.lower() == "small":
        coffee_size_value = 2
        break

    elif coffee_size.lower() == "medium":
        coffee_size_value = 3
        break

    elif coffee_size.lower() == "large":
        coffee_size_value = 4
        break

coffee_type = ""
coffee_type_value = 0

while coffee_type != "brewed" or "espresso" or "cold brew":

    coffee_type = input("Do you want brewed, espresso, or cold brew? ")

    if coffee_type.lower() == "brewed":
        break

    elif coffee_type.lower() == "espresso":
        coffee_type_value = 0.5
        break

    elif coffee_type.lower() == "cold brew":
        coffee_type_value = 1
        break

coffee_flavoring = ""
coffee_flavoring_value = 0

while coffee_flavoring != "yes" or "no":

    coffee_flavoring = input("Do you want flavoring? (yes or no) ")

    if coffee_flavoring.lower() == "yes":
        coffee_flavoring_value = 0.5
        break

    elif coffee_flavoring.lower() == "no":
        break

coffee_cost = round((coffee_size_value + coffee_type_value + coffee_flavoring_value), 2)

print("The cost of your coffee is $" + str(coffee_cost) + ".")

coffee_cost_tip = round((coffee_cost*1.15), 2)
print("The price with a 15% tip is $" + str(coffee_cost_tip))