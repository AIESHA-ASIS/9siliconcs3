# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[OOPAct1](q1/classObjectUML.md)
## Design Revision
Changes from my previous design: "availability" attribute gets renamed to "__is_available" and is set to private

## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
|weapon_name|string|public|display purposes|
|price |int|public|cost needs to be visible to buyers when browsing items|
|quantity|int|public|quantity needs to be visible to determine the amount of stock available
|__is_available|boolean|private|Prevents the external code from setting the attribute to True/False without checking actual item stock|
## Updated UML Class Diagram
[Class Diagram](<img width="172" height="282" alt="classdiagramSG5 drawio" src="https://github.com/user-attachments/assets/b9267bb2-21a7-497f-8860-56364942b890" />

## Python Implementation
[View Python Source](q1/classImplementation.py)
## Test Run
[Test Run](<img width="1840" height="640" alt="images-classTestRun" src="https://github.com/user-attachments/assets/19508c75-f351-463b-960e-add61ca13958" />
## Object Diagram
[Object Diagram](<img width="357" height="351" alt="images-objectDiagram" src="https://github.com/user-attachments/assets/d5eac6c3-3d55-4c60-a522-09c489e4c0fb" />

## Analysis
### Why did you make your chosen attribute private?
- Among the attributes, the only chosen private attribute is __is available. By making __is_available private it enforces encapsulation. With the help of invoking encapsulation to an attrivute, it helps in preventing the attribute from modifying the availability to true or false without actually checking item stock.
### Which method changes the state of your object?
- The method that changes the state of my object is PurchaseItem(). Purchaseitem()'s purpose is to purchase an item available in the store. Using this method, the attributes price, and quantity is reduced by the amount of items purchased. 
### How did your two objects demonstrate that instances are independent?
- In the test run, it is shown by weapon 1 (object 1) that when PurchaseItem() was executed, it's quantity was reduced to 0 and changed the status of __is_available to False. Meanwhile, weapon2 (object 2) retained its initial values, maintaining a quantity of 10 and keeping its __is_available status as True. Through this, it shows that an object stores its own data, protecting its data value from getting modified by external code.
### What is the difference between your class diagram and your object diagram?
- The class diagram outlines the attributes with their data types and methods with their parameters, which serves as a general blueprint without specific data. Object diagram on the other hand, it shows a brief run-through of the actual values during execution. Both diagrams work together as the class diagram establishes the structure, and the object diagram holds the actual data during execution.
