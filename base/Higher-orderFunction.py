"""
函数式编程
    传入为函数：高阶函数
    1 函数本身也可以赋值给变量，即：变量可以指向函数,函数名也是变量 f = abs
    2 既然变量可以指向函数，函数的参数能接收变量
    那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
    返回为函数：闭包
    传入和传出都为函数：装饰器

"""

from operator import itemgetter, attrgetter
from functools import reduce
import functools
student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10)]
# itemgetter
sorted(student_tuples, key=itemgetter(2))

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [Student('john', 'A', 15),Student('jane', 'B', 12),Student('dave', 'B', 10)]

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list(map(lambda x: x**2, lis)) # 结果要用list展示[1, 4, 9, 16, 25, 36, 49, 64, 81]
reduce(lambda x, y: x+y, lis) # 叠加，只有一个值，45
# attrgetter
sorted(student_objects, key=attrgetter('age'))



# 将数值转化为int
def str2int2(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

second = str2int2('56789')
print(second)

# filter过滤空字符串
def not_empty(s):
    return s and s.strip()

not_empty = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))


# 计算素数的一个方法是埃氏筛法，迭代器
def primes():
    def _odd_iter():
        n = 1
        while True:
            n = n + 2
            yield n

    def _not_divisible(n):
        return lambda x: x % n > 0
    # 开始
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列

# 打印100以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break

# sorted 针对list
sort_ = sorted([36, 5, -12, 9, -21], key=abs)
# 若为字符按照ASCII比较
sort_str = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
sort_dict = sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)], key=lambda item: item[0])


# 闭包
def count():
    fs = []
    for i in range(1, 4):
        fs.append(lambda i: i**2)
    return fs
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量
f1, f2, f3 = count()  # 结果都是9，等到全返回才执行


# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log
def now():
    print('2015-3-25')
f_de = now()
print(now.__name__)


@log2('execute')
def now2():
    print('2015-8-20')
f_de2 = now2()
print(now2.__name__)
print('end')