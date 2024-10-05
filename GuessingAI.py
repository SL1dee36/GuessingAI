import random
import datetime
import os

def guess_the_number(ai, number):
    guesses = []
    for i in range(7):
        guess = ai.guess()
        guesses.append(guess)
        if guess == number:
            return True, guesses

        if guess < number:
            ai.learn(guess, 1)  # 1 – больше
        else:
            ai.learn(guess, 0)  # 0 – меньше

    return False, guesses


class GuessingAI:
    def __init__(self):
        self.lower_bound = 0
        self.upper_bound = 100
        self.history = []
        self.attempts = 0
        self.wins = 0

    def guess(self):
        if self.lower_bound <= self.upper_bound:
          # Пример улучшения:  предпочтение среднему значению
          guess = (self.lower_bound + self.upper_bound) // 2
          self.attempts += 1
          return guess
        else:
            return -1  # или raise Exception, если логика предполагает ошибку

    def learn(self, guess, result):
        if result == 1:
            self.lower_bound = guess + 1
        elif result == 0:
            self.upper_bound = guess - 1
        self.lower_bound = max(0, self.lower_bound)
        self.upper_bound = min(100, self.upper_bound)
        self.history.append((guess, result))

    def reset(self):
      self.lower_bound = 0
      self.upper_bound = 100
      self.history = []
      self.attempts = 0


def run_games(num_games):
    total_games = 0
    total_wins = 0
    results_file = "results.md"

    if os.path.exists(results_file):
        mode = 'a'
    else:
        mode = 'w'

    with open(results_file, mode) as f:
        f.write(f"# GameResults (Data: {datetime.date.today()})\n\n")
        for i in range(num_games):
            number = random.randint(0, 100)
            ai = GuessingAI()
            success, guesses = guess_the_number(ai, number)
            total_games += 1
            if success:
                total_wins += 1
                ai.wins +=1  #Учет побед
            ai.reset() #обнуляем данные

            f.write(f"Game {i + 1}:\n")
            f.write(f"Gues num: {number}\n")
            f.write("-----------------------\n")
            for j, guess in enumerate(guesses):
                result_str = "=" if guess == number else ("<" if guess < number else ">")
                f.write(f"AI try {j + 1}: {guess}  system: {result_str}\n")
            f.write(f"Correct: {'Yes' if success else 'No'}\n\n")

        print(f"Всего игр: {total_games} из них побед: {total_wins}")


if __name__ == "__main__":
    num_games = 100
    run_games(num_games)