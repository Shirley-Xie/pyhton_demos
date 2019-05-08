class Kls:
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1
    @classmethod
    def get_no_of_instance(cls_obj):
        return cls_obj.no_inst
ik1 = Kls()
ik2 = Kls()
ik1.get_no_of_instance()
Kls.get_no_of_instance()


def iget_no_of_instance(ins_obj):
    return ins_obj.__class__.no_inst
class Kls:
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1
ik1 = Kls()
ik2 = Kls()
# print(iget_no_of_instance(ik1))
from functools import reduce
def strfloat(f):
    f='123.456'
    n=f.index('.')
    y=len(f)
    def char(f):
        return {'0':0,'1':1,'2': 2,'3': 3,'4':4,'5': 5,'6': 6,'7': 7,'8': 8,'9':9}[f]
    def g(a,b):
        return 10*a+b
    return reduce(g,map(char,f[:n]))+reduce(g,map(char,(f[n+1:])))/(10**n)
# print(strfloat('123.456'))
# print('name'.capitalize())


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


# 定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
         n = next(it) # 返回序列的第一个数
         yield n
         it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
  if n < 30:
      pass
  else:
      break

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs


def fool(g, h, lis):
    f = g + h
    lis.append(f)

# print('ywef')
list_ = []
fool(1, 2, list_)
fool(3, 2, list_)
print(list_, 'hfhr')
