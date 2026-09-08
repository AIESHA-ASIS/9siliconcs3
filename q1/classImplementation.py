class Weapon:
    def __init__(self, weapon_name: str, quantity: int, price: int, is_available: bool = True):
        self.weapon_name = weapon_name
        self.quantity = quantity
        self.price = price
        self.__is_available = is_available if quantity > 0 else False

    def purchase_item(self, quantity_bought: int):
        if not self.__is_available or self.quantity < quantity_bought:
            print(f"Cannot purchase {quantity_bought} x {self.weapon_name}. Insufficient stock!")
            return
        
        self.quantity -= quantity_bought
        print(f"Successfully purchased {quantity_bought} x {self.weapon_name}(s).")
        
        if self.quantity == 0:
            self.__is_available = False

    def display_info(self):
        if self.__is_available:
            status = "Available" 
        else:
            status ="Out of Stock"
        print(f"Weapon: {self.weapon_name} | Price: {self.price} gold | Stock: {self.quantity} | Status: {status}")

    def check_quantity(self):
        print(f"Current quantity for {self.weapon_name}: {self.quantity}")

    def get_availability(self):
        return self.__is_available


weapon1 = Weapon("Iron Sword", 5, 150)
weapon2 = Weapon("Wooden Bow", 10, 80)

print("=== BEFORE PURCHASE ===")
weapon1.display_info()
weapon2.display_info()

print("\n--- Performing action on Object 1 (Purchasing 5 Iron Swords) ---")
weapon1.purchase_item(5)

print("\n=== AFTER PURCHASE ===")
weapon1.display_info()
weapon2.display_info()