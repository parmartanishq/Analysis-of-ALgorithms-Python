def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in reversed(range(m)):
        for j in reversed(range(n)):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]

# User input
text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

# Result
result = longestCommonSubsequence(text1, text2)
print("Length of Longest Common Subsequence:", result)
