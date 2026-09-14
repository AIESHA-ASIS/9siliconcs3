# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](q1/classObjectUML.md)
[Part II - Class Attributes and Methods](q1/classAttributesMethods.md)
## Existing Class
Class: Weapon
Description: A weapon is a defense item that the character will be using in the game to protect themselves from opponents.
## New Related Class
Class: Weapon quirk
Description: A weapon quirk is a unique ability given to the player's weapon to further improve its quality or performance.
## Association
Relationship: A weapon can utilize many weapon quirk/powerups 
Explanation: A weapon can use up to many powerups like a sword that can utilize both the sharpness and damage power up to make defeating opponents more easier.
## Multiplicity
One-to-Many
- This multiplicity fits my system because one-to-many multiplicity means that an object one side can be linked to many objects on the other side but can be only linked back to that specific object. In relation to the system, it means explains that one weapon can be linked to many powerups but those powerups can only be linked back to that weapon because of specficity.

