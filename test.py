# 数字反转
class Reverse_integer:
	def reverse_string(self, x):
		# x = int(str(x)[::-1]) if x>= 0 else -int(str(-x)[::-1])
		# return x if x<2147483648 and x>= -2147483648 else 0
        # 改进版
		sign = 1 if x>=0 else -1
		rever = int(str(x*sign)[::-1])
		return sign*rever * (rever < 2**31)

	def reverse(self, x):
		sign = 1 if x >= 0 else -1
		new_x, x = 0, abs(x)
		while x:
			new_x = 10 * new_x + x % 10
			x //= 10   
		new_x = sign * new_x
		return sign*new_x * (rever < 2**31)

s = Reverse_integer()  
s.reverse_string(-109)


# 为什么运算加括号
# Python运算符优先级
def cmp(a,b):
	print((a>b)-(a<b))
	print(a>b - a<b)
cmp(5,4)
