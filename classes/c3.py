import random
# class subclass(super_class)      # sub_class = new_class and super_class = old_class
class MyList(list):          # inherits from list 
    
    def shuffle(self):
        random.shuffle(self)

    def get_random(self):
        return random.choice(self)


a = MyList([12,121,3,1,2,35,7,9,3,])
a.sort()
print(a)
a.shuffle()
print(a)
print('random item from the list = ', a.get_random())
