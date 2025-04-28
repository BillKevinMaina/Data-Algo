class ShoppingCart:
    def _init_(self):
        self.items = []

    def add_item(self, item_name: str, qty: int, unit_price: float):
        self.item_name = item_name
        self.qty = qty
        self.unit_price = unit_price

        self.items.append((item_name, qty, unit_price))

    def remove_item(self, item_name: str):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)

    def summury(self):
        print("Cart Summury")

        for item_name,Qty, price in self.items:
            print(f"{price}:{Qty}")