# Description of the Guessing AI

This Python code implements a simple AI to guess a randomly selected number between 0 and 100.  The AI employs a binary search strategy to efficiently narrow down the possible numbers.

**Functionality:**

* **`GuessingAI` Class:**  This class encapsulates the AI's logic.
    * **`__init__`:** Initializes the AI's internal state:
        * `lower_bound`: The lowest possible number.
        * `upper_bound`: The highest possible number.
        * `history`: A list to keep track of guesses and results.
        * `attempts`: Count of attempts.
        * `wins`: Count of successful guesses.
    * **`guess`:** Predicts the next number to guess.  Critically, it uses a binary search strategy, selecting the middle number in the remaining range of possibilities.
    * **`learn`:** Updates the `lower_bound` or `upper_bound` based on the result (greater or smaller) of the previous guess.
    * **`reset`:** Resets the AI's internal state for the next game.

* **`run_games` function:**  This function runs multiple games and records results.
    * It handles the file writing for results (appending to existing results).
    * Counts total games played and wins achieved.


**How the AI Works:**

The AI starts by guessing the middle number in the initial range (0-100). If the guess is too low (the target number is greater), it adjusts the lower bound to the guess + 1. If the guess is too high, it adjusts the upper bound to the guess - 1. This process is repeated until the correct number is found or the maximum number of attempts (7 in this case) is reached. The binary search approach guarantees that the AI will find the number efficiently.


**Improvements over a purely random guessing approach:**

The use of a binary search dramatically reduces the number of attempts compared to a purely random guessing approach, leading to much better performance.
