# Probability-Playground-With-Python
 Complete probability implementation in pure Python. Master core concepts without libraries: basic probability, event relationships, probability rules, classical/empirical types, card simulations, and Bayesian updating. Learn math-to-code translation through medical diagnosis &amp; card game examples. Essential for data science/AI foundations.
# ProbabilityLab: Complete Probability Implementation in Pure Python

A comprehensive implementation of core probability concepts using only Python (no external libraries). Learn how probability theory translates directly to code through hands-on examples.

## 📋 Overview

This project implements 6 fundamental probability concepts through practical Python code:
1. Basic Probability Formulas
2. Probability Type Identification
3. Event Relationship Analysis
4. Probability Rules Implementation
5. Card Draw Simulations
6. Bayesian Probability Updating

## 🎯 Objectives

- **Understand** how probability theory translates to code
- **Implement** core concepts without external libraries
- **Practice** problem-solving with mathematical concepts
- **Build** foundational skills for data science and AI

## 📁 Project Structure

### Task 1: Basic Probability (`basic_probability.py`)
**Function:** `calculate_basic_probability(favorable, total)`
- Implements the fundamental probability formula: P(event) = favorable/total
- Includes error handling for invalid inputs
- Returns probability as float between 0 and 1

### Task 2: Probability Types (`probability_types.py`)
**Class:** `ProbabilityCalculator`
- **Classical Probability:** `classical_probability(event_outcomes, sample_space)`
  - Both parameters are lists
  - Assumes all outcomes equally likely
  - Example: P(even number on dice) = 3/6 = 0.5
- **Empirical Probability:** `empirical_probability(observed_frequencies)`
  - Parameter: dictionary with outcomes as keys and counts as values
  - Returns dictionary with probabilities for each outcome
  - Example: {'Heads': 520, 'Tails': 480} → {'Heads': 0.52, 'Tails': 0.48}
- **Type Identification:** `identify_probability_type(description)`
  - Takes text description, returns "Classical", "Empirical", or "Subjective"
  - Uses keyword matching

### Task 3: Event Relationships (`event_relationships.py`)
**Functions:**
- `are_mutually_exclusive(eventA, eventB, sample_space)`
  - Returns True if events cannot occur together
  - Example: EventA = [1, 3, 5] (odd dice), EventB = [2, 4, 6] (even dice)
- `are_independent(pA, pB, pA_and_B)`
  - Returns True if P(A and B) = P(A) * P(B)
  - Tolerance of 0.001 for floating point errors
- `conditional_probability(pA_and_B, pA)`
  - Returns P(B|A) = P(A and B) / P(A)
  - Handles division by zero

**Example Problem:** Card deck analysis
- Event A: Drawing a Heart (13 cards)
- Event B: Drawing a Face card (12 cards)
- Event C: Drawing a Red card (26 cards)
- Determine which events are mutually exclusive, independent, and calculate conditional probabilities

### Task 4: Probability Rules (`probability_rules.py`)
**Functions:**
- **Addition Rule:** `addition_rule(pA, pB, pA_and_B)`
  - P(A or B) = P(A) + P(B) - P(A and B)
  - For mutually exclusive: P(A and B) = 0
- **Multiplication Rule:** `multiplication_rule(pA, pB, are_independent)`
  - If independent: P(A and B) = P(A) * P(B)
  - If dependent: P(A and B) = P(A) * P(B|A)
- **Complement Rule:** `complement_rule(pA)`
  - P(not A) = 1 - P(A)

**Application Problem:** Student survey analysis
- Class of 60 students
- 30 like Math, 25 like Science, 10 like both
- Calculate: P(Math or Science), P(neither), P(Science | Math)

### Task 5: Card Simulations (`card_simulations.py`)
**Functions:**
- `create_deck()`: Returns list of 52 cards as strings "AH" (Ace of Hearts), "2S", etc.
- `simulate_draws(deck, num_draws, with_replacement)`
  - Simulates drawing cards
  - If with_replacement=True, card goes back after draw
  - Returns list of drawn cards
- `calculate_experimental_probability(draws, target_condition)`
  - Calculates probability based on simulation
  - target_condition is function that takes card and returns boolean
- `calculate_theoretical_probability(num_target, total_cards, draws, with_replacement)`
  - Calculates what probability should be theoretically

**Simulation Tasks:**
1. Draw 1000 cards with replacement, find P(Heart)
2. Draw 1000 cards without replacement, find P(Ace)
3. Draw two cards without replacement, find P(both are same suit)
4. Compare experimental vs theoretical probabilities

### Task 6: Bayesian Updating (`bayesian_updating.py`)
**Class:** `BayesianUpdater`
- `__init__(self, prior, likelihood)`
  - prior: dict of hypotheses and their probabilities
  - likelihood: dict of P(evidence|hypothesis)
- `update(self, evidence_observed)`
  - Updates probabilities based on observed evidence
  - Returns posterior probabilities
- `normalize(self, probabilities)`
  - Ensures probabilities sum to 1

**Medical Diagnosis Problem:**
- Disease prevalence: 2% of population
- Test accuracy: 95% true positive, 3% false positive
- Implement:
  1. Prior: P(Disease) = 0.02, P(No Disease) = 0.98
  2. Update with positive test result
  3. Update with negative test result (after positive)
  4. Show how probability changes with multiple tests

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- No external libraries required

### Running the Code
Each task can be run independently:
```python
# Example for Task 1
python basic_probability.py

# Example for Task 2
python probability_types.py

# Example for Task 6
python bayesian_updating.py
