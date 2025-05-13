def verify_subset_sum(S, t):
    """
    Verifies whether a subset of S exists that sums to t.

    Args:
        S: List of positive integers
        t: Target sum

    Returns:
        (bool, subset): A tuple containing whether a solution exists and the subset if it does
    """
    # Part (a): Systematically check all subsets
    n = len(S)
    solution_found = False
    solution_subset = []

    # Generate all 2^n possible subsets using binary representation
    print(f"Systematically checking all subsets of {S} to find a subset that sums to {t}:")
    for i in range(1, 2 ** n):
        # Convert number to binary to represent subset selection
        binary = bin(i)[2:].zfill(n)
        subset = [S[j] for j in range(n) if binary[j] == '1']
        subset_sum = sum(subset)

        # Output for the systematic check
        print(f"  Subset {subset}: sum = {subset_sum}")

        if subset_sum == t:
            solution_found = True
            solution_subset = subset
            print(f"  ✓ Solution found: {subset} sums to {t}")
            break

    if not solution_found:
        print(f"\nNo subset sums to {t}.")

    return solution_found, solution_subset


def brute_force_complexity(sizes):
    """
    Demonstrates why brute force is not feasible for larger sets.

    Args:
        sizes: List of set sizes to analyze
    """
    print("\nPart (b): Why brute force is not feasible for larger sets:")

    for n in sizes:
        subsets = 2 ** n
        print(f"  For n = {n}: 2^{n} = {subsets:,} subsets to check")

    print("\nThe exponential growth makes it impractical to check all subsets for large n.")


def analyze_dynamic_programming_complexity():
    """
    Explains why a dynamic programming solution is not polynomial time.
    """
    print("\nPart (c): Why dynamic programming is not polynomial time:")
    print("  1. The dynamic programming solution has time complexity O(nB) where:")
    print("     - n is the number of elements in the set")
    print("     - B is the target sum")
    print("  2. Input size analysis:")
    print("     - To represent n numbers, each up to B, we need O(n log B) bits")
    print("     - The numbers are encoded in binary (log B bits each)")
    print("  3. Therefore:")
    print("     - O(nB) = O(n × 2^(log B))")
    print("     - This is exponential in terms of the input size")
    print("     - Making it a pseudo-polynomial time algorithm, not truly polynomial")


def demonstrate_dp_solution(S, t):
    """
    Implements and visualizes the dynamic programming solution.

    Args:
        S: List of positive integers
        t: Target sum

    Returns:
        bool: Whether a solution exists
    """
    n = len(S)

    # Create DP table: rows are items 0...n, columns are sums 0...t
    dp = [[False for _ in range(t + 1)] for _ in range(n + 1)]

    # Base case: empty subset can form sum 0
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the table
    for i in range(1, n + 1):
        for j in range(1, t + 1):
            if j < S[i - 1]:
                # Can't include current element
                dp[i][j] = dp[i - 1][j]
            else:
                # Either include or exclude current element
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - S[i - 1]]

    # Visualization of the DP table
    print("\nDynamic Programming Table for SUBSET SUM:")
    print("  (rows = items considered, columns = target sums)")

    # Print column headers
    header = "     |"
    for j in range(t + 1):
        header += f" {j:2d} |"
    print(header)
    print("-" * len(header))

    # Print table rows
    for i in range(n + 1):
        row_label = "∅" if i == 0 else f"{S[i - 1]}"
        row = f" {row_label:3s} |"
        for j in range(t + 1):
            cell = " T " if dp[i][j] else " F "
            row += f"{cell}|"
        print(row)

    return dp[n][t]


def main():
    # Problem data
    S = [2, 3, 5, 7, 8]
    t = 19

    print("SUBSET SUM Problem Analysis")
    print("==========================")

    # Part (a): Check if S has a subset summing to t
    has_solution, solution = verify_subset_sum(S, t)

    # Part (b): Demonstrate brute force complexity
    brute_force_complexity([10, 20, 30, 50, 100])

    # Demonstrate DP solution
    print("\nApplying dynamic programming to our problem:")
    has_dp_solution = demonstrate_dp_solution(S, t)
    print(f"\nDP Solution exists: {has_dp_solution}")

    # Part (c): Analyze DP complexity
    analyze_dynamic_programming_complexity()


if __name__ == "__main__":
    main()
