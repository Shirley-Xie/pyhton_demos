
"""
string,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
"""
str1='frfvrvrv'
str1=','.join(str1)

str1=str1.split(',') # str.split(str="", num=string.count(str))，生成列表
print("我叫 %s 今年 %d 岁!" % ('小明', 10))



"""
list列表,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
"""
# 增
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList += [786]
aList.append('ivntuv')
aList.extend([3,4,5])
aList.insert(3,'woshi3')

# 删
aList.remove('xyz');
aList.pop()
# del aList[2]

# 查
aList.index('abc')# 反回索引

# other
aList.reverse()
# aList.sort() # 不支持str和int混合排序,只为list服务



"""
dict字典,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
"""
info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}

# 删
# del info;pop()
# info.clear() 

#改
info.update({'Sex': 'female' })

# 查
info.keys()
info.values()
info.items()

# other
len(info); str(info); 


"""
touple,,,,,,,,,,,,,,类似于列表，只是不能修改,,,,,,,,,,,,,,,,,,,,,,,,,,,,
"""
tup1 = ();

"""
set
"""
s1 = set([1,2,3,4,5,4,3])
s2 = set([1,20,30])
#增
s1.add('vim')
s1.update({"Google", "Runoob"})

#交并差,对称差集:除了交集
a1 = s2 & s1
a2 = s2 | s1
a3 = s1-s2
a4 = s1^s2
s1.symmetric_difference(s2)

s1.issubset(s2) #判断是否为子集

#删
s1.remove(2) 
s1.discard(9) # 即使不存在也不会发生错误
s1.clear()

"""
迭代函数
https://docs.python.org/3/howto/sorting.html
"""
# sorted(iterable, *, key=None, reverse=False)

student_tuples = [('john', 'A', 15),('jane', 'B', 1),('dave', 'B', 10)]
student_ = sorted(student_tuples, key=lambda student: student[2]) 

class Student:
	def __init__(self, name, grade, age):
		self.name = name
		self.grade = grade
		self.age = age
	def __repr__(self):
		return repr((self.name, self.grade, self.age))# 调用的时候就可以打印出来

student_objects = [('john', 'A', 15),('jane', 'B', 1),('dave', 'B', 10)]
student_ = sorted(student_tuples, key=lambda student: student[2]) 
# Operator Module Functions
from operator import itemgetter, attrgetter
sorted(student_tuples, key=itemgetter(2))

