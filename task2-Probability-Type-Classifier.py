class ProbabilityCalculator:
    def classical_probability(self, event_outcomes, sample_space):
        """Calculate probability when all outcomes are equally likely."""
        if len(sample_space) == 0:
            return 0.0
        return len(event_outcomes) / len(sample_space)
    
    def empirical_probability(self, observed_frequencies):
        """Calculate probability from observed data."""
        if not observed_frequencies:
            return {}
        
        total = sum(observed_frequencies.values())
        if total == 0:
            return {k: 0.0 for k in observed_frequencies.keys()}
        
        probabilities = {}
        for outcome, count in observed_frequencies.items():
            probabilities[outcome] = count / total
        
        return probabilities
    
    def identify_probability_type(self, description):
        """Identify type of probability from description."""
        desc_lower = description.lower()
        
        # Check for empirical (observed data)
        empirical_keywords = ['observed', 'data', 'survey', 'experiment', 
                             'collected', 'records', 'study', 'trial',
                             'toss', 'roll', 'measure', 'recorded',
                             'based on', 'observations']
        
        # Check for classical (equally likely)
        classical_keywords = ['equally likely', 'fair', 'balanced', 'random',
                             'theoretical', 'all outcomes', 'all cards',
                             'all faces', 'symmetrical']
        
        # Check for subjective (personal feeling)
        subjective_keywords = ['feel', 'think', 'believe', 'guess', 
                              'estimate', 'intuition', 'gut feeling',
                              'probably', 'likely', 'maybe', 'perhaps',
                              'might']
        
        # Check each type
        for word in empirical_keywords:
            if word in desc_lower:
                return "Empirical"
        
        for word in classical_keywords:
            if word in desc_lower:
                return "Classical"
        
        for word in subjective_keywords:
            if word in desc_lower:
                return "Subjective"
        
        return "Unknown"


# Test code exactly as specified
# Create calculator
calc = ProbabilityCalculator()

# Classical example
dice_sample = [1, 2, 3, 4, 5, 6]
even_event = [2, 4, 6]
print(calc.classical_probability(even_event, dice_sample))  # Should be 0.5

# Empirical example
weather_data = {'Sunny': 280, 'Rainy': 70, 'Cloudy': 15}
print(calc.empirical_probability(weather_data))

# Identification
print(calc.identify_probability_type("Based on 1000 coin toss observations"))  # Empirical
print(calc.identify_probability_type("All cards equally likely to be drawn"))   # Classical
print(calc.identify_probability_type("I feel it might rain today"))             # Subjective