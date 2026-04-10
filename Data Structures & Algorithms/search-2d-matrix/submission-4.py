class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        mid = -1
        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][0] < target:
                if len(matrix) == mid + 1 or matrix[mid + 1][0] > target:
                    break
                low = mid + 1
 
        low = 0
        high = len(matrix[mid]) - 1
        while low <= high:
            new_mid = (high + low) // 2
            if matrix[mid][new_mid] == target:
                return True
            elif matrix[mid][new_mid] > target:
                high = new_mid - 1
            else:
                low = new_mid + 1
        return False
    
        