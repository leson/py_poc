from common.common import Common
from test.clz.dog import Dog

class TestClz():
    'Testing for class written'

    def __init__(self):
        pass

    def testCommon(self):
        cm=Common()
        cm.fibs()

    def testClass(self):
        dog=Dog()
        dog.setAge(3)
        dog.setName("Ha shi qi")
        print(dog.getName(),dog.getAge())


if __name__ == '__main__':
    tc = TestClz()
    # tc.testCommon()
    tc.testClass()