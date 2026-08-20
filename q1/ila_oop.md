
# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation groups the data and methods into a single 'Product' object which cant be directly accessible to properties like 'price' and 'quantity' with the help of private modifiers. Through methods like 'sellItem()' or 'restock(), controlled updates can occur which prevents errors like negative inventory counts.

### 2. Abstraction
Abstraction hides the complex background processes but displays the simpler actions/results such as an 'checkout()' method in an 'InventoryManager` class. Using abstraction, it helps the system to process sales without having to display the calculation process.

### 3. Inheritance
Inheritance allows specific items to acquire the properties or methods of a parent object like ('name','price') from 'Product'. This eliminates duplicates in the code and makes adding new items more efficient. 

### 4. Polymorphism
Polymorphism allows different products to use the same 'displayinfo()' command while executing their own individual functions. The inventory list can display expiration warning for milk and bundle deals/discounts for shampoo using a single loop.

## Reflection
With the help of OOP, it organizes software design around data or "objects" which helps make the code look more organized, readable, and easier to expand. If I were to choose among the four pillars of Object-Oriented-Programming that I believe would help further improve the sari-sari system, it would be Encapsulation. Encapsulation helps improve the sari-sari store program because it helps contribute to locking product data like price and quantity inside a secure 'Product' object which could help prevent accidental production or negative stock counts. Using controlled methods like sellitem() gurantees that the inventory numbers stay accurate and never drop below zero.
