''' question
Imagine working on software that processes lists of numbers. 
Create a function named merge_lists that takes two sorted lists 
and merges them into a single sorted list. This function should 
take in two lists of whole numbers. The function should return a 
new sorted list which consists of the elements of the two arguments.

List 1	List 2	Output
[1, 2, 4, 5]	[6]	[1, 2, 4, 5, 6]
[-30, -10, 0, 15, 16]	[-20, -5, 5]	[-30, -20, -10, -5, 0, 5, 15, 16]
'''

''' feedback

'''

def merge_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list1, list):
        raise ValueError("Both inputs must be of type 'list'")

    if list1 == [] and list2 == []:
        return list1
    elif list1 == []:
        return list2
    elif list2 == []:
        return list1
    
    if list1[0] < list2[0]:
        return [list1[0]] + merge_lists(list1[1:], list2)
    else:
        return [list2[0]] + merge_lists(list1, list2[1:])
    



list1 = [1, 2, 4, 6]
list2 = [5]
print(merge_lists(list1, list2))

list1 = []
list2 = []
print(merge_lists(list1, list2))

list1 = [-50, -25, 0]
list2 = [10, 20, 30]
print(merge_lists(list1, list2))

list1 = [-30, -10, 0, 15, 16]
list2 = [-20, -5, 5]
print(merge_lists(list1, list2))

def test_two_nominal_lists():
    # nominal test case
    # Arrange
    list1 = [1, 2, 4, 6]
    list2 = [5]

    # Act
    result = merge_lists(list1, list2)

    # Assert
    assert result == [1, 2, 3, 4, 5, 6]

def test_empty_lists():
    # edge test case
    # Arrange
    list1 = []
    list2 = []

    # Act
    result = merge_lists(list1, list2)

    # Assert
    assert result == []

def test_list_1_all_before_list_2():
    # alternative test case
    # Arrange
    list1 = [-50, -25, 0]
    list2 = [10, 20, 30]

    # Act
    result = merge_lists(list1, list2)

    # Assert
    assert result == [-50, -25, 0, 10, 20, 30]