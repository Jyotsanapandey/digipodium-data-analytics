class Cat:
    name = " "
    age = 0
    fur_color = ""
    breed = ""                             # these are properties


    def eat(self):
        print("Cat is eating!")            # this is methods

    def sleep(self):                       # without self our function become static
        print("Cat is sleeping!")     

# creating objects  
tom = Cat()
snow = Cat()
print(tom)
tom.name = "Tom"
tom.age = 3
tom.fur_color = 'gray'
tom.breed = 'City cat'

snow.name = "Snow"
snow.age = 5
snow.fur_color = 'white'
snow.breed = 'Persian'

# calling methods
tom.eat()
snow.sleep()
tom.sleep()

# display attributes
print(tom.name, tom.age, tom.fur_color , tom.breed)
print(snow.name, snow.age, snow.fur_color , snow.breed)


