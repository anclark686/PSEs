"""
Given this problem prompt
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is not present in the array.

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are 
    [1,5,6,8,9,10,12,13,...]. 
    The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are 
    [5,6,7,...]. The 2nd missing positive integer is 6.
Constraints:

1 <= arr[i]
1 <= k
arr[i] < arr[j] for 1 <= i < j <= arr.length
"""


def kth_missing_positive_number(numbers, k):
    '''
    INPUT: List of positive numbers in increating order & a positive integer k
    OUTPUT: The kth missing number
    '''
    def num_generator(list):
        for i in range(1000):
            if i not in list:
                yield i
                
    nums = num_generator(numbers)
    num = 0
    
    for i in range(k + 1):
        num = next(nums)
        
    return num