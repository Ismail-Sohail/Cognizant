def inventory_manager():
    """
    This will create a inventory manager of the fruits
    """

    inventory_fruits = {'apple': (10, 2.5),
                        'banana' : (20, 1.2)
                        }
    
    # prints the current inventory
    print("Current Inventory:")
    display_inventory(inventory_fruits)
    
    # update the inventory
    inventory_fruits['mango'] = (15,3.0)
    print("Updated Inventory:")
    display_inventory(inventory_fruits)

    # calculates the total inventory.
    price = 0
    for item, value in inventory_fruits.items():
        cur_inv = value[0] * value[1]
        price += cur_inv
    
    return f"The value of inventory: {price}"


def display_inventory(fruits_inventory):
    """
    This function takes the dictionary of inventory and displays them.
    """
    for item, value in fruits_inventory.items():
        print(f"Item: {item} , Quantity: {value[0]}, Price: {value[1]}")

if __name__ == '__main__':
    print(inventory_manager())