# Object Orientd Programming
## 基本概念
	类：对事物的的一种抽象
	对象：类的实例
## 基本要素
	属性：变量，功能：方法

## 封装：
    对于类的方法而言，对外只知道功能隐藏细节
## 继承：
    子类从属父类的属性和方法，也可自己定义，覆盖父类或添加。
    用super()调用父类的方法：
    class A（object）：
       def method（self，arg）：
          pass

    class B（A）：
        def method（self，arg）：
          super（B，self）.method(arg)

    用类名调用父类的方法(体现不了继承关系)：
    class A(object):
        def method(self,arg):
           pass

    class B(A):
       def method(self,arg):
          A.method(arg)

    子类的类型判断：
    isinstance:判断父类
    issubclass:判断是否是子类
    多重继承：继承不同维度


    多继承：
    class DerivedClassName(Base1,Base2,Base3):
      <statement-1>
      ...
      <statement-n>

## 多态：
    不同子类继承同一父类调用同一方法，因子类重写而有不同的反馈
    （继承与方法重写，可以直接替换）


## 定义类
    构造函数def__init__(self, [...):
    析构函数def__del__(self, [...):垃圾回收
    老式类默认不继承Object，新式是有的
    2个内建函数
    dir()函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表
    type()

## 定义类的属性
1．直接在类中定义
   所有类的对象属性都一样
		class Programer(object):
		   sex = 'male'
2. 在构造函数里定义（可以改变对象的属性）
	 #访问控制无，是人为约定
   class Programer(object):
       def __init__(self,name,age):
           self.name = name      #可以公开访问pulic
           self._age = age       #约定，私有属性private
           self.__weight = weight
           #部分私有属性，类可访问，实例无法直接访问
           #实例化后可通过实例名._类名__weight访问

## 定义类的方法
    函数和方法：
    函数：直接用函数名调用的，
    方法：类的一部分，必须和对象结合一起使用

    类的方法也是类的属性，是 method 类型的属性
    访问控制同属性
    @classmethod: 针对直接在类里定义的属性，调用时候用类名，不是某对象名
    @propery: 像访问属性一样调用方法


## Magic Method:方法名旗前后有2个下划线
### 构造对象
	1 创建类的对象def __new__(cls)可以重写需要返回
	2 初始化对象 def __init__(self)

### 运算符
	比较运算符
	__cmp__(self,other)比较所有情况
	__eq__(self,other)
	__lt__(self,other)
	__gt__(self,other)
	数字运算
	__add__(self,other)
	__sub__(self,other)
	__mul__(self,other)
	__div__(self,other)
	逻辑运算
	__or__(self, other)
	__and__(self, other)

### 类的展示
      转换字符串 __str__, __repr__, __unicode__
      展现对象属性  __dir__

### 类的属性访问
	def __setattr__(self,name,value)：
	    self.__dict__[name] = value   是正确的

	查询 __getattr__, 未查询 getattribute,  每次 ，易引起递归
	删除 __delattr__,
	设置 __setattr__,

