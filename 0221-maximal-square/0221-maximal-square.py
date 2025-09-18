class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        max_side = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(
                            dp[i][j - 1],
                            dp[i - 1][j - 1],
                            dp[i - 1][j]
                        )
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side  # area of largest square
