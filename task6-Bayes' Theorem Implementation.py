class BayesianUpdater:
    def __init__(self, prior, likelihood):
        """
        Initialize Bayesian Updater
        
        Parameters:
        prior: dict of hypotheses and their probabilities
        likelihood: dict of P(evidence|hypothesis)
        """
        self.prior = prior.copy()
        self.likelihood = likelihood.copy()
        self.current_belief = prior.copy()
    
    def normalize(self, probabilities):
        """
        Ensure probabilities sum to 1
        """
        total = sum(probabilities.values())
        if total == 0:
            return probabilities
        
        normalized = {}
        for hypothesis, prob in probabilities.items():
            normalized[hypothesis] = prob / total
        
        return normalized
    
    def update(self, evidence_observed):
        """
        Update probabilities based on observed evidence using Bayes' Theorem
        
        Bayes' Theorem: P(H|E) = P(E|H) * P(H) / P(E)
        where P(E) = sum over H of P(E|H) * P(H)
        """
        # Calculate unnormalized posterior
        unnormalized_posterior = {}
        
        for hypothesis in self.current_belief:
            # Get P(E|H) from likelihood
            p_evidence_given_hypothesis = self.likelihood.get(evidence_observed, {}).get(hypothesis, 0)
            
            # P(H) is current belief
            p_hypothesis = self.current_belief[hypothesis]
            
            # Unnormalized posterior: P(E|H) * P(H)
            unnormalized_posterior[hypothesis] = p_evidence_given_hypothesis * p_hypothesis
        
        # Normalize to get posterior
        self.current_belief = self.normalize(unnormalized_posterior)
        
        return self.current_belief.copy()


# Medical Diagnosis Problem Implementation
def medical_diagnosis_example():
    print("=== MEDICAL DIAGNOSIS - BAYESIAN UPDATING ===")
    print("Scenario:")
    print("- Disease prevalence: 2% of population")
    print("- Test accuracy: 95% true positive, 3% false positive")
    print()
    
    # Define hypotheses: Disease (D) and No Disease (¬D)
    hypotheses = ['Disease', 'No Disease']
    
    # Step 1: Prior probabilities
    prior = {
        'Disease': 0.02,      # P(D) = 2%
        'No Disease': 0.98    # P(¬D) = 98%
    }
    
    print("1. PRIOR BELIEFS (before any test):")
    for hypo, prob in prior.items():
        print(f"   P({hypo}) = {prob:.4f} ({prob*100:.1f}%)")
    print()
    
    # Step 2: Likelihoods P(Test Result | Hypothesis)
    # True Positive: P(Positive Test | Disease) = 0.95
    # False Positive: P(Positive Test | No Disease) = 0.03
    # True Negative: P(Negative Test | No Disease) = 1 - 0.03 = 0.97
    # False Negative: P(Negative Test | Disease) = 1 - 0.95 = 0.05
    
    likelihood = {
        'Positive': {
            'Disease': 0.95,      # True Positive Rate
            'No Disease': 0.03    # False Positive Rate
        },
        'Negative': {
            'Disease': 0.05,      # False Negative Rate (1 - 0.95)
            'No Disease': 0.97    # True Negative Rate (1 - 0.03)
        }
    }
    
    print("2. TEST CHARACTERISTICS:")
    print("   P(Positive | Disease) = 0.95 (True Positive Rate)")
    print("   P(Positive | No Disease) = 0.03 (False Positive Rate)")
    print("   P(Negative | Disease) = 0.05 (False Negative Rate)")
    print("   P(Negative | No Disease) = 0.97 (True Negative Rate)")
    print()
    
    # Create Bayesian Updater
    doctor = BayesianUpdater(prior, likelihood)
    
    # Step 3: First test comes back POSITIVE
    print("3. FIRST TEST RESULT: POSITIVE")
    posterior_positive = doctor.update('Positive')
    
    print("   Bayes' Theorem Calculation:")
    print("   P(Disease | Positive) = P(Positive | Disease) * P(Disease) / P(Positive)")
    print(f"                         = 0.95 * 0.02 / [0.95*0.02 + 0.03*0.98]")
    print(f"                         = 0.019 / 0.0484")
    print(f"                         = {posterior_positive['Disease']:.4f}")
    
    print("\n   Updated beliefs after positive test:")
    for hypo, prob in posterior_positive.items():
        print(f"   P({hypo} | Positive) = {prob:.4f} ({prob*100:.1f}%)")
    print()
    
    # Step 4: Second test comes back NEGATIVE
    print("4. SECOND TEST RESULT: NEGATIVE (after positive)")
    posterior_negative = doctor.update('Negative')
    
    print("   Updated beliefs after negative test:")
    for hypo, prob in posterior_negative.items():
        print(f"   P({hypo} | Positive then Negative) = {prob:.4f} ({prob*100:.1f}%)")
    print()
    
    # Step 5: Show multiple test scenarios
    print("5. MULTIPLE TEST SCENARIOS:")
    
    # Reset to prior
    doctor2 = BayesianUpdater(prior, likelihood)
    
    test_sequences = [
        ['Positive'],                           # 1 positive
        ['Positive', 'Positive'],               # 2 positives
        ['Positive', 'Negative'],               # Mixed
        ['Negative'],                           # 1 negative
        ['Negative', 'Negative'],               # 2 negatives
    ]
    
    for i, sequence in enumerate(test_sequences):
        # Reset for each sequence
        doctor2 = BayesianUpdater(prior, likelihood)
        
        for test in sequence:
            doctor2.update(test)
        
        final_prob = doctor2.current_belief['Disease']
        
        print(f"   Tests: {sequence}")
        print(f"   Final P(Disease) = {final_prob:.6f} ({final_prob*100:.2f}%)")
        print()


def spam_filter_example():
    """Another Bayesian updating example: Spam filter"""
    print("=== SPAM FILTER - BAYESIAN UPDATING ===")
    print("Scenario: Classifying emails as Spam or Not Spam")
    print()
    
    # Prior: based on email statistics
    prior = {
        'Spam': 0.30,      # 30% of emails are spam
        'Not Spam': 0.70   # 70% are not spam
    }
    
    # Likelihood: P(word appears | email type)
    likelihood = {
        'word: "viagra"': {
            'Spam': 0.80,      # 80% of spam emails contain "viagra"
            'Not Spam': 0.01   # 1% of non-spam emails contain "viagra"
        },
        'word: "meeting"': {
            'Spam': 0.05,      # 5% of spam emails contain "meeting"
            'Not Spam': 0.40   # 40% of non-spam emails contain "meeting"
        },
        'word: "free"': {
            'Spam': 0.60,      # 60% of spam emails contain "free"
            'Not Spam': 0.10   # 10% of non-spam emails contain "free"
        }
    }
    
    # Create spam filter
    filter = BayesianUpdater(prior, likelihood)
    
    print("Initial beliefs:")
    for hypo, prob in prior.items():
        print(f"  P({hypo}) = {prob:.4f}")
    print()
    
    # Update with evidence
    print("1. Email contains 'viagra':")
    beliefs1 = filter.update('word: "viagra"')
    print(f"   P(Spam | 'viagra') = {beliefs1['Spam']:.4f}")
    print()
    
    print("2. Then we see it also contains 'meeting':")
    beliefs2 = filter.update('word: "meeting"')
    print(f"   P(Spam | 'viagra' and 'meeting') = {beliefs2['Spam']:.4f}")
    print()
    
    print("3. Then we see it also contains 'free':")
    beliefs3 = filter.update('word: "free"')
    print(f"   P(Spam | all three words) = {beliefs3['Spam']:.4f}")
    print()


def coin_bias_example():
    """Bayesian updating for coin bias detection"""
    print("=== COIN BIAS DETECTION ===")
    print("Scenario: Determining if a coin is fair or biased")
    print()
    
    # Hypotheses about the coin
    # Each hypothesis: P(Heads) = probability
    prior = {
        'Fair (P=0.5)': 0.70,      # 70% chance coin is fair
        'Biased Heads (P=0.7)': 0.15,  # 15% chance biased toward heads
        'Biased Tails (P=0.3)': 0.15   # 15% chance biased toward tails
    }
    
    # Likelihood function for coin flips
    def coin_likelihood(num_heads, num_flips, p_heads):
        """Probability of getting num_heads out of num_flips if P(Heads)=p_heads"""
        # For simplicity, we'll use binomial probability
        # P(k heads in n flips) = C(n,k) * p^k * (1-p)^(n-k)
        
        # Since we're only comparing probabilities, we can ignore the binomial coefficient
        # as it cancels out in normalization
        return (p_heads ** num_heads) * ((1 - p_heads) ** (num_flips - num_heads))
    
    # Create simple test
    print("Coin flip experiment:")
    print("Prior beliefs:")
    for hypo, prob in prior.items():
        print(f"  {hypo}: {prob:.4f}")
    print()
    
    # Simulate flipping the coin 10 times, getting 7 heads
    num_flips = 10
    num_heads = 7
    
    print(f"Flip coin {num_flips} times, get {num_heads} heads.")
    
    # Calculate likelihoods for this evidence
    likelihoods = {
        'Fair (P=0.5)': coin_likelihood(num_heads, num_flips, 0.5),
        'Biased Heads (P=0.7)': coin_likelihood(num_heads, num_flips, 0.7),
        'Biased Tails (P=0.3)': coin_likelihood(num_heads, num_flips, 0.3)
    }
    
    print("\nLikelihoods for this evidence:")
    for hypo, like in likelihoods.items():
        print(f"  P({num_heads} heads in {num_flips} | {hypo}) = {like:.6f}")
    print()
    
    # Calculate posterior manually to show Bayes' Theorem
    unnormalized = {}
    for hypo in prior:
        unnormalized[hypo] = prior[hypo] * likelihoods[hypo]
    
    total = sum(unnormalized.values())
    posterior = {}
    for hypo in prior:
        posterior[hypo] = unnormalized[hypo] / total
    
    print("Posterior beliefs after evidence:")
    for hypo, prob in posterior.items():
        print(f"  {hypo}: {prob:.4f}")
    print()
    
    # Show how beliefs would update with more flips
    print("If we flip 90 more times and get 63 heads (total 70/100):")
    total_flips = 100
    total_heads = 70
    
    likelihoods2 = {
        'Fair (P=0.5)': coin_likelihood(total_heads, total_flips, 0.5),
        'Biased Heads (P=0.7)': coin_likelihood(total_heads, total_flips, 0.7),
        'Biased Tails (P=0.3)': coin_likelihood(total_heads, total_flips, 0.3)
    }
    
    unnormalized2 = {}
    for hypo in prior:
        unnormalized2[hypo] = prior[hypo] * likelihoods2[hypo]
    
    total2 = sum(unnormalized2.values())
    posterior2 = {}
    for hypo in prior:
        posterior2[hypo] = unnormalized2[hypo] / total2
    
    print("Final beliefs after 100 flips:")
    for hypo, prob in posterior2.items():
        print(f"  {hypo}: {prob:.4f}")


def simple_bayes_calculator():
    """Simple interactive Bayes' Theorem calculator"""
    print("\n=== BAYES' THEOREM CALCULATOR ===")
    print("Formula: P(A|B) = P(B|A) * P(A) / P(B)")
    print()
    
    try:
        # Get user input
        p_a = float(input("Enter P(A) [prior probability of A]: "))
        p_b_given_a = float(input("Enter P(B|A) [probability of B given A]: "))
        p_b_given_not_a = float(input("Enter P(B|not A) [probability of B given not A]: "))
        
        # Calculate P(B) = P(B|A)*P(A) + P(B|not A)*P(not A)
        p_not_a = 1 - p_a
        p_b = (p_b_given_a * p_a) + (p_b_given_not_a * p_not_a)
        
        # Calculate P(A|B) using Bayes' Theorem
        p_a_given_b = (p_b_given_a * p_a) / p_b
        
        print("\nResults:")
        print(f"P(B) = P(B|A)*P(A) + P(B|not A)*P(not A)")
        print(f"     = ({p_b_given_a:.4f} * {p_a:.4f}) + ({p_b_given_not_a:.4f} * {p_not_a:.4f})")
        print(f"     = {p_b:.4f}")
        print()
        print(f"P(A|B) = P(B|A) * P(A) / P(B)")
        print(f"       = ({p_b_given_a:.4f} * {p_a:.4f}) / {p_b:.4f}")
        print(f"       = {p_a_given_b:.4f} ({p_a_given_b*100:.1f}%)")
        
    except ValueError:
        print("Please enter valid numbers between 0 and 1")
    except ZeroDivisionError:
        print("Cannot divide by zero. Check your inputs.")


# Run all examples
if __name__ == "__main__":
    medical_diagnosis_example()
    print("\n" + "="*60 + "\n")
    spam_filter_example()
    print("\n" + "="*60 + "\n")
    coin_bias_example()
    print("\n" + "="*60 + "\n")
    simple_bayes_calculator()
    
    print("\n=== BAYESIAN UPDATING SUMMARY ===")
    print("Key concepts implemented:")
    print("1. Bayes' Theorem: P(H|E) = P(E|H) * P(H) / P(E)")
    print("2. Prior: Initial beliefs before evidence")
    print("3. Likelihood: Probability of evidence given hypothesis")
    print("4. Posterior: Updated beliefs after evidence")
    print("5. Sequential updating: Incorporating multiple pieces of evidence")