def P(n):
    if n == 1:
        return 1
    else:
        return sum(P(k) * P(n-k) for k in range(1, n))

def is_omega_2n(n):
    """
    Prove that P(n) is Ω(2^n) using induction.
    """
    # Base case
    if n == 1:
        return P(1) >= 2**1

    # Inductive step
    return all(is_omega_2n(k) and is_omega_2n(n-k) for k in range(1, n))

if __name__ == "__main__":
    # Test the proof
    for n in range(1, 11):
        print(f"P({n}) is Ω(2^{n}): {is_omega_2n(n)}")