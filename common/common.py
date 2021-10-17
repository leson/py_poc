import os

class Common():
    'Testing for class written'

    def __init__(self):
        pass

    def testInput(self):
        din = input("please input:")
        print(din)

    def fibs(self):
        fibs = [0, 1]
        num = input("How many Fibonacci numbers do you want?:")
        for i in range(int(num)):
            fibs.append(fibs[-2] + fibs[-1])
        print(fibs)


if __name__ == '__main__':
    cm = Common()
    print("common : ",str(cm))
