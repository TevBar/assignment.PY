restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu.setdefault('Starters', {})['Bread Bowl'] = 7.56
restaurant_menu['Steak'] = 17.99
removed_item = restaurant_menu['Starters'].pop('Bruschetta')

#below we are setting the setdefault to assign a new key 'beverages' along with its values. code below

new_item =  new_restaurant = restaurant_menu.setdefault('Beverages', {})
new_restaurant['Dr Pepper'] = 1.25
new_restaurant['Pepsi'] = 1.25

print(restaurant_menu)