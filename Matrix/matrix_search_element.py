class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        is_found = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    is_found = True
                    break
        return is_found



sol = Solution()
print(sol.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]],target=3))