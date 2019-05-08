class A:
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


a = A()
# print(a.class_foo)
print(A.class_foo)
print(a.static_foo)
print(A.static_foo)


# 可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性
class C(object):
    def getx(self): return self._x

    def setx(self, value): self._x = value

    def delx(self): del self._x

    x = property(getx, setx, delx, print("I'm the 'x' property."))

# c = C()
# c.x = 96
# print(c.x)


# 等价的写法
class C(object):
    @property
    def x(self):
        print("I am the 'x' property.")
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

c = C()
c.x = 91
print(c.x)


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
print(L)
L2 = list()
L2.add(1)
print(L2)


