"""93,94
0-1背包问题
我们有n种物品，物品j的重量为wj，价格为pj。
我们假定所有物品的重量和价格都是非负的。背包所能承受的最大重量为W。
如果限定每种物品只能选择0个或1个
"""
# 首先进行判断新东西是否可以装进去，不然继承之前的
# 若装进去，则判断
   # 否存在现在东西和空的空间和比之前最优更好
      # 有则cell[i][j] == cell[i][j-1]+cell[i-1][j-当前重量]
      #
import time
def maxSubArray1(A):
   if not A:
      return 0

   curSum = maxSum = A[0]
   for num in A[1:]:
      curSum = max(num, curSum + num)
      maxSum = max(maxSum, curSum)

   return maxSum

from sys import maxsize
def maxSubArray(a): 
   sizes = len(a)
   max_so_far = -maxsize - 1
   max_ending_here = 0
   
   for i in range(sizes): 
      max_ending_here = max_ending_here + a[i] 
      if (max_so_far < max_ending_here): 
         max_so_far = max_ending_here 

      if max_ending_here < 0: 
         max_ending_here = 0
   return max_so_far 
             
# start = time.clock()
# maxSubArray1([-2,1,-3,4,-1,2,1,-5,4])
# end = time.clock()
# print(end-start)
# print(maxSubArray([-3,4,-1,2,1,-5,]))

# function to find the smallest sum 
# contiguous subarray 
def smallestSumSubarry(arr, n): 
   # to store the minimum value that is ending 
   # up to the current index 
   min_ending_here = maxsize
   # to store the minimum value encountered so far 
   min_so_far = maxsize
   # traverse the array elements 
   for i in range(n): 
      # if min_ending_here > 0, then it could not possibly 
      # contribute to the minimum sum further 
      if (min_ending_here > 0): 
         min_ending_here = arr[i] 
      # else add the value arr[i] to min_ending_here 
      else: 
         min_ending_here += arr[i] 
      # update min_so_far 
      min_so_far = min(min_so_far, min_ending_here) 
   # required smallest sum contiguous subarray value 
   return min_so_far 
   
# Driver code 
arr = [3, -4, 2, -3, -1, 7, -5] 
n = len(arr) 
# print("Smallest sum: ", smallestSumSubarry(arr, n))



# Dynamic Programming Python implementation of Coin 
# Change problem 
def change_coins(coins, amount): 
   m = len(coins)
   # table[i] will be storing the number of solutions for 
   # value i. We need n+1 rows as the table is constructed 
   # in bottom up manner using the base case (n = 0) 
   # Initialize all table values as 0 
   table = [0 for k in range(amount+1)] 
   # Base case (If given value is 0) 
   table[0] = 1
   # Pick all coins one by one and update the table[] values 
   # after the index greater than or equal to the value of the 
   # picked coin 
   for i in range(0,m): 
      for j in range(coins[i],amount+1): 
         table[j] += table[j-coins[i]] 

   return table[amount] 

# Driver program to test above function 
arr = [1, 2, 5]  
n = 11
x = count(arr, n) 
print (x) 

# This code is contributed by Afzal Ansari 







def recMC1(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC1(coinValueList, change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins
# print(recMC([1, 5, 10, 25], 63))


def recDC(coinValueList, change, knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

# print(recDC([1, 5, 10, 25], 63, [0]*64))
