"""
Given this problem prompt:
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3
    (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 
    (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on 
    day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, 
    so we never buy the stock to achieve the maximum
    profit of 0.
"""


def maxProfit(prices):
    day_list = []
    total = 0
    lowest = 0
    for i in range(len(prices)):
        low = i
        high = i

        if i != 0:
            if prices[i] <= prices[i-1]:
                lowest = i

        for j in range(i + 1, len(prices)):
            if prices[low] < prices[j] and prices[high] < prices[j]:
                high = j
            else:
                break
        
        if low != high:
            if low == lowest:
                day_list.append((low, high))
            
    for item in day_list:
        total += prices[item[1]] - prices[item[0]]

    return total

print(maxProfit([7,1,5,3,6,4]))
print()
print(maxProfit([1,2,3,4,5]))
print()
print(maxProfit([7,6,4,3,1]))
print()
print(maxProfit([2,2,5]))

'''their solution'''

def max_profit(prices):
    total_profit = 0
    for i in range(1, len(prices)):
        # if prices[i] - prices[i-1] is > 0, then we have a profit
        total_profit += max(prices[i]-prices[i-1], 0)
    return total_profit

print(maxProfit([7,1,5,3,6,4]))
print()
print(maxProfit([1,2,3,4,5]))
print()
print(maxProfit([7,6,4,3,1]))
print()
print(maxProfit([2,2,5]))