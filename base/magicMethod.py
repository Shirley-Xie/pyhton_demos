class Programer(object):

    def __init__(self, name, age):
        self.name = name #可以公开访问pulic
        self.age = age #约定：私有属性private

    def __eq__(self, other):
        if isinstance(other, Programer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('The type object must be Programer')

    def __add__(self, other):
        if isinstance(other, Programer):
            return self.age + other.age
        else:
            raise Exception('The type object must be Programer')

    def __str__(self):
        return '%s is %s years old' % (self.name, self.age)

    def __dir__(self):
        return self.__dict__.keys()

    def __getattribute__(self, name):
        return super(Programer, self).__getattribute__(name)

    def __setattr__(self, name, value):
        self.__dict__[name] = value

if __name__ == '__main__':

    programer = Programer('Lily', 44)
    print('-------Magic  Method----__new___init___类与运算符_____')
    programer2 = Programer('xie', 26)
    print(programer2)
    print(programer2 == programer)
    print(programer2 + programer)
    print('-------Magic  Method----___类展示_____')
    print(programer)
    print(dir(programer))
    print('-------Magic  Method----___类属性控制_____')
    print(programer.name)
