# call upon 'item.py' module and import all functions and classes
from item import Item

# INHERITANCE


# child class that INHERITS the functionality of parent 'Item' class
class Phone(Item):          # create another class (child class) to inherrit from original class
    all = []
    # you only need the constructor (__init__) method to get the inheritance
    # now you have access to all the additional methods in 'Item' class
    def __init__(self, name: str, price: float, quantity=5, broken_phones=0): # can add more parameters
        
        #super function == remove the duplicate
        
        # Call to super function to have access to all attributes / methods
        # super function == remove the duplicate
             # SUPER can allow you to delete the self initation variables and asserts from init class
             # you can comment out the 'assert' and 'self' in initalization and you won't get errors
        super().__init__(
            name, price, quantity
        )
        '''
        # ASSERT DATA TYPES
        assert type(name) == str, f"Invalid data type for name"
        assert float(price), f"Invalid data type for price"
        assert type(quantity) == int, f"Invalid data type for quantity"
        
        # ASSERT POSITIVE VALUES
        assert price >= 0
        assert quantity >= 0, f"Price ({quantity}) needs to be > 0"
        
        # ASSIGN PARAMETERS
        self.name = name
        self.price = price
        self.quantity = quantity
        '''
        
        # ASSERT POSITIVE VALUES
        assert broken_phones >= 0, f"Broken Phones ({broken_phones}) needs to be > 0" # check new parameter from child class
        # ASSIGN NEW PARAMETER TO SELF OBJECT
        self.broken_phones = broken_phones
        
        Phone.all.append(self)