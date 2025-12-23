def addition_rule(pA, pB, pA_and_B):
    """
    Calculate P(A or B) = P(A) + P(B) - P(A and B)
    
    Parameters:
    pA: Probability of event A
    pB: Probability of event B
    pA_and_B: Probability of both A and B occurring
    
    Returns: Probability of A or B occurring
    """
    return pA + pB - pA_and_B


def multiplication_rule(pA, pB, are_independent, pB_given_A=None):
    """
    Calculate P(A and B)
    
    If independent: P(A and B) = P(A) * P(B)
    If dependent: P(A and B) = P(A) * P(B|A)
    
    Parameters:
    pA: Probability of event A
    pB: Probability of event B
    are_independent: Boolean, True if events are independent
    pB_given_A: P(B|A) - only needed when are_independent=False
    
    Returns: Probability of both A and B occurring
    """
    if are_independent:
        return pA * pB
    else:
        # For dependent events, we need P(B|A)
        # pB parameter is not used for dependent case
        if pB_given_A is None:
            raise ValueError("For dependent events, pB_given_A is required")
        return pA * pB_given_A


def complement_rule(pA):
    """
    Calculate P(not A) = 1 - P(A)
    
    Parameters:
    pA: Probability of event A
    
    Returns: Probability of event not A occurring
    """
    return 1 - pA


# Helper function
def calculate_probability(favorable, total):
    """Calculate basic probability"""
    if total == 0:
        return 0.0
    return favorable / total


# Application Problem Solution
print("=== CLASS SURVEY PROBLEM ===")
print("Class: 60 students")
print("- 30 like Math")
print("- 25 like Science")
print("- 10 like both")
print()

total_students = 60
like_math = 30
like_science = 25
like_both = 10

# Calculate probabilities
p_math = calculate_probability(like_math, total_students)
p_science = calculate_probability(like_science, total_students)
p_both = calculate_probability(like_both, total_students)
p_science_given_math = calculate_probability(like_both, like_math)

print("Basic Probabilities:")
print(f"P(Math) = {like_math}/{total_students} = {p_math:.4f}")
print(f"P(Science) = {like_science}/{total_students} = {p_science:.4f}")
print(f"P(Math AND Science) = {like_both}/{total_students} = {p_both:.4f}")
print(f"P(Science|Math) = {like_both}/{like_math} = {p_science_given_math:.4f}")
print()

# 1. Probability a student likes Math OR Science
print("1. Probability a student likes Math OR Science:")
print("   Using Addition Rule: P(Math OR Science) = P(Math) + P(Science) - P(Math AND Science)")
result1 = addition_rule(p_math, p_science, p_both)
print(f"   = {p_math:.4f} + {p_science:.4f} - {p_both:.4f}")
print(f"   = {result1:.4f}")
print(f"   Interpretation: {result1*100:.1f}% of students like Math or Science")
print()

# 2. Probability a student likes neither
print("2. Probability a student likes neither Math nor Science:")
print("   Step 1: Find P(Math OR Science) from above = {result1:.4f}")
print("   Step 2: Using Complement Rule: P(neither) = 1 - P(Math OR Science)")
result2 = complement_rule(result1)
print(f"   = 1 - {result1:.4f}")
print(f"   = {result2:.4f}")
print(f"   Interpretation: {result2*100:.1f}% of students like neither subject")
print()

# 3. Probability a Math-liker also likes Science (P(Science|Math))
print("3. Probability a randomly selected Math-liker also likes Science:")
print("   This is conditional probability: P(Science | Math)")
print("   Formula: P(Science AND Math) / P(Math)")
print(f"   = {p_both:.4f} / {p_math:.4f}")
print(f"   = {p_science_given_math:.4f}")
print(f"   Interpretation: {p_science_given_math*100:.1f}% of Math-likers also like Science")
print()

# Additional demonstration using multiplication rule
print("=== DEMONSTRATING MULTIPLICATION RULE ===")
print()

# Are Math and Science preferences independent?
print("Are Math and Science preferences independent?")
print("Check: P(Math AND Science) = P(Math) * P(Science)?")
expected_if_independent = p_math * p_science
print(f"P(Math) * P(Science) = {p_math:.4f} * {p_science:.4f} = {expected_if_independent:.4f}")
print(f"Actual P(Math AND Science) = {p_both:.4f}")
are_independent = abs(p_both - expected_if_independent) < 0.001
print(f"Result: {'Independent' if are_independent else 'Dependent'}")
print()

# Using multiplication rule for independent case (hypothetical)
print("If they were independent:")
print("P(Math AND Science) using multiplication rule:")
result_ind = multiplication_rule(p_math, p_science, are_independent=True)
print(f"  = P(Math) * P(Science) = {result_ind:.4f}")
print()

# Using multiplication rule for dependent case (actual)
print("Since they are actually dependent:")
print("P(Math AND Science) = P(Math) * P(Science|Math)")
# CORRECT: Pass pB_given_A parameter for dependent case
result_dep = multiplication_rule(p_math, None, are_independent=False, pB_given_A=p_science_given_math)
print(f"  = {p_math:.4f} * {p_science_given_math:.4f} = {result_dep:.4f}")
print(f"  This matches P(Math AND Science) = {p_both:.4f}")
print()

# Simple example of using all rules together
print("=== SIMPLE EXAMPLE ===")
print("Example: Rolling a fair 6-sided die")
print("Event A: Getting an even number (2, 4, 6)")
print("Event B: Getting a number greater than 4 (5, 6)")
print()

p_even = 3/6  # P(A)
p_gt4 = 2/6   # P(B)
p_even_and_gt4 = 1/6  # Only 6 is both even and >4

# Addition rule
p_even_or_gt4 = addition_rule(p_even, p_gt4, p_even_and_gt4)
print(f"P(even OR >4) = {p_even:.3f} + {p_gt4:.3f} - {p_even_and_gt4:.3f} = {p_even_or_gt4:.3f}")

# Check if independent
expected = p_even * p_gt4
is_independent = abs(p_even_and_gt4 - expected) < 0.001
print(f"Are they independent? P(A and B)={p_even_and_gt4:.3f}, P(A)*P(B)={expected:.3f}")
print(f"Result: {'Independent' if is_independent else 'Dependent'}")

# Multiplication rule for independent events
if is_independent:
    p_and = multiplication_rule(p_even, p_gt4, are_independent=True)
    print(f"Using multiplication rule: {p_even:.3f} * {p_gt4:.3f} = {p_and:.3f}")

# Complement rule
p_not_even = complement_rule(p_even)
print(f"P(not even) = 1 - {p_even:.3f} = {p_not_even:.3f}")