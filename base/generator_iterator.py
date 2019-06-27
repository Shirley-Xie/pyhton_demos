"""
当你需要存储内容的时候，便可以考虑使用生成器
延迟操作
遍历一次
"""
# 1生成器函数
def gensquares(n):
	for i in range(n):
		# print('before')
		yield i ** 2 # 有种return的赶脚，不过还是继续执行，挂起
		# print('after')

for item in gensquares(5):
	print('')	

# 生成器表达式，类似列表推倒式
squ = (x**2 for x in range(5))

next(squ)
next(squ)
# print(list(squ))

strs = 'helloworld'
count_dict = {}
for i in strs:
    count = 1
    if i in count_dict:
        count += 1
    count_dict[i] = count 
print(count_dict)

def index_word(text):
	result = []
	if text:
		result.append(0)
	for index, letter in enumerate(text, 1):
		if letter == " ":
			result.append(index)
	print(result)

def index_word2(text):
	result = []
	if text:
		yield 0 
	for index, letter in enumerate(text, 1):
		if letter == " ":
			yield index

a = 'this is this'		
for i in index_word2(a):
	print(i)
