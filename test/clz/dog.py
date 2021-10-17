import os
from test.clz.animal import Animal

class Dog(Animal):
    'Testing for class written'

    name = ""
    age = 2

    # def __init__(self):
    #     pass

    # def __init__(self,name, age):
    #     # self.__age = age
    #     self.name=name
    #     self.age=age
    #     pass

    def sayHi(self):
        print("hello Dog")

if __name__ == '__main__':
    t = Dog("旺财",3)
    t.setAge(4)
    print(t.getName(), t.getAge())
    t2=Dog("小黑",2)
    print(t2.getName(),t2.getAge())
    t2.sayHi()

