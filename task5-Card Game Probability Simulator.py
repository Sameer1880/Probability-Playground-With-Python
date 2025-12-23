# ==================== PURE PYTHON - NO IMPORTS ====================

# Simple random number generator (linear congruential generator)
class SimpleRandom:
    def __init__(self, seed=None):
        self.state = seed if seed is not None else 12345
        self.m = 2**31 - 1  # modulus
        self.a = 1103515245  # multiplier
        self.c = 12345       # increment
    
    def randint(self, a, b):
        """Generate random integer between a and b (inclusive)"""
        self.state = (self.a * self.state + self.c) % self.m
        rand_num = self.state / self.m  # Between 0 and 1
        return a + int(rand_num * (b - a + 1))
    
    def choice(self, items):
        """Randomly choose one item from list"""
        if not items:
            return None
        index = self.randint(0, len(items) - 1)
        return items[index]


# ==================== BASIC PROBABILITY ====================
def basic_probability(favorable, total):
    """Calculate P(event) = favorable / total"""
    if total == 0:
        return 0.0
    return favorable / total


# ==================== PROBABILITY TYPES ====================
def classical_probability(event_outcomes, sample_space):
    """Probability when all outcomes equally likely"""
    if len(sample_space) == 0:
        return 0.0
    return len(event_outcomes) / len(sample_space)


def empirical_probability(observed_data):
    """Probability from observed data"""
    total = sum(observed_data.values())
    if total == 0:
        return {k: 0.0 for k in observed_data}
    
    probabilities = {}
    for outcome, count in observed_data.items():
        probabilities[outcome] = count / total
    return probabilities


# ==================== EVENT RELATIONSHIPS ====================
def are_mutually_exclusive(eventA, eventB):
    """Check if events cannot occur together"""
    # Convert lists to sets and check intersection
    for a in eventA:
        for b in eventB:
            if a == b:
                return False
    return True


def are_independent(pA, pB, pA_and_B):
    """Check if P(A and B) = P(A) * P(B)"""
    expected = pA * pB
    return abs(pA_and_B - expected) < 0.001


def conditional_probability(pA_and_B, pA):
    """Calculate P(B|A) = P(A and B) / P(A)"""
    if pA == 0:
        return 0.0
    return pA_and_B / pA


# ==================== PROBABILITY RULES ====================
def addition_rule(pA, pB, pA_and_B):
    """P(A or B) = P(A) + P(B) - P(A and B)"""
    return pA + pB - pA_and_B


def multiplication_rule(pA, pB, is_independent, pB_given_A=None):
    """
    Calculate P(A and B)
    Independent: P(A and B) = P(A) * P(B)
    Dependent: P(A and B) = P(A) * P(B|A)
    """
    if is_independent:
        return pA * pB
    else:
        if pB_given_A is None:
            return 0.0
        return pA * pB_given_A


def complement_rule(pA):
    """P(not A) = 1 - P(A)"""
    return 1 - pA


# ==================== CARD SIMULATION ====================
def create_deck():
    """Create a standard 52-card deck"""
    suits = ['H', 'D', 'C', 'S']  # Hearts, Diamonds, Clubs, Spades
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    return deck


def simulate_draws(deck, num_draws, with_replacement=True, random_gen=None):
    """Simulate drawing cards from deck using our own random generator"""
    if random_gen is None:
        random_gen = SimpleRandom()
    
    working_deck = deck.copy()
    draws = []
    
    for _ in range(num_draws):
        if len(working_deck) == 0:
            break
        
        # Draw random card using our generator
        index = random_gen.randint(0, len(working_deck) - 1)
        card = working_deck[index]
        draws.append(card)
        
        if not with_replacement:
            # Remove the card
            working_deck.pop(index)
    
    return draws


def experimental_probability(draws, condition_func):
    """Calculate probability from simulation results"""
    if not draws:
        return 0.0
    
    favorable = 0
    for card in draws:
        if condition_func(card):
            favorable += 1
    
    return favorable / len(draws)


def theoretical_probability(num_target, total_cards, num_draws, with_replacement):
    """Calculate what probability should be theoretically"""
    if with_replacement:
        # Probability stays constant
        return num_target / total_cards
    else:
        if num_draws == 1:
            return num_target / total_cards
        elif num_draws == 2:
            # For drawing two without replacement
            return (num_target / total_cards) * ((num_target - 1) / (total_cards - 1))
        else:
            # Simplified
            return num_target / total_cards


# ==================== TEST EXAMPLES ====================
def run_demonstrations():
    print("=== PROBABILITY CONCEPTS - PURE PYTHON (NO IMPORTS) ===\n")
    
    # Create our own random number generator
    my_random = SimpleRandom(seed=42)
    
    # 1. BASIC EXAMPLES
    print("1. Basic Probability Examples:")
    print(f"   P(rolling 6 on die) = {basic_probability(1, 6):.4f}")
    print(f"   P(drawing Ace) = {basic_probability(4, 52):.4f}")
    print()
    
    # 2. CLASSICAL PROBABILITY
    print("2. Classical Probability:")
    dice = [1, 2, 3, 4, 5, 6]
    primes = [2, 3, 5]  # Prime numbers on dice
    p_prime = classical_probability(primes, dice)
    print(f"   P(prime on die) = {p_prime:.4f}")
    print()
    
    # 3. EMPIRICAL PROBABILITY
    print("3. Empirical Probability:")
    coin_data = {'Heads': 487, 'Tails': 513}
    p_coin = empirical_probability(coin_data)
    print(f"   Coin flip data: {coin_data}")
    print(f"   Probabilities: {p_coin}")
    print()
    
    # 4. EVENT RELATIONSHIPS
    print("4. Event Relationships:")
    
    # Create sample events
    hearts = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH']
    face_cards = ['JH', 'QH', 'KH', 'JD', 'QD', 'KD', 'JC', 'QC', 'KC', 'JS', 'QS', 'KS']
    
    # Check if mutually exclusive
    exclusive = are_mutually_exclusive(hearts, face_cards)
    print(f"   Hearts and Face cards mutually exclusive? {exclusive}")
    
    # Calculate some probabilities
    p_heart = len(hearts) / 52
    p_face = len(face_cards) / 52
    p_heart_and_face = 3 / 52  # J, Q, K of hearts
    
    # Check independence
    independent = are_independent(p_heart, p_face, p_heart_and_face)
    print(f"   Hearts and Face cards independent? {independent}")
    
    # Conditional probability
    p_face_given_heart = conditional_probability(p_heart_and_face, p_heart)
    print(f"   P(Face | Heart) = {p_face_given_heart:.4f}")
    print()
    
    # 5. PROBABILITY RULES
    print("5. Probability Rules:")
    
    # Addition rule
    p_heart_or_face = addition_rule(p_heart, p_face, p_heart_and_face)
    print(f"   P(Heart or Face) = {p_heart:.4f} + {p_face:.4f} - {p_heart_and_face:.4f} = {p_heart_or_face:.4f}")
    
    # Multiplication rule (dependent - drawing two hearts without replacement)
    p_heart_then_heart = multiplication_rule(p_heart, 12/51, False, pB_given_A=12/51)
    print(f"   P(Heart then Heart) = {p_heart:.4f} × {12/51:.4f} = {p_heart_then_heart:.4f}")
    
    # Complement rule
    p_not_heart = complement_rule(p_heart)
    print(f"   P(not Heart) = 1 - {p_heart:.4f} = {p_not_heart:.4f}")
    print()
    
    # 6. CARD SIMULATION
    print("6. Card Draw Simulations:")
    deck = create_deck()
    
    # Task 1: Draw 500 cards with replacement, find P(Heart)
    print("   Task 1: P(Heart) with replacement")
    draws1 = simulate_draws(deck, 500, with_replacement=True, random_gen=my_random)
    p_heart_exp = experimental_probability(draws1, lambda c: c.endswith('H'))
    p_heart_theo = theoretical_probability(13, 52, 1, True)
    print(f"     Experimental: {p_heart_exp:.4f}")
    print(f"     Theoretical:  {p_heart_theo:.4f}")
    
    # Task 2: Draw 500 cards without replacement, find P(Ace)
    print("   Task 2: P(Ace) without replacement")
    draws2 = simulate_draws(deck, 500, with_replacement=False, random_gen=SimpleRandom(seed=123))
    p_ace_exp = experimental_probability(draws2, lambda c: c.startswith('A'))
    p_ace_theo = theoretical_probability(4, 52, 1, False)
    print(f"     Experimental: {p_ace_exp:.4f}")
    print(f"     Theoretical:  {p_ace_theo:.4f}")
    
    # Task 3: Draw two cards without replacement, P(both same suit)
    print("   Task 3: P(both same suit) without replacement")
    
    same_suit_count = 0
    trials = 5000
    
    for i in range(trials):
        # Use different seed for each trial
        trial_random = SimpleRandom(seed=i)
        two_draws = simulate_draws(deck, 2, with_replacement=False, random_gen=trial_random)
        if len(two_draws) == 2:
            suit1 = two_draws[0][-1]  # Get suit (last character)
            suit2 = two_draws[1][-1]
            if suit1 == suit2:
                same_suit_count += 1
    
    p_same_suit_exp = same_suit_count / trials
    p_same_suit_theo = (13/52) * (12/51) * 4  # 4 suits
    
    print(f"     Experimental: {p_same_suit_exp:.4f}")
    print(f"     Theoretical:  {p_same_suit_theo:.4f}")
    print()


def student_survey_example():
    """Practical example: Student survey"""
    print("=== PRACTICAL EXAMPLE: STUDENT SURVEY ===")
    print("60 students surveyed:")
    print("- 30 like Math")
    print("- 25 like Science")
    print("- 10 like both")
    print()
    
    total = 60
    p_math = 30/60
    p_science = 25/60
    p_both = 10/60
    
    print("Calculations:")
    print(f"1. P(Math) = {p_math:.4f}")
    print(f"2. P(Science) = {p_science:.4f}")
    print(f"3. P(both) = {p_both:.4f}")
    print()
    
    # Using probability rules
    p_math_or_science = addition_rule(p_math, p_science, p_both)
    print(f"Using Addition Rule:")
    print(f"P(Math or Science) = {p_math:.4f} + {p_science:.4f} - {p_both:.4f} = {p_math_or_science:.4f}")
    print()
    
    p_neither = complement_rule(p_math_or_science)
    print(f"Using Complement Rule:")
    print(f"P(neither) = 1 - {p_math_or_science:.4f} = {p_neither:.4f}")
    print()
    
    p_science_given_math = conditional_probability(p_both, p_math)
    print(f"Using Conditional Probability:")
    print(f"P(Science | Math) = {p_both:.4f} ÷ {p_math:.4f} = {p_science_given_math:.4f}")
    print(f"Interpretation: {p_science_given_math*100:.1f}% of Math-likers also like Science")
    print()


def simple_dice_game():
    """Simple dice probability example"""
    print("=== SIMPLE DICE GAME ===")
    print("Rolling two fair dice:")
    
    # All possible outcomes
    outcomes = []
    for die1 in range(1, 7):
        for die2 in range(1, 7):
            outcomes.append((die1, die2))
    
    total_outcomes = len(outcomes)
    print(f"Total possible outcomes: {total_outcomes}")
    
    # Event A: Sum is 7
    sum_7 = [(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)]
    p_sum_7 = classical_probability(sum_7, outcomes)
    print(f"P(sum = 7) = {len(sum_7)}/{total_outcomes} = {p_sum_7:.4f}")
    
    # Event B: First die is 4
    first_is_4 = [(4,1), (4,2), (4,3), (4,4), (4,5), (4,6)]
    p_first_4 = classical_probability(first_is_4, outcomes)
    print(f"P(first die = 4) = {len(first_is_4)}/{total_outcomes} = {p_first_4:.4f}")
    
    # Event A and B: Sum is 7 AND first die is 4
    both = [(4,3)]
    p_both_events = classical_probability(both, outcomes)
    print(f"P(sum=7 AND first=4) = {len(both)}/{total_outcomes} = {p_both_events:.4f}")
    
    # Check if independent
    independent = are_independent(p_sum_7, p_first_4, p_both_events)
    print(f"Are these independent? {independent}")
    print()


# Run everything
if __name__ == "__main__":
    run_demonstrations()
    student_survey_example()
    simple_dice_game()
    
    print("=== SUMMARY ===")
    print("✓ All code uses pure Python (no imports)")
    print("✓ Implements all probability concepts mathematically")
    print("✓ Includes our own random number generator")
    print("✓ Shows theory → code translation")
    print("✓ Practical examples with calculations")