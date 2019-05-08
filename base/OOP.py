
class OldStyle:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class NewStyle(object):

    def __init__(self, name, description):
        self.name = name
        self.age = description


class Programer(object):
    hobby = 'play computer'

    def __new__(cls, *args, **kwargs):
        print('call __new__method')
        # print(*args)
        return super(Programer, cls).__new__(cls)   # 在2中返回所有 (cls, *args, **kwargs)

    def __init__(self, name, age, weight):
        #访问控制
        print('call __init__method')
        self.name = name #可以公开访问pulic
        self.__weight = weight  # 部分私有属性
        if isinstance(age, int):
            self._age = age #约定：私有属性private
        else:
            raise Exception('age must ge int')

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
        super(BackendProgramer, self).__init__(name, age, weight)
        self.language = language

    def self_introduction(self):
        print('My Name is %s\nMy favorite language is %s\n' % (self.name, self.language))

def introduce(programer):
    if isinstance(programer, Programer):
        programer.self_introduction()


if __name__ == '__main__':
    #定义类属性
    programer = Programer('xie', 25, 60)
    print('-----定义类的属性-----------')
    print(dir(programer))   # 获取属性方法列表
    print(programer.__dict__)   # 从构造函数中获取属性键值对
    print(programer.get_weight())   # 部分私有属性，类可访问，实例无法直接访问
    print(programer._Programer__weight)     # 实例化后可通过实例名._类名__weight访问
    print('------定义类的方法之属性----------')
    print(programer.get_weight)    # 类的方法也是类的属性，是 method 类型的属性
    programer.get_weight = 'change'
    print(programer.get_weight)     # 访问控制同属性
    print('----定义类的方法之修饰符-----------')
    print(Programer.get_hobby())    # @classmethod,针对直接在类写的属性，用类直接名调用
    print(programer.get_name)   # property，为了增加修改的限制
    print(programer.self_introduction())    # 正常调用
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


    '''old = OldStyle('old', 'Old style class')
    print(old)
    print(type(old))
    print(dir(old))
    print(dir())
    print('-------------------------')
    new = NewStyle('new', 'new style class')
    print(new, type(new), dir(new))
    print(dir())'''
