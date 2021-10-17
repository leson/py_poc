import os

class Animal:
    'Testing for class written'

    name = ""
    age = 1

    def __init__(self):
        # self.__age = age
        # self.age=age
        pass

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def sayHi(self):
        print("hello animal")


if __name__ == '__main__':
    t = Animal(2)
    print(t.getAge())
    t2=Animal(3)
    print(t2.getAge())
