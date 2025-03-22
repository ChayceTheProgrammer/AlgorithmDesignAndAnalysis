def longest_increasing_subsequence(nums):
    """
    Find the length of the longest increasing subsequence in the given sequence.

    Args:
        nums (list): A sequence of numbers.

    Returns:
        int: The length of the longest increasing subsequence.
    """
    n = len(nums)
    dp = [1] * n  # Initialize dp array with 1s
    prev = [-1] * n  # Initialize prev array with -1s

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Find the index of the maximum value in the dp array
    max_index = dp.index(max(dp))

    # Reconstruct the longest increasing subsequence
    lis = []
    while max_index != -1:
        lis.append(nums[max_index])
        max_index = prev[max_index]
    lis.reverse()

    return len(lis)

if __name__ == "__main__":
    # Test cases
    print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]))  # Output: 6
    print(longest_increasing_subsequence([3, 10, 2, 1, 20]))  # Output: 3
    print(longest_increasing_subsequence([1, 2, 3, 4, 5]))  # Output: 5
    print(longest_increasing_subsequence([5, 4, 3, 2, 1]))  # Output: 1
    print(longest_increasing_subsequence([2, 2, 2, 2]))  # Output: 1