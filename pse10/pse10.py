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