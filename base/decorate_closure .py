'''
LEGB
L:local 函数内部作用域
E:enclosing 函数内部与内嵌函数之间
G: global 全局作用域
B: build-in 内置作用域
'''
passline = 60 #G

def func(val): #L:val,passline,就近查找
    print('%x'%id(val))
    passline = 90
    if val >= passline:
        print('pass')
    else:
        print('failed')
    def in_func():
        print(val) # E:相对而言val
    in_func()
    return in_func

def Max(val1, val2):
	return max(val1, val2)  #B:max

f = func(89)
f() #in_func
print(f.__closure__)#添加到函数属性中了
print(Max(90, 100))

'''
Closure:内部函数中对enclosing作用域的变量进行引用
函数实质与属性
1. 函数是一个对象
2. 函数执行完成后内部变量收回
3. 函数属性
4. 函数返回值
'''

def func_150(val): #L:val,passline,就近查找
    passline = 90
    if val >= passline:
        print('%d pass'%val)
    else:
        print('failed')

def func_100(val): #L:val,passline,就近查找
    passline = 60
    if val >= passline:
        print('%d pass'%val)
    else:
        print('failed')

func_150(89)
func_100(89)

'''闭包，简洁，内置函数对E作用域变量的使用，
将变量放到closure这个属性中，当内部函数处理时直接使用
1.封装
2. 代码复用
'''
def set_passive(passline):
    def cmp(val):
        if val >= passline:
            print('pass')
        else:
            print('failed')
    return cmp

f_100 = set_passive(60)
f_150 = set_passive(90)
f_100(89)
f_150(89)


'''
def my_sum(*arg):
	if len(arg) == 0:
			return 0
		for val in arg:
			if not isinstaance(val, int):
				return 0
	return sum(arg)
'''
'''
参数为函数
'''
def dec(func):
	def in_dec(*arg):
		if len(arg) == 0:
			return 0
		for val in arg:
			if not isinstance(val, int):
				return 0
		return func(*arg)
	return in_dec #必须返回，不然为None

@dec
def my_sum(*arg):
	return sum(arg)
def my_average(*arg):
	return sum(arg)/len(arg)



# my_sum = dec(my_sum)替代@dec

print(my_sum(1, 2, 3, 4, 5))

'''
装饰器就是对闭包的使用
1.装饰器用来装饰函数
2. 返回一个函数对象
3. 被装饰函数标识符指向返回的函数对象
4. 语法糖 @deco
'''