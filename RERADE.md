1.安装anaconda

2.使用自带的jupyter notebook

3.numpy:数组与矩阵运算 ndarray,ufunf
  pandas：二维表格处理 series，dataFrame,index
  matplotlib:绘图

4.开发工具
	cmd命令行  
	自带及第三方IDE工具。
	推荐：jupyter notebook
  方式：
	脚本式：一次性；python xx.py 魔法参数run% xx.py
	交互式:一步步；

5.操作
	\n，缩进，模块，import
	多行写在一行用；
	命名区分大小写，不可为关键字
	自带电池：好用的函数

不可变类型:
	□ 数值 Number 
	□ 字符串 String
	□ 容器类型
(可变类型): 
	□列表 List
	□元组 Tuple 
	□集合 Set
	□字典 Dictionary

	▪ 算术运算符
	/，//取整，%取模(余数 )，**求幂

	▪ 赋值运算符
	# 多重赋值，=
		a=b=c=100
		# 多元赋值
		a,b,c=99,100,101
		# 变量交换赋值
		a,b,c=b,c,a

	 逻辑运算符 
	 ■ and/or/not

	▪ 成员运算符
	■ in/not in身份运算符

	▪ 身份运算符
	■ is/is not身份运算符	
 
 左闭右开
 #如果是字符串包含单引或双引，则需要对其进行转义
sentence='Today\'s news is not a good news'

#访问之切片
# [::]三个参数分别是开始索引位置，结束索引位置，步长。
s = 'china'
print(s[0:-1:-1])

#格式化访问
url='http://www.{}.com'
companyName='七月在线'
url.format(companyName)
url.find('edu')
返回索引值
url.replace('原来的','替换') URL没变
url.count('hhh')
url.index('台')

1：若找最后3位字符[-3:0:-1]
序列对象：str，list ， tuple

sorted(a) # a不变
a.sort() # a 改变
index find 返回的是索引，若没找到，find返回-1，index报错
any('',0,false)

{}并集 : | update()


a="hello"  #全局变量a
def test():
    global a
    a="hell0 global" #修改全局变量a的值
    b =a     #test方法之里后再调用a时，都是全局的a
    print(b+",",a)
test()
print(a)

#hell0 global, hell0 global
hell0 global

def localsPresent():
    present = True
    print(present)
    locals()['present'] = False;
    print(present)

localsPresent()
#True
True

import functools
hex2int2=functools.partial(int,base=16)

函数名就是变量



