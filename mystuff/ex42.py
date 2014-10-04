## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
    
## Dog is-a Animal that has-a __init__ function using self and name as parameters
class Dog(Animal):

    def __init__(self, name)
        ## from self get the attribute name and set it to name
        self.name = name

## Cat is-a Animal that has-a __init__ function using self and name as parameters
class Cat(Animal):

    def __init__(self, name)
        ##
        self.name = name
        
## Person has-a __init__ that takes self and name parameters
class Person(object):

    def __init__(self, name)
        ## from self get the name attribute and set it to name
        self.name = name
        
        ## from self get the pet attribute and set it to none
        self.pet = none
        
## Employee is-a Person that has-a __init__ that takes self, name and salary parameters
class Employee(Person):

    def __init__(self, name, salary):
        ## hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## from self get the salary attribute and set it to salary
        self.salary = salary
        
## Fish is-a object
class Fish(object):
    pass
    
## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass
    

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## from mary get the pet attribute and set it to satan
mary.pet = satan

## set frank to an Frank instance of class Employee
frank = Employee("Frank", 120000)

## from frank get the pet attribute and set it to rover
frank.pet = rover

## set flipper to an instance of class Fish
flipper = Fish()

## set crouse to an instance of class Salmon
crouse = Salmon()

## set harry to an instance of class Halibut
harry = Halibut()