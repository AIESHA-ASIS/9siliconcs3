# advancedRelationships.py

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


class Blade:
    def __init__(self, material: str = "Strong Iron", sharpness: int = 90):
        self.material = material
        self.sharpness = sharpness

    def display_info(self):
        print(f"  Blade Material: {self.material} | Sharpness: {self.sharpness}%")


class Weapon:
    def __init__(self, weapon_name: str, quantity: int, price: int, is_available: bool = True):
        self.weapon_name = weapon_name
        self.quantity = quantity
        self.price = price
        self.__is_available = is_available if quantity > 0 else False
        self.powerups = []

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
            print("UTILIZED POWERUPS:")
            for p in self.powerups:
                p.display_info()

    def check_quantity(self, item: int):
        print(f"Current quantity for {self.weapon_name}: {self.quantity}")

    def get_availability(self):
        return self.__is_available


class IronSword(Weapon):
    def __init__(self, weapon_name: str, quantity: int, price: int, block_power: int = 25, is_available: bool = True):
        super().__init__(weapon_name, quantity, price, is_available)
        self.block_power = block_power
        self.blade = Blade()

    def display_info(self):
        super().display_info()
        print(f"  Sword Block Power: {self.block_power}")
        self.blade.display_info()


if __name__ == "__main__":
    weapon_rel = IronSword("Iron Sword", 5, 150)
    p1 = Powerup("Fire Enchantment", 3, 50)
    p2 = Powerup("Lifesteal Gem", 2, 80)

    weapon_rel.add_powerup(p1)
    weapon_rel.add_powerup(p2)
    weapon_rel.display_info()
    weapon_rel.purchase_item(2)
    weapon_rel.display_info()