class Animal(object):
    def __init__(self, age):
        self.name = None
        self.age = age 
    def get_name(self):
        return self.name 
    def get_age(self):
        return self.name
    def __str__(self):
        return "Animal: " + self.name + ', ' + str(self.age)
    def set_name(self, name):
        self.name = name

class Cat(Animal):
    def speak(self):
        print('meow')
    
    def __str__(self):
        return "Cat: " + self.name + ", " +str(self.age)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    
    def get_friends(self):
        return self.friends
    
    def set_friends(self, friends):
        for f in friends:
            self.friends.append(f)

    def speak(self):
        print('Hello')

    def age_diff(self, other):
        return abs(self.age - other.age)
    
    def __str__(self):
        return 'Person: ' + str(self.name) +', ' + str(self.age)

class Student(Person):
    def __init__(self, name, age, major=None):
        super().__init__(name, age)
        self.major = major
    
    def speak():
        print('I am a HUST student')

    def set_major(self, major):
        self.major = major 

    def __str__(self):
        return 'Student: ' + str(self.name) + ', ' + str(self.age) + ', ' +self.major

class Rabbit(Animal):
    tag=1
    def __init__(self, age, parent1=None, parent2=None):
        super().__init__(age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag 
        Rabbit.tag += 1
    
    def get_id(self):
        return str(self.rid).zfill(3)
    
    def __str__(self):
        parent1 = None if self.get_parent1() is None else self.get_parent1().get_id()
        parent2 = None if self.get_parent2() is None else self.get_parent2().get_id()
        return 'Rabbit: ' + str(self.age) + ', ' + str(self.get_id()) + ', ' +str(parent1) + ', ' +str(parent2 )

    def get_parent1(self):
        return self.parent1
    
    def get_parent2(self):
        return self.parent2
    
    def __add__(self, other):
        return Rabbit(0, self, other)
    
    def __eq__(self, other):
        same_parent = (self.get_parent1().get_id() == other.get_parent1().get_id()) and (self.get_parent2().get_id() == other.get_parent2().get_id()) 
        opposite_parents = (self.get_parent1().get_id() == other.get_parent2().get_id()) and (self.get_parent2().get_id() == other.get_parent1().get_id()) 
        return same_parent or opposite_parents
    
if __name__ == '__main__':
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r3 = r1+r2
    r4 = r2+r1
    print(r3)
    print(r4)
    print(r3 == r4 )
    print(r1)
    print(Rabbit.tag)