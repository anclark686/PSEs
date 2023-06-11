''' question
Imagine working on software that analyzes mutations in DNA.

Create a function named hamming_distance that calculates the number of differences between two DNA strands (aka two strings). This method should take in two different DNA strands of the same length as parameters. This method should have a return value of the number of differences between each string.

For example, given these two DNA strands (strings), hamming_distance should return 7 because there are 7 differences:
'''

''' feedback
Love it! Short and sweet! Good job
'''

def hamming_distance(strand1, strand2):
    if len(strand1) != len(strand2):
        raise ValueError
    
    distance = 0
    
    for i in range(len(strand1)):
        if strand1[i] != strand2[i]:
            distance += 1
            
    return distance