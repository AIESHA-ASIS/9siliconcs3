# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](q1/classObjectUML.md)
[Part II - Class Attributes and Methods](q1/classAttributesMethods.md)

## Existing Class
Class: Weapon
Description: A weapon is a defense item that the character will be using in the game to protect themselves from opponents.

## New Related Class
Class: Power up
Description: A powerup a unique ability given to the player's weapon to further improve its quality or performance.

## Association
Relationship: A weapon can utilize many weapon powerups 
Explanation: When a weapon is purchased, it starts off ordinary and basic without any quirks. Once powerups are utilized, it makes the weapon more convenient and unique.

## Multiplicity
Multiplicity: One-to-Many
Explanation: This multiplicity fits my system because one-to-many multiplicity means that an object one side can be linked to many objects on the other side but can be only linked back to that specific object. In relation to the system, it means explains that one weapon can be linked to many powerups but those powerups can only be linked back to that weapon because of specficity.

## UML Class Relationship Diagram
![Class Relationship Diagram]<img width="172" height="692" alt="images-classRelationshipDiagram drawio (1)" src="https://github.com/user-attachments/assets/3043b03c-7420-43d1-aa2c-a053adeb45dd" />

## Python Implementation
[View Python Source](q1/classRelationship.py)

## Test Run
![Relationship Test Run]<img width="1913" height="876" alt="images-relationshipTestRun" src="https://github.com/user-attachments/assets/b1513032-f390-4a50-8035-8c0a6aa34148" />

## Object Relationship Diagram
![Object Relationship Diagram]<img width="310" height="238" alt="images-objectRelationshipDiagram drawio" src="https://github.com/user-attachments/assets/81c50f29-3f14-4605-8a40-0b55a35156da" />


## Analysis
### What is the association between your two classes?
-In the system, weapon can utilize many powerups. Due to specificity for some weapons, not all powerups can be used on different weapons. This shows that ONE weapon can utilize MANY powerups, but the powerups can only be joined back to specifically that weapon it is linked to.
### What multiplicity did you choose and why?
- I chose the 'one-to-many' multiplicity because it fits my system best. This multiplicity fits my system because one-to-many multiplicity means that an object one side can be linked to many objects on the other side but can be only linked back to that specific object. In relation to the system, it means explains that one weapon can be linked to many powerups but those powerups can only be linked back to that weapon because of specficity.
### How did you implement the relationship in Python?
-I Implemented the relationship through the manner of using an attribute that will contain the powerups, linking objects through aggregation, and delegating actions. As the __init__, a list is created to store the powerups/the powerup object. Linking object through aggression is applied as the add_powerup method adds powerups to the Weapon's list of utilized powerups. To simply explain, delegating actions means 'to pass the job to someone who knows how to do it' which is applied when Weapon_display.info() loops over its list of power ups and passses the job to the p.displayinfo() to print the info on each item.
### Why did you store an object reference instead of copying its data?
-It's because the weapon will instantly see the change in stock's stats without needing to fix outdated copies whenever there's updated information. Secondly, it saves computer memory as it is stored in an existing object. Lastly, it can also allows the object to run built-in-methods instead of just storing data.
### If your relationship uses many, why is a list appropriate?  
-Its because using a list makes the code more cleaner. As a list is used, it makes the code more organized instead having to store the data line by line. In addition, it also supports the chosen mutiplicity, naturally accommodating an array of items. Because we use a list, it can also preserve the order of the item, meaning that whatever order of data is inputted, it will also be displayed in the same order when printed.
