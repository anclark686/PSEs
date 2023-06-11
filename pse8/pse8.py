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