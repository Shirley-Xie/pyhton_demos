"""
动态规划：优化问题（最少硬币找零，币值有1，10，25）
例子：1美元买37美分，找钱的最少硬币是多少？
100-37 = 63 = 25*2+10+1*3
方法：
1.贪婪算法:尽可能多的找最大的，从最大的硬币（25 美分）开始，并尽可能多，然后我们去找下一个小点的硬币，并尽可能多的使用它们
  若出现21美分，则最优为21*3，二贪婪算法结果还是和之前一样
"""

# 递归重复计算，时间长
def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList, change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins
# print(recMC([1,5,10,21,25],26))


# 计算过的数值存储起来，避免重复计算
def recDC(coinValueList,change,knownResults):
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

# print(recDC([1,5,10,25],63,[0]*64))


# 动态规划
def dpMakeChange1(coinValueList,change,minCoins):
   for cents in range(change+1):
      coinCount = cents
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
      minCoins[cents] = coinCount
   return minCoins[change]

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin


def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

# main()
def fool(g, h, lis):
    f = g + h
    lis.append(f)

# print('ywef')
list_ = []
fool(1, 2, list_)
fool(3, 2, list_)
print(list_, 'hfhr')
