"""
函数

# 了解函数的意义，掌握函数创建及使用 
	 函数的意义:
		 1.对输入进行变换映射后输出 
		 2.过程化 VS 结构化
	 函数的创建及结构: 
			 return与yield的区别

# 参数使用
语法:func(positional_args,keyword_args,*tuple_nonkw_args,**dict_kw_args)
 按参数传递方式:
	 位置参数包裹及使用*
	 关键字参数包裹及使用**
	 包裹解包顺序
	 传递参数时使用包裹
 函数如何处理传入参数:
	 值传递参数与指针传递参数
"""
"""
2.要求创建一个函数，它可以接收，位置参数， 不定长位置参数，不定长关键词参数，并按 要求输出 。
 输入班级名，班级特色(如’勤奋’,’颜值 高’ )等等不同特色，班级不同同学的姓 名与年龄。
 要求输出，班级名，班级特色，班级成员， 班级成员的平均年龄。
"""
#默认参数
def myp(str, age=35): # 默认放在最后，age=35关键字参数，str:位置参数
	print(str,age)
myp('go')

# 不定长参数，*args：位置, **kwargs：关键字,toupe,dict
def class_(className, *args, **kwargs):
    # con = lambda x : sum(x)/len(x)
	ret = {'班级姓名':className,
		'班级特色':args,
		'班级成员':kwargs['name'],
		'班级平均年龄': sum(kwargs['age'])/len(kwargs['age']),
		# '班级平均年龄': con(kwargs['age'])
	}
	return ret

name = ['xie','li','zhang']
age=[32,21,34]
ret = class_('18班', '勤奋','颜值高',name=name,age=age)
print(45,ret)


"""
 理解变量的作用域
标识符的作用域
locals()
globals() 
"""


"""
匿名函数lambda:  使用场景:
 返回简单结束 ，不需要专门定义函数
"""

#使用1：作为正常函数使用，不推荐
foo=lambda x,y:x+y #不用写return
#lambda
print(foo(5,6))

#使用2：lambda关键字定义在高阶函数的参数位上
d1={'china':15,'India':9,'USA':2,'Japan':1.5}
sorted(d1.items(),key=lambda x:(x[0],x[1]))#按d1.items()第0个元素升序，国家名
sorted(d1.items(),key=lambda x:(x[1]))

"""
 理解高阶函数的概念
 引用:访问，变量别名(多个别名引用) 
 调用:()

"""
#高阶函数:一个函数接收另一个函数作为参数
def mycalucate(num,func):
    return func

									#回调函数:函数作为调用函数的结果返回
									def callbackfunc(*num):
									    return max


"""
 掌握BIFs中的map(),reduce(),filter()函数的使用 
"""
l1 = [6,90,6]
# 找到及格的人
list(filter(lambda x:True if x >60 else False,l1)) # 90, 用真假
# [(6, 2), (90, 1), (6, 2)]
list(map(lambda x:(x,l1.count(x)),l1))
#reduce()对list的每个元素反复调用函数f，并返回最终结果值。
from functools import reduce
reduce(lambda a,b:a+b,[1,2,3,4,5,6,7,8])

"""
 了解闭包，装饰器，函数式编程的概念

 闭包的概念
 涉及嵌套函数时才有闭包问题
 内层函数引用了外层函数的变量(参数)，然后 返回内层函数的情况，称为闭包(Closure)。
 这些外层空间中被引用的变量叫做这个函数的环 境变量。
 环境变量和这个非全局函数一起构成了闭包。  闭包的特点:
 函数会记住外层函数的变量  闭包的实现:


 定义:
 以函数作参数并返回一个替换函数的可执行函数
 简单理解:
 装饰器的作用就是为已存在的对象添加额外功能  为一个函数增加一个装饰(用另一个函数装饰)  本质上就一个返回函数的高阶函数
 应用:
 给函数动态增加功能(函数)

 函数式编程Functional Programming
 函数式编程思想:
 函数是第一等公民First Class
 函数式编程是一种编程范式，是如何编写程度的方法论。 把运算过程尽量变成一系列函数的调用。属于结构化编程
 特点:
 允许函数作为参数，传入另一个函数  返回一个函数

"""



"""
1.定义一个函数，接收任意3个数字的输入，并按 顺序从小到大输出
"""
def from_s2b(*args):
	print(sorted(args)) 
# from_s2b(3,9,5)
# sorted()和sort()的比较



# 匿名函数问题

# 3.使用reduce函数实现找出一组数字列表中的 最大值
reduce(lambda x,y:y if x < y else x,[1,13,4,7])

# 4.求1000以内能同时被3和7整除的数有哪些。要求使用****map****与filter函数
def lab(x):
	if (x%3==0 and x%7==0):
		print(x)
		return x
a = list(map(lambda x:x%3==0 and x%7==0,range(1,64)))

b = list(filter(lambda x:(x%3==0 and x%7==0), range(1,1000)))
# print('rvtv',a[:10],b[:10])

"""
6.
 要求使用map与filter函数，输出一个输入字 符串里每个字符出现的次数
 提示:结合dict使用实现
"""
def dictfun(s):
	dic = {}
	if s in dic:
		dic[s]+=1 
	else:
		dic[s]=1

a = list(map(dictfun,'hfurfhfk'))
a = list(filter(dictfun,'hfurfhfk'))
print(a)

# 4.1体现闭包的思想，创建一个三层嵌套的函数， 并调用。
nums_in_global=[15,2,3,9,3.2]#声明一个全局

def foo1(nums_in_function):
    print('nums_in_function此时在是foo1中，可以被 访问：',nums_in_function)
    def foo2():
        return max(nums_in_function)
#         return max(nums_in_global)#虽然没有给foo2传入任何参数，但foo2却能访问到全局变量nums_in_global
    return foo2

# print(nums_in_function)#此时已经消失了 #name 'nums_in_function' is not defined

#调用
# foo1([5,3,8])()

"""
5.0
请以round函数，定义一个偏函数roundN，调用
为输入一个数字N，返回圆周率后N位的数字 

 了解偏函数，匿名函数
偏函数Partial function application
使用场景:如果一个函数的参数很多，而在每次 调用的时候有一些又经常不需要被指定时，就可 以使用偏函数(近似理解为默认值)
 语法:partical(func,*args,**keywords)
 原理:创建一个新函数，固定住原函数的部分参 数(可以为位置参数，也可以是关键字参数)

5.1
请以sorted函数，定义一个偏函数sortedDESC， 结果为输入一个序列，返回为按降序排列后序列。
"""
# 5.0
from functools import partial
import math

hex2int2=functools.partial(math.pi,base=16)

# 5.1
l = [4,5,67,3,54]
sorted(l, reverse=True)

















