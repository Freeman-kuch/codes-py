#! Python 3
# List to Dictionary Function for Fantasy Game Inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = {'gold coin': 42, 'rope': 1}


def addToInventory(inventory, addedItems):
    sorted(dragonLoot)
    for idx, loots in enumerate(dragonLoot):
        inventory.setdefault(loots, 0)
        inventory[loots] += 1
    return inventory


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total = item_total + v
    print("Total number of items: " + str(item_total))



inv = addToInventory(inventory, dragonLoot)
displayInventory(inv)