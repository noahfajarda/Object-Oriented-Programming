import csv

# classes:
class Item: # initialized data type

    pay_rate = 0.8 # (class attibute) The pay rate after 20% discount
    
    all = [] # list to add all instances; can access each instance in this list
    
    # constructor
    def __init__(self, name: str, price: float, quantity=5): # built-in method
        # default parameters at the end and set them equal to value
        # self parameter necessary
        
        # initiated by calling the method by itself --> 'item1 = Item()'
        print(f"An instance created: {name}")
        
        ''' 'name: str' as parameter verifies datatype'''
        
        # Asserts for data types
        assert type(name) == str, f"Invalid data type for name"
        assert float(price), f"Invalid data type for price"
        assert type(quantity) == int, f"Invalid data type for quantity"
        
        # Run validations (asserts) to the received arguments to test if positive number
        assert price >= 0    # once verified that 'price' is 'float', then assert if > 0
        assert quantity >= 0, f"Price ({quantity}) needs to be > 0" # gives statement after error
        
        # assign the item name to be 'name' parameter, and can be accessed
        self.name = name     # ENCAPSULATION: underscore ('self._name') makes it a 'property' == won't be able to be changed
        self.price = price
        self.quantity = quantity
        
        # append code everytime I create an instance
        # actions to execute
        Item.all.append(self)        # will add each instance of 'Item' created to the list 'all'
    
    # PROPERTY attribute
    #@property
    # Property Decorator = Read-Only Attribute
    # you won't be able to change this attrubte
    #def name(self):
        #return self.__name    # add single underscore to make property decorator
    
    # SETTERS
    #@name.setter
    #def name(self, value):     # 'set' new value for name with '.__' that is a 'property'
    #   if len(value) > 10:                             # ENCAPSULATION: restrict access to override methods and var in setters
    #       raise Exception("Name too long!")
    #   self.__name = value         # a 'property' attribute will be READ ONLY, unless a setter is used to change the value
    
    
    # METHODS: functions inside classes
    
    def calculate_total_price(self): #function/method for data type
        
        # 'self' parameter for method == passes itself as a parameter
                # i.e.: item1.calculate_total_price === calculate_total_price(item1)
        
        # can utilized initalized variables from '__init__'
        # instead of 'return x * y'
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate # have to call object to display (class attribute)
        # 'self' variable will use input variable from 'class' initialization

    # replaces the '.all' method for simplification
    def __repr__(self):  # use __repr__ to access all class instances in a simplified manner
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
                    # self.__class__.__name__ gets the class name, even from inherritance
    
    # class method == method accessed at class level
    # use a decorator to 'convert' to 'class method'
    # takes file as parameter
    @classmethod
    def instantiate_from_csv(cls):  # 'class' passed as argument in background
        with open('items.csv', 'r') as f: # open the csv file
            reader = csv.DictReader(f)    # read content as a list of dictionaries
            items = list(reader)          # create a list out of the dictionary

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),   # price will be type:'str' in csv file, need to convert to 'float' to meet assert condition
                quantity=int(item.get('quantity'))
            )
    
    # static method == regular methods that don't take any objects, just regular parameters
    # why use them if they don't relate to the class? == it's still related to the item class
    @staticmethod
    def is_integer(num):   # static methods DO NOT send instance ('self') as the first argument
                            # uses regular parameters
        # we will count out float that end in .0 (i.e. 5.0, 38.0)
        if isinstance(num, float):
            # count out the floats that end in .0 (i.e. 5.0, 38.0)
            return num.is_integer()
        elif isinstance(num, int): # check if int
            return True
        else:
            return False
    
    # PROPERTIES
    # property decorator creates immutable value that can't be changed no matter what
    @property
    def read_only_name(self):
        return "AAA"

    # ABSTRACTION: convert methods used within other methods to private methods
    def __connect(self, smpt_server):
        pass
    
    def __prepare_body(self):                                   # all of these are private and can only be accessed with 'send_email' method
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times.
        Regards, NoahCoding
        """
    
    def __send(self):
        pass

    def send_email(self):
        self.conect()
        self.prepare_body()
        self.send()