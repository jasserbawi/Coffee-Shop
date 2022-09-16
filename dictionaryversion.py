coffee_menu = {
    'coffee_size':{'small': 2, 'medium': 3, 'large': 4},
    'coffee_type':{'brewed': 0, 'espresso': 0.5, 'cold brew': 1},
    'coffee_flavor':{'yes': 0.5, 'no': 0}
}

while True:
    input_size = input("What coffee size do you want?\n")
    if (input_size.lower() in coffee_menu['coffee_size']) == True:
        break
while True:
    input_type = input("What type of coffee do you want?\n")
    if (input_type.lower() in coffee_menu['coffee_type']) == True:
        break
while True:
    input_flavor = input("Do you want any additional flavours?\n")
    if (input_flavor.lower() in coffee_menu['coffee_flavor']) == True:
        break

def coffee_order(size: str, type: str, flavor: str):
    size_price = coffee_menu['coffee_size'][input_size.lower()]
    type_price = coffee_menu['coffee_type'][input_type.lower()]
    flavor_price = coffee_menu['coffee_flavor'][input_flavor.lower()]

    coffee_price = "%.2f" % round((size_price + type_price + flavor_price),2)

    coffee_price_tip = "%.2f" % round((float(coffee_price)*1.15), 2)

    return f'The price of your coffee is ${coffee_price}, with tip is ${coffee_price_tip}.'
    print(coffee_order())

print(coffee_order(size = input_size, type = input_type, flavor = input_flavor))