def min_deletions_to_make_palindrome(s):
    n = len(s)

    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    min_deletions = n - dp[0][n - 1]

    return min_deletions

string = "2553432"
result = min_deletions_to_make_palindrome(string)
print(f"Minimum deletions to make '{string}' a palindrome: {result}")
