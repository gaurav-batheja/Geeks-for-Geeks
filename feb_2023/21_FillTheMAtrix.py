# Given a matrix with dimensions N x M, entirely filled with zeroes except for one position at co-ordinates X and Y containing '1'. 
# Find the minimum number of iterations in which the whole matrix can be filled with ones.
# Note: In one iteration, '1' can be filled in the 4 neighbouring elements of a cell containing '1'.
def minIteration(self, N, M, x, y):
    #code here
    distx=max(x-1,N-x)
    disty=max(y-1,M-y)
    return distx+disty
