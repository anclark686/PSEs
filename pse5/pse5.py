''' question
Imagine working on software that processes lists of numbers. 
Create a function named pairs_with_given_sum It finds the number of pairs 
of numbers in a list which add up to a given target. This function should 
take in a list of whole numbers and a target as parameters. This function 
should have a return value of the integer of number of pairs.
'''

''' feedback

Very creative approach! Only suggestion I have is how can we increase time efficiency from O(n^2) to O(n).

We might be able to use a dictionary like a frequency map of every number in the list, then check for pairs. We could get rid of the nested loop.

'''

def pairs_with_given_sum(numbers, target):
    if not isinstance(target, int):
        raise ValueError
        
    if not numbers:
        return 0
        
    result = 0
    new_nums = numbers[1:]
    
    for i in numbers:
        if not isinstance(i, int):
            raise ValueError
        for j in new_nums:
            if not isinstance(j, int):
                raise ValueError
            if i + j == target:
                result += 1
                new_nums.remove(j)
                new_nums = new_nums[1:]
                break
    return result

numbers1 = [1, 2, 4, 5]
target1 = 6

numbers2 = [97, 51, 49, 35, 3, 65]
target2 = 100

print(pairs_with_given_sum(numbers1, target1))
print(pairs_with_given_sum(numbers2, target2))

''' additional question 
What is the time complexity of your solution? 
Explain. Define your variable(s) (i.e. n is the length of the list).
'''

''' answer
O(n2) - because we're looping through two lists. 
'''