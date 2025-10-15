"""
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

 

Example 1:



Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.
Example 2:



Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
"""



class Solution:
    def findPeakGrid(self, mat):
        if not mat or not mat[0]:
            return [-1, -1]

        rows, cols = len(mat), len(mat[0])
        left, right = 0, cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            max_row = 0

            # Find the row index with the max element in column 'mid'
            for i in range(rows):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i

            # Check if mat[max_row][mid] is a peak
            left_is_smaller = (mid == 0 or mat[max_row][mid] > mat[max_row][mid - 1])
            right_is_smaller = (mid == cols - 1 or mat[max_row][mid] > mat[max_row][mid + 1])

            if left_is_smaller and right_is_smaller:
                return [max_row, mid]
            elif mid > 0 and mat[max_row][mid - 1] > mat[max_row][mid]:
                right = mid - 1
            else:
                left = mid + 1

        return [-1, -1]