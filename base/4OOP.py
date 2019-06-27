# 类与对象。类名，属性，方法，继承，封装：数据「私有」，方法，多态
class Programer(object):
    hobby = 'play computer'
    # super 是用来解决多重继承问题的,就是继承的具体操作
    def __new__(cls, *args, **kwargs):
        return super(Programer, cls).__new__(cls)   # 在2中返回所有 (cls, *args, **kwargs)

    def __init__(self, name, age, weight):
        #访问控制
        self.name = name #可以公开访问pulic
        self.__weight = weight  

        if isinstance(age, int):
            self._age = age #约定：私有属性private
        else:
            raise Exception('age must ge int')
    # 部分私有属性，只能用方法外流
    def get_weight(self):
        return self.__weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_name(self):
        return self.name

    def self_introduction(self):
        print('My Name is %s \nI am %s years old\n' % (self.name, self._age))

class BackendProgramer(Programer):

    def __init__(self, name, age, weight, language):
        super(BackendProgramer, self).__init__(name, age, weight) # 都会调用父类一遍，然后才自己
        self.language = language

    def self_introduction(self):
        print('My Name is %s\nMy favorite language is %s\n' % (self.name, self.language)) # 因为super过了父类

def introduce(programer):
    if isinstance(programer, Programer):
        programer.self_introduction()


if __name__ == '__main__':
    #定义类属性
    programer = Programer('xie', 25, 60)
    dir(programer)  # 获取属性方法列表
    programer.__dict__  # 从构造函数中获取属性键值对{'name': 'xie', '_Programer__weight': 60, '_age': 25}
    programer.get_weight()  # 部分私有属性，类可访问，实例无法直接访问,60
    programer._Programer__weight # 实例化后可通过实例名._类名__weight访问,60

    programer.get_weight   # 类的方法也是类的属性，是 method 类型的属性
    programer.get_weight = 'change'
    programer.get_weight     # 访问控制同属性 change
    print('----定义类的方法之修饰符-----------')
    Programer.get_hobby()   # @classmethod,针对直接在类写的属性，用类直接名调用
    print(programer.get_name)   # property，为了增加修改的限制

    print('---------------继承-------------')
    back_programer = BackendProgramer('xiao', 35, 70, 'python')
    print(dir(back_programer))
    print(back_programer.__dict__)
    print(type(back_programer))
    print(isinstance(back_programer, Programer))
    print(back_programer.get_weight())   # 除了重写其余都有
    print('---------------多态--------------------')
    print(introduce(programer))
    print(introduce(back_programer))


