class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        
    def get_name(self): 
        return self.name
        
    def get_price(self): 
        return self.price
        
    def get_weight(self): 
        return self.weight
        
    def get_cost(self): 
        return self.price / self.weight

def knapsack(itemList, amount):
    n = len(itemList)
    for i in range(n):
        for j in range(0, n - i - 1):
            if itemList[j].get_cost() < itemList[j + 1].get_cost():
                itemList[j], itemList[j + 1] = itemList[j + 1], itemList[j]

    print(f"Knapsack Size: {float(amount)} kg")
    print("===============================")
    
    total_price = 0
    
    for item in itemList:
        if item.get_weight() <= amount:
            print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")
            total_price += item.get_price()
            amount -= item.get_weight()
            
    print(f"Total: {total_price} THB")

def main():
  import json
  items = []
  num_items = int(input())
  while num_items != 0:
    item_in = json.loads(input())
    items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
    num_items = num_items - 1
  knapsack_capacity = float(input())
  knapsack(items, knapsack_capacity)

main()