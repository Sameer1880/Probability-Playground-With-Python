def are_mutually_exclusive(eventA, eventB, sample_space):
    """
    Check if two events are mutually exclusive (cannot occur together).
    
    Parameters:
    eventA: List of outcomes in event A
    eventB: List of outcomes in event B
    sample_space: List of all possible outcomes
    
    Returns: True if events cannot occur together, False otherwise
    """
    # Convert to sets for efficient intersection check
    setA = set(eventA)
    setB = set(eventB)
    
    # Events are mutually exclusive if they have no common outcomes
    return len(setA.intersection(setB)) == 0


def are_independent(pA, pB, pA_and_B, tolerance=0.001):
    """
    Check if two events are independent.
    
    Events are independent if P(A and B) = P(A) * P(B)
    
    Parameters:
    pA: Probability of event A
    pB: Probability of event B
    pA_and_B: Probability of both A and B occurring
    tolerance: Allowable difference for floating point comparison
    
    Returns: True if independent, False otherwise
    """
    # Calculate expected probability if independent
    expected = pA * pB
    
    # Check if actual probability matches expected (within tolerance)
    return abs(pA_and_B - expected) < tolerance


def conditional_probability(pA_and_B, pA):
    """
    Calculate conditional probability P(B|A) = P(A and B) / P(A)
    
    Parameters:
    pA_and_B: Probability of both A and B occurring
    pA: Probability of event A
    
    Returns: Conditional probability P(B|A), or 0 if division by zero
    """
    if pA == 0:
        return 0.0
    
    return pA_and_B / pA


# Helper function to calculate basic probability
def calculate_probability(favorable, total):
    """Calculate basic probability"""
    if total == 0:
        return 0.0
    return favorable / total


# Test with card deck problem
print("=== CARD DECK ANALYSIS ===")
print("Deck: 52 cards")
print("Event A: Heart (13 cards)")
print("Event B: Face card (12 cards)")
print("Event C: Red card (26 cards)")
print()

# Define the deck
all_cards = list(range(1, 53))  # Cards numbered 1 to 52 for simplicity

# Define events (in real terms)
# Let's say: 
# Cards 1-13: Hearts (A, 2-10, J, Q, K)
# Cards 14-26: Diamonds
# Cards 27-39: Spades
# Cards 40-52: Clubs
# Face cards: J, Q, K of each suit (positions: 11, 12, 13 in each suit)

# Create actual lists for events
hearts = list(range(1, 14))  # Cards 1-13: Hearts
face_cards = []
for suit_start in [1, 14, 27, 40]:  # Start of each suit
    face_cards.extend([suit_start + 10, suit_start + 11, suit_start + 12])  # J, Q, K

red_cards = list(range(1, 27))  # Cards 1-26: Hearts + Diamonds (Red cards)

print("1. Checking Mutually Exclusive Events:")
print("-" * 40)

# Check A vs B (Heart vs Face card)
print("Are Hearts and Face cards mutually exclusive?")
print("Heart cards:", hearts[:5], "...")  # Show first 5
print("Face cards:", face_cards[:5], "...")  # Show first 5
print("Result:", are_mutually_exclusive(hearts, face_cards, all_cards))
print("Explanation: Some hearts are face cards (J, Q, K of hearts)")
print()

# Check B vs C (Face card vs Red card)
print("Are Face cards and Red cards mutually exclusive?")
print("Face cards:", face_cards[:5], "...")
print("Red cards:", red_cards[:5], "...")
print("Result:", are_mutually_exclusive(face_cards, red_cards, all_cards))
print("Explanation: Some face cards are red (J, Q, K of hearts and diamonds)")
print()

# Check A vs C (Heart vs Red card) - Actually not mutually exclusive!
print("Are Hearts and Red cards mutually exclusive?")
print("Heart cards:", hearts[:5], "...")
print("Red cards:", red_cards[:5], "...")
print("Result:", are_mutually_exclusive(hearts, red_cards, all_cards))
print("Explanation: All hearts are red cards")
print()

print("2. Calculating Probabilities:")
print("-" * 40)

# Calculate basic probabilities
p_heart = calculate_probability(13, 52)  # 13 hearts / 52 cards
p_face = calculate_probability(12, 52)   # 12 face cards / 52 cards
p_red = calculate_probability(26, 52)    # 26 red cards / 52 cards

print(f"P(Heart) = 13/52 = {p_heart:.4f}")
print(f"P(Face card) = 12/52 = {p_face:.4f}")
print(f"P(Red card) = 26/52 = {p_red:.4f}")

# Calculate joint probabilities
# Heart AND Face card: 3 cards (J, Q, K of hearts)
p_heart_and_face = calculate_probability(3, 52)
print(f"P(Heart AND Face) = 3/52 = {p_heart_and_face:.4f}")

# Heart AND Red card: All hearts are red, so 13 cards
p_heart_and_red = calculate_probability(13, 52)
print(f"P(Heart AND Red) = 13/52 = {p_heart_and_red:.4f}")

# Face AND Red card: 6 cards (3 hearts + 3 diamonds that are face cards)
p_face_and_red = calculate_probability(6, 52)
print(f"P(Face AND Red) = 6/52 = {p_face_and_red:.4f}")
print()

print("3. Checking Independent Events:")
print("-" * 40)

# Check if Heart and Face card are independent
print("Are Hearts and Face cards independent?")
print(f"P(Heart) * P(Face) = {p_heart:.4f} * {p_face:.4f} = {p_heart * p_face:.4f}")
print(f"P(Heart AND Face) = {p_heart_and_face:.4f}")
print("Result:", are_independent(p_heart, p_face, p_heart_and_face))
print("Explanation:", "Independent" if are_independent(p_heart, p_face, p_heart_and_face) else "Not independent")
print()

# Check if Heart and Red card are independent
print("Are Hearts and Red cards independent?")
print(f"P(Heart) * P(Red) = {p_heart:.4f} * {p_red:.4f} = {p_heart * p_red:.4f}")
print(f"P(Heart AND Red) = {p_heart_and_red:.4f}")
print("Result:", are_independent(p_heart, p_red, p_heart_and_red))
print("Explanation:", "Independent" if are_independent(p_heart, p_red, p_heart_and_red) else "Not independent")
print()

print("4. Calculating Conditional Probabilities:")
print("-" * 40)

# Calculate P(Face card | Heart)
print("Probability of Face card GIVEN Heart:")
print(f"P(Face | Heart) = P(Face AND Heart) / P(Heart)")
print(f"                = {p_heart_and_face:.4f} / {p_heart:.4f}")
result = conditional_probability(p_heart_and_face, p_heart)
print(f"                = {result:.4f}")
print(f"Interpretation: If you know a card is a heart, there's a {result*100:.1f}% chance it's a face card")
print()

# Calculate P(Heart | Face card)
print("Probability of Heart GIVEN Face card:")
print(f"P(Heart | Face) = P(Heart AND Face) / P(Face)")
print(f"                = {p_heart_and_face:.4f} / {p_face:.4f}")
result2 = conditional_probability(p_heart_and_face, p_face)
print(f"                = {result2:.4f}")
print(f"Interpretation: If you know a card is a face card, there's a {result2*100:.1f}% chance it's a heart")
print()

# Summary
print("=== SUMMARY ===")
print("1. No events are mutually exclusive (they can overlap)")
print("2. Hearts and Face cards are NOT independent")
print("3. P(Face card | Heart) = 3/13 ≈ 0.2308")