class Weapon:
    def __init__(self, weapon_name: str, quantity: int, price: int, is_available: bool = True):
        self.weapon_name = weapon_name
        self.quantity = quantity
        self.price = price
        self.__is_available = is_available if quantity > 0 else False

    def PurchaseItem(self, quantity_bought: int):
        if not self.__is_available or self.quantity < quantity_bought:
            print(f"Cannot purchase {quantity_bought} x {self.weapon_name}. Insufficient stock!")
            return
        
        self.quantity -= quantity_bought
        print(f"Successfully purchased {quantity_bought} x {self.weapon_name}(s).")
        
        if self.quantity == 0:
            self.__is_available = False

    def DisplayInfo(self):
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
weapon1.DisplayInfo()
weapon2.DisplayInfo()

print("\n--- Performing action on Object 1 (Purchasing 5 Iron Swords) ---")
weapon1.PurchaseItem(5)

print("\n=== AFTER PURCHASE ===")
weapon1.DisplayInfo()
weapon2.DisplayInfo()


class Powerup:
  class Powerup:
    def __init__(self, power_up_name: str, quantity: int, price: int, is_available: bool = True):
        self.power_up_name = power_up_name
        self.quantity = quantity
        self.price = price
        self.__is_available = is_available if quantity > 0 else False

    def purchase_powerup(self, power_up: int):
        if not self.__is_available or self.quantity < power_up:
            print(f"Cannot purchase {power_up} x {self.power_up_name}. Insufficient stock!")
            return
        self.quantity -= power_up
        print(f"Successfully purchased {power_up} x {self.power_up_name}(s).")
        if self.quantity == 0:
            self.__is_available = False

    def display_info(self):
        status = "Available" if self.__is_available else "Out of Stock"
        print(f"  Powerup: {self.power_up_name} | Price: {self.price} gold | Stock: {self.quantity} | Status: {status}")

    def check_quantity(self, power_up: int):
        print(f"Current quantity for {self.power_up_name}: {self.quantity}")


class WeaponPowerup:
  class Powerup:
    def __init__(self, power_up_name: str, quantity: int, price: int, is_available: bool = True):
        self.power_up_name = power_up_name
        self.quantity = quantity
        self.price = price
        self.__is_available = is_available if quantity > 0 else False

    def purchase_powerup(self, power_up: int):
        if not self.__is_available or self.quantity < power_up:
            print(f"Cannot purchase {power_up} x {self.power_up_name}. Insufficient stock!")
            return
        self.quantity -= power_up
        print(f"Successfully purchased {power_up} x {self.power_up_name}(s).")
        if self.quantity == 0:
            self.__is_available = False

    def display_info(self):
        status = "Available" if self.__is_available else "Out of Stock"
        print(f"  Powerup: {self.power_up_name} | Price: {self.price} gold | Stock: {self.quantity} | Status: {status}")

    def check_quantity(self, power_up: int):
        print(f"Current quantity for {self.power_up_name}: {self.quantity}")


class Weapon:
  class Powerup:
    def __init__(self, power_up_name: str, quantity: int, price: int, is_available: bool = True):
        self.power_up_name = power_up_name
        self.quantity = quantity
        self.price = price
        self.__is_available = is_available if quantity > 0 else False

    def purchase_powerup(self, power_up: int):
        if not self.__is_available or self.quantity < power_up:
            print(f"Cannot purchase {power_up} x {self.power_up_name}. Insufficient stock!")
            return
        self.quantity -= power_up
        print(f"Successfully purchased {power_up} x {self.power_up_name}(s).")
        if self.quantity == 0:
            self.__is_available = False

    def display_info(self):
        status = "Available" if self.__is_available else "Out of Stock"
        print(f"  Powerup: {self.power_up_name} | Price: {self.price} gold | Stock: {self.quantity} | Status: {status}")

    def check_quantity(self, power_up: int):
        print(f"Current quantity for {self.power_up_name}: {self.quantity}")


class Powerup:
    def __init__(self, power_up_name: str, quantity: int, price: int, is_available: bool = True):
        self.power_up_name = power_up_name
        self.quantity = quantity
        self.price = price
        self.__is_available = is_available if quantity > 0 else False

    def purchase_powerup(self, power_up: int):
        if not self.__is_available or self.quantity < power_up:
            print(f"Cannot purchase {power_up} x {self.power_up_name}. Insufficient stock!")
            return
        self.quantity -= power_up
        print(f"Successfully purchased {power_up} x {self.power_up_name}(s).")
        if self.quantity == 0:
            self.__is_available = False

    def display_info(self):
        status = "Available" if self.__is_available else "Out of Stock"
        print(f"  Powerup: {self.power_up_name} | Price: {self.price} gold | Stock: {self.quantity} | Status: {status}")

    def check_quantity(self, power_up: int):
        print(f"Current quantity for {self.power_up_name}: {self.quantity}")


class WeaponPowerup:
    def __init__(self, power_up_name: str, quantity: int, price: int, is_available: bool = True):
        self.power_up_name = power_up_name
        self.quantity = quantity
        self.price = price
        self.__is_available = is_available if quantity > 0 else False

    def purchase_powerup(self, power_up: int):
        if not self.__is_available or self.quantity < power_up:
            print(f"Cannot purchase {power_up} x {self.power_up_name}. Insufficient stock!")
            return
        self.quantity -= power_up
        print(f"Successfully purchased {power_up} x {self.power_up_name}(s).")
        if self.quantity == 0:
            self.__is_available = False

    def display_info(self):
        status = "Available" if self.__is_available else "Out of Stock"
        print(f"  Powerup: {self.power_up_name} | Price: {self.price} gold | Stock: {self.quantity} | Status: {status}")

    def check_quantity(self, power_up: int):
        print(f"Current quantity for {self.power_up_name}: {self.quantity}")


class Weapon:
    def __init__(self, weapon_name: str, quantity: int, price: int, is_available: bool = True):
        self.weapon_name = weapon_name
        self.quantity = quantity
        self.price = price
        self.__is_available = is_available if quantity > 0 else False
        self.powerups = []  # Stores Powerup object references (1-to-many relationship)

    def add_powerup(self, powerup: Powerup):
        self.powerups.append(powerup)

    def purchase_item(self, item: int):
        if not self.__is_available or self.quantity < item:
            print(f"Cannot purchase {item} x {self.weapon_name}. Insufficient stock!")
            return
        self.quantity -= item
        print(f"Successfully purchased {item} x {self.weapon_name}(s).")
        if self.quantity == 0:
            self.__is_available = False

    def display_info(self):
        status = "Available" if self.__is_available else "Out of Stock"
        print(f"Weapon: {self.weapon_name} | Price: {self.price} gold | Stock: {self.quantity} | Status: {status}")
        if self.powerups:
            print("Utilized Powerups:")
            for p in self.powerups:
                p.display_info()

    def check_quantity(self, item: int):
        print(f"Current quantity for {self.weapon_name}: {self.quantity}")

print("\n--- BEFORE RELATIONSHIP ---")
weapon_rel = Weapon("Iron Sword", 5, 150)
p1 = Powerup("Fire Enchantment", 3, 50)
p2 = Powerup("Lifesteal Gem", 2, 80)

weapon_rel.display_info()

print("\n--- BUILDING RELATIONSHIP ---")
weapon_rel.add_powerup(p1)
weapon_rel.add_powerup(p2)
print(f"Added powerups to {weapon_rel.weapon_name} successfully.")

print("\n--- AFTER RELATIONSHIP ---")
weapon_rel.display_info()