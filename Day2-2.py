# class Test:
#     pass

# x= Test()
# y= Test()

# print(x)
# print(y)

# class Test:
#     name='I am the class'
#     variable = 10

# x= Test()
# y= Test()

# print(x)
# print(y)

# print(x.name)
# print(x.variable)
# print(y.name)
# print(y.variable)


# class Test:
#     name='I am the class'
#     variable = 10

#     def printName(self): # self is important
#         print('I am a method of the class')

# x= Test()
# x.printName()



# class Test:
#     name='I am the class'
#     variable = 10

#     def printName(self, age): # self is important
#         print('I am a method of the class')
#         print(age)

# x= Test()


# class Test2:
#     def __init__(self):
#         print('I am the init function')

# y=Test2()

class Test2:
    def __init__(self, name):
        self.name=name
        print('I am the init function')

y=Test2('y')
# print(y.name)
x=Test2('x')
# print(x.name)



class Dog:

    scientific_name = 'Canis'

    def __init__(self,name):
        self.name=name
duke =Dog('duke')
bob = Dog('bob')

# print(duke.scientific_name)
# print(duke.name)


# print(bob.scientific_name)
# print(bob.name)


class Hero:
    def __init__(self, name) :
        self.name = name
        self.energy = 100
    
    def eating(self,food):
        if food == 'pasta':
            self.energy=self.energy+10
        elif food == 'pizza':
            self.energy = self.energy - 20


mario = Hero('Mario')
print(mario.name)
print(mario.energy)


adissu = Hero('Adissu')

# print(mario.name)
# print(mario.energy)

# print(adissu.name)
# print(adissu.energy)

# mario = Hero('Mario')
# print(mario.name)
# print(mario.energy)
# mario.eating('pasta')
# print(mario.energy)
# mario.eating('pizza')
# print(mario.energy)



# class BaseClass:

#     def printName(self):
#         print ('I come from the Base Class')

# class SubClass(BaseClass) :
#     pass

# a= SubClass()
# a.printName()


# class BaseClass:

#     def printName(self):
#         print ('I come from the Base Class')

# class SubClass(BaseClass) :
#     def printName(self): #instead of pass if we def then over write the base class
#         print('I come from the Sub Class')

# a= SubClass()
# a.printName()


# EXCERCISE

# class Employee:
#     def __init__(self, name) :
#         self.name = name
#     def paycheck(self, paycheck):

# Roi=Employee('Roi')
# print(Roi.name)


class Employee:

    def __init__(self,name,paycheck):
        self.name=name
        self.paycheck=paycheck

    def raise_paycheck(self, number):
        self.paycheck= self.paycheck+(self.paycheck*number)

mario =Employee('Mario', 1000)
print(mario.name)
print(mario.paycheck)

mario.raise_paycheck(0.1)
print(mario.paycheck)