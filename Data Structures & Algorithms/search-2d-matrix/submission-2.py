class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix[0])
        width = len(matrix)
        
        left = 0
        mid = (width * height) // 2
        right = (width * height)

        # matrix [x/4][x%4]
        while left < right:
            matrixValue = matrix[mid // height][mid % height]

            if target == matrixValue:
                return True
            elif target > matrixValue:
                left = mid + 1
                mid = (left + right) // 2
            elif target < matrixValue:
                right = mid
                mid = (left + right) // 2
        
        return False


        