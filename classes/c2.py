class Animal:                                # constructor is used to make an object

    def __init__(self,name ,age, color, region):                      # __intit__ function is the function which initializes  the object
        self.name = name
        self.age = age
        self.color = color                       # these are constructor 
        self.region = region
        self.is_domestic = False
       

def info(self):
    print('Animal details')
    print('Name:', self.name)
    print('Age:', self.age)
    print('Colr:', self.color)
    print('Region',self.region)


o1 = Animal("Elephant", 10, 'grey','Africa',False)
o2 = Animal("Lion",5,'Yellow', 'Africa',False)        

o1.info()
o2.info()