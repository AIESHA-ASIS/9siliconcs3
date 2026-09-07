# SG4 - Understanding Classes and Objects
## Weapon/tool
## A weapon is a defense item that the character will be using in the game to protect themselves from opponents.

## Properties
| Property | Data Type | Description |
|---|---|---|
|Weapon name|string|Name of weapon|
|Quantity|int|Amount to be purchased|    
|Price|int|Cost of the weapon|
|Availablity|boolean|Determines whether the desired object is available for purchase|
## Methods
| Method | Description |
|---|---|
|PurchaseItem(item)|This method allows the user to purchase the item of their choice|
|DisplayInfo()|This method displays the info of the item/s  |
|CheckQuantity(item)|This method displays the number of the desired object is avaialable for purchase|
## Class Diagram
<img width="172" height="282" alt="classdiagram drawio (1)" src="https://github.com/user-attachments/assets/c66dd1e3-7529-472a-8f32-dd0ca2720d81" />

## Design Explanation
### Why did you choose this class?
- I chose this class because it is common in games for a character to purchase/have an weapon, object, and tool
### Which property is the most important? Why?
- The name of the object is significant as it can serve as the very first identity or impression of the item so players can have an idea of what weapon they're checking out.
### Which method is the most useful? Why?
- PurchaseItem(item), because it allows the user purchase the weapon they need for the battle they're preparing for or for convenience.
