import time

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

# s = Reverse_integer()  
# s.reverse_string(-109)
Foo = type('Foo', (), {'bar':True})
def echo_bar(self):
	print(self.bar)
ooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
# print(hasattr(ooChild, 'echo_bar'))

"""
O(n) solution for finding 
smallest subarray with sum 
greater than x 
"""

def smallestSubWithSum(arr, n, x): 
# arr1 = [84,-37,32,40,95]; 167
	curr_sum = 0; 
	min_len = n+1; 

	start = 0; 
	end = 0; 

	while (end < n): 	
		while (curr_sum <= x and end < n): 
		# 和为负数舍弃，从头算起 
			if (curr_sum <= 0 and x > 0): 
				start = end; 
				curr_sum = 0; 

			curr_sum += arr[end]; 
			end += 1; 
		# 大于要求的值从前剪掉

		while (curr_sum >= x and start < n): 
			# Update minimum 
			# length if needed 
			# 2< 6;2;6;2
			# 1< 2;1;2;3
			if (end - start < min_len): 
				min_len = end - start; 
 
			# remove starting elements 
			curr_sum -= arr[start]; 
			start += 1; 

		# 判断是否还是大于x

	if min_len == n+1:
		min_len = -1
	return min_len; 

# Driver Code 
# arr1 = [84,-37,32,40,95]; 
arr1 = [84,-37,32,40,95]; 
x = 167; 
# x = 4

n1 = len(arr1); 
res1 = smallestSubWithSum(arr1, n1, x); 
print(res1)
# 3
# This code is contributed by mits 
import collections

def shortestSubarray(A, K):
    N = len(A)
    P = [0]
    for x in A:
        P.append(P[-1] + x)

    #Want smallest y-x with Py - Px >= K
    ans = N+1 # N+1 is impossible
    monoq = collections.deque() #opt(y) candidates, represented as indices of P
    print(P)
    for y, Py in enumerate(P):
        #Want opt(y) = largest x with Px <= Py - K
        print(monoq)
        while monoq and Py <= P[monoq[-1]]:
            monoq.pop()

        while monoq and Py - P[monoq[0]] >= K:
            ans = min(ans, y - monoq.popleft())

        monoq.append(y)

    return ans if ans < N+1 else -1

# print(shortestSubarray(arr1, x))