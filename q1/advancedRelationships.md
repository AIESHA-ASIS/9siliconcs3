# Advanced Class Relationships

## Previous Activities
[classAttrib](q1/classAttributesMethods.md)
[classRel](q1/classRelationships.md)

## Existing System Description:
## Inheritance Relationship
Parent: Weapon

Child: Iron sword

Explanation: The child is a type of the parent because an iron sword 'IS-A' weapon. The child class 'Iron sword' inherits common attributes from the parent class 'Weapon.'

## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation
Relationship: Composition 
Class containing another object: IronSword
Contained Object: Blade
Explanation: The object 'Iron sword' contains a 'Blade'. A blade is a part of an Iron sword which means it co-exists with the sword. Once the iron sword object is deleted, the blade object is also deleted.

## Advanced UML Diagram
![Advanced UML](q1/images/advancedClassDiagram.drawio.png)

## Python Implementation
[Source Code](advancedRelationship.py)

## Test Run
![Test](q1/images/advancedTestRun.png)

## Object Diagram
![Objects](q1/images/advancedObjectDiagram.drawio.png)

## Reflection
Answers:

1. I chose the inheritance relationship because 'IronSword' is a specific type of 'Weapon, which makes inheritance fitting. Both classes share core weapon propertie like the price, quantity of items in stock, purchasing logic while also adding its own 'block_power' attrivute. This inheritance forms a clear "IS-A" relationship where 'Ironsword' IS-A 'Weapon.'

2. Inheritance allows 'IronSword' to reuse 'Weapon' attributes like weapon_name, quantity, and price without having to retype. Method such as purchase_item() and check_quantity() were inherited directly from the parent class (Weapon). Utilizing super().__init()__() in the code keeps the child class code short and clean.

3. The HAS-A relationship is composition because 'IronSword' creates its own 'Blade' object inside its __init__ constructor. The Blade object is a physical part of the sword which cannot independently exist in the system. It co-exists with the IrownSword object because if the IronSword object is deleted, it willbe deleted as well.

4. In part 3, association links the two independent objects that could exist seperately. In part 4 in the other hand, composition creates a relationship between them where the class owns the whole part. The contained part cannot exist without the parent object present to hold it.

5. My design follows the 'DRY' principle by using common properties like price, quantity, and methods in the Weapon class which avoids repetitive code in IronSword. By utilizing super().__init__(), the system reuses the parent class initialization logic instead of retyping duplicated code. The DRY principle keeps the IronSword class short, made up of no repetitive code other than its block_power feature. 
