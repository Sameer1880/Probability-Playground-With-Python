def calculate_basic_probability(favorable, total):
    """
    Calculate probability of an event happening.
    
    Formula: probability = favorable outcomes / total outcomes
    
    Example: 
    - Probability of rolling a 3 on a die:
      favorable = 1 (only one 3 on a die)
      total = 6 (6 sides on a die)
      probability = 1/6 ≈ 0.1667
    """
    
    # Check if total is 0 (can't divide by zero)
    if total == 0:
        return 0.0
    
    # Make sure favorable isn't negative
    if favorable < 0:
        favorable = 0
    
    # Make sure favorable isn't more than total
    if favorable > total:
        favorable = total
    
    # Calculate probability
    probability = favorable / total
    
    return probability


# Simple examples
print("=== Simple Probability Examples ===")
print()

# Example 1: Coin toss
print("1. Coin Toss:")
print("Probability of heads when tossing a coin")
favorable = 1  # 1 head
total = 2      # 2 sides total
prob = calculate_basic_probability(favorable, total)
print(f"   Favorable: {favorable}, Total: {total}")
print(f"   Probability: {prob}")
print()

# Example 2: Dice roll
print("2. Dice Roll:")
print("Probability of rolling a 5 on a 6-sided die")
favorable = 1  # only one 5 on a die
total = 6      # 6 sides total
prob = calculate_basic_probability(favorable, total)
print(f"   Favorable: {favorable}, Total: {total}")
print(f"   Probability: {prob:.4f} (that's {prob*100:.1f}%)")
print()

# Example 3: Deck of cards
print("3. Deck of Cards:")
print("Probability of drawing a heart")
favorable = 13  # 13 hearts in a deck
total = 52      # 52 cards total
prob = calculate_basic_probability(favorable, total)
print(f"   Favorable: {favorable}, Total: {total}")
print(f"   Probability: {prob:.4f} (that's 1/4 or 25%)")
print()

# Example 4: Impossible event
print("4. Impossible Event:")
print("Probability of rolling a 7 on a 6-sided die")
favorable = 0  # no 7 on a regular die
total = 6
prob = calculate_basic_probability(favorable, total)
print(f"   Favorable: {favorable}, Total: {total}")
print(f"   Probability: {prob} (0 means impossible)")
print()

# Example 5: Certain event
print("5. Certain Event:")
print("Probability of rolling 1-6 on a 6-sided die")
favorable = 6  # all numbers are 1-6
total = 6
prob = calculate_basic_probability(favorable, total)
print(f"   Favorable: {favorable}, Total: {total}")
print(f"   Probability: {prob} (1 means certain)")
print()

# Interactive example
print("=== Try It Yourself ===")
print("Let's calculate the probability of something!")

try:
    # Get user input
    fav = int(input("How many ways can it happen? Example: For heads on a coin, enter 1: "))
    tot = int(input("How many total possibilities? Example: For a coin, enter 2: "))
    
    # Calculate probability
    result = calculate_basic_probability(fav, tot)
    
    # Show results
    print(f"\nResult:")
    print(f"Probability = {fav}/{tot} = {result:.4f}")
    print(f"That's {result*100:.1f}%")
    
    # Simple interpretation
    if result == 0:
        print("This is impossible!")
    elif result == 1:
        print("This is certain to happen!")
    elif result < 0.5:
        print("This is unlikely.")
    elif result > 0.5:
        print("This is likely.")
    else:
        print("This has an equal chance of happening or not.")
        
except ValueError:
    print("Please enter whole numbers only!")