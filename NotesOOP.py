# call upon EXTERNAL MODULES ('items.py' & 'phone.py') inside folders
from item import Item
from phone import Phone

# OOP PRINCIPLES
'''
Encapsulation: restrict direct access to some attributes in program
Abstraction: shows necessary attributes, hides (abstracts) unnecessary ones/information from instances
Inheritance: reuse code throughout the classes (child --> parent classes)
Polymorphism: IMPORTANT: use single type entity to represent different types in different scenarios of exact same entity
'''

# assign values
print("\nCREATE & ASSIGN VALUES: ")
item1 = Item("Phone", 25, 3)
item2 = Item("ipad", 12, 43)
item1.name = "Phone"
item1.price = 100
#item1.quantity = 5
# call method                           # pass parameters
#print(item1.calculate_total_price(item1.price, item1.quantity))

print("\nCALL CLASS METHOD W/O PARAMETERS (SELF VARIABLES INIALIZED): ")
# call class method without parameters b/c self variables already initalized
print(item1.calculate_total_price())
print(item1.name)
print(item1.price)
print(item1.quantity)

print("\nPRINTS DATA TYPES OF ASSIGNED VARIABLES: ")
# prints data types of assigned variables
print(type(item1)) # item; (uses the data type initialized as a 'class')
print(type(item1.name)) # str
print(type(item1.price)) # int
print(type(item1.quantity)) # int

# methods for strings
print("\nUSING BUILT-IN METHODS FOR STRINGS (i.e. capitalize): ")
random_str = "message"
print(random_str.upper()) #capitalize all letters


# can add attributes to object "Item" even when it's not initialized:
print("\nADD ATTRIBUTES WITHOUT INITIALIZATION: ")
item1.has_numpad = False
print(f"Has numpad?: {item1.has_numpad}")

# access class attribute
print("\nACCESS CLASS ATTRIBUTES FOR DIFFERENT INSTANCES: ")
print(Item.pay_rate)
print(item1.pay_rate) # first searches if initialized in function,
print(item2.pay_rate) # then searches for 'class attribute' at 'class' level

print("\nDICTIONARY WITH ALL 'CLASS' LEVEL ATTRIBUTES: ")
print(Item.__dict__) # '.__dict__' returns all attributes at 'class' level
print("\nDICTIONARY WITH ALL 'INSTANCE' LEVEL ATTRIBUTES: ")
print(item1.__dict__) # '.__dict__' returns all attributes at 'instance' level

print("\nUSING METHOD AND ACCESSING CLASS ATTRIBUTE")
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7 # changes default value of class attribute (0.8)
item2.apply_discount() # use 'apply discount' method from class
print("\nUSE AND INITALIZE CLASS ATTRIBUTE")
print(item2.price)


print("\nCREATE NEW 'ITEM' INSTANCES")
sample_item1 = Item("Phone", 100, 1)      # creating multiple 'item's from class
sample_item2 = Item("Laptop", 1000, 3)
sample_item3 = Item("Cable", 10, 5)
sample_item4 = Item("Mouse", 50, 5)
sample_item5 = Item("Keyboard", 75, 5)

print("\nALL CLASS INSTANCES: ")
print(Item.all) # uses 'all' attribute to access all instances
print("\nUSE FOR LOOP, ALL CLASS INSTANCES: ")
for instance in Item.all:
    print(instance.name)
    
    
# save data in a .csv file
# creates a dictionary from information from csv
print("\nUSING CLASS METHOD, PRINT DICTIONARIES OF ITEMS: ")
Item.instantiate_from_csv()
print(Item.all)                    # stores instances inside a list



# static methods
# they are just regular functions, the only difference is they are in the class
# but they really are just regular functions
print("\nUSING STATIC METHODS, THEY'RE REGULAR FUNCTIONS INSIDE CLASSES: ")
print(Item.is_integer(7.0))
print(Item.is_integer(7.5))
print(Item.is_integer(7))


# INHERITANCE
print("\nINHERITANCE, 'PHONE' CLASS IS A 'CHILD' CLASS INHERITING FROM 'PARENT' 'ITEM' CLASS")
# parent classes and child classes

phone1 = Phone("NoahPhone22", 500, 5, 1)    # create instance of phone
phone2 = Phone("NoahPhone33", 700, 5, 1)

print(f"\nTotal Price from child methods and inherritted parent methods: {phone1.calculate_total_price()}")
print()
print(Item.all)
print("\nPrints specified class name using self.__class__.__name__ from __repr__: ")
print(Phone.all)

print(f"\nUtilized EXTERNAL MODULES to call classes and methods.")

# ENCAPSULATION
# an attribute that can only be INITALIZED ONCE
# will have errors if changed later in code

print(f"\nENCAPSULATION LETS ATTRIBUTE TO BE INITIALIZED ONCE:")
item1 = Item("MyItem", 750)
item1.name = "OtherItem"   # this should produce an error with 'encapsulation'

# PROPERTIES
# cannot be overwritten
# 'item1.read_only_name - "BBB"' will not work
print(item1.read_only_name)     # will print "AAA" from Item module

# SETTERS
# item1.read_only_name = "other"  will set the property to another value