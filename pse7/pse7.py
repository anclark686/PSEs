"""
Implement reshape_matrix.

Use these tests to guide your solution. These tests may make different 
assumptions about the problem than you did! Do not alter your assumptions 
above, and take these assumptions for this challenge.

def test_convert_two_by_two_to_one_by_four():
    matrix = [[1,2],[3,4]]
    r = 1
    c = 4

    reshaped_matrix = reshape_matrix(matrix, r, c)

    assert reshaped_matrix == [[1,2,3,4]]

def test_cannot_reshape():
    matrix = [[1,2],[3,4]]
    r = 2
    c = 4

    reshaped_matrix = reshape_matrix(matrix, r, c)

    assert reshaped_matrix == [[1,2],[3,4]]

def test_convert_four_by_two_to_two_by_four():
    matrix = [[1,2],[3,4],[5,6],[7,8]]
    r = 2
    c = 4

    reshaped_matrix = reshape_matrix(matrix, r, c)

    assert reshaped_matrix == [[1,2,3,4],[5,6,7,8]]

def test_three_by_three_to_nine_by_one(self):
        # Arrange
        matrix = [[7, 2, 1], [4,3,5], [6,9,8]]
        r = 9
        c = 1 
        # Act
        answer = reshape_matrix(matrix, r, c)
        # Assert
        self.assertEqual([[7],[2],[1],[4],[3],[5],[6],[9],[8]], answer)
"""



''' feedback

'''


def reshape_matrix(matrix, r, c):
    '''
    INPUT: Two dimensional list, and number of rows and columns of reshaped matrix
    OUTPUT: Reshaped matrix
    '''
    
    if len(matrix) * len(matrix[0]) != r * c:
        return matrix
        
    full_list = [i for sublist in matrix for i in sublist]
    new_nums = []

    for i in range(r):
        new_row = full_list[i * c : i * c + c]
        new_nums.append(new_row)

    return new_nums


"""
What is the time complexity of your solution? Explain. Define your variable(s).

O(n2) - because we're looping through two lists. 
"""



"""
What is the space complexity of your solution? Explain. Define your variable(s).

O(n) - because we're creating a new list, which is dependent on the original list length.
"""