class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in range(len(matrix)):
            for n in range(len(matrix[m])):
                if matrix[m][n]==target:
                    return True
        return False
        