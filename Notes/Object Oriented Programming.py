#Thomas Gilman
#Paul Yost
#Etgg 1801-02
#23rd November, 2015

#So far our programs have been very Procedural:
    #For Example:
        #ship_x=400
        #ship_y=300
        #ship_angle=0
        #ship_angle_travel=0
        #ship_speed=0
        #def draw_ship(x,y,angle): draws ship at location with angle
    #all initialized variables for the ship.
#Object Oriented Programming:
#A different way of thinking about programming.
#A way to organize our code so that we move naturally represent real-world item.
#With procedural programming,
    #what happens if you want another ship?
        #*make more variables for the other ship.
        #*make more code that manipulates those variables.
        #*make more functions
    #data, functions, & code:
        #* only grouped by how we use them together.
    #Ex: In the real world:
        #What makes an object:
            #*Properties(Characteristics, Attributes)-data items or variables.
            #*Behaviors(abilities, actions, etc...)-actions or code.
    #Ex: A dog
        #Properties:*shape, size, weight, breed, alive or dead, hungry, disposition?, awake?, IQ, age, etc.
        #Behaviors:*eat, sleep, bark, attack wag-tail, walk, run, have sex, die, rot, vomit, poop.
#In Object Oriented Programming:
    #Characteristics are called:
        #*Properties
        #*Object variables
    #Behaviors are called:
        #*Methods
        #*Object functions
    #an Object is a collection of:
        #*Properties
        #*and Methods
        #*Are grouped together

#Make an Object in Python:
    #First, we must make a 'class'.
    #a class is like a blueprint or a template that we can use to create objects.
    #Once we have a class, we can make an object 'instance'(or many object instances) from that class.
    #With one class, we can make as many instances as we'd like.
#Class example:
class Coin(object):
    def __init__(self): #Object Function: __init__ [Special Object function: the constructor.
#The constructo is called when we make an Object instance.    
        self.side_up="heads"
    def turnover(self): #Self refers to the current object instance. :always the first parameter of every object function.
        if self.side_up=="heads": #We define the object variables.
            self.side_up="tails"
        else:
            self.side_up="heads"
    def flip(self):
        import random
        if random.randint(0,1)==0:
            self.side_up="heads"
        else:
            self.side_up="tails"
#To create an object instance:
penny=Coin()
print(penny.side_up)#->heads
penny.turnover()
print(penny.side_up)#->tails
penny.flip()
print(penny.side_up)#->prints the side of penny after flip.
