from quests import cards
from random import randint

class CardGame:
    def __init__(self):
        self.slots = (list(cards.items()), [], [])
        self.box_chance_mul = [4, 2, 1]

    def play(self):
        try:
            while True:
                question, answer = self.choose_question()
                self.display_question(question)
                user_answer = input("Answer: ")
                correct_answer = f"The answer was: {answer}"
                self.display_result(correct_answer)
                if not self.continue_playing():
                    break
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            self.calculate_performance()

    def choose_question(self):
        wts = [len(i) * self.box_chance_mul[idx] for idx, i in enumerate(self.slots)]
        f = randint(1, sum(wts)) - 1
        box_idx = 0
        a = 0
        n = 0
        for idx, i in enumerate(wts):
            a += i
            if f < a:
                box_idx = idx
                n = f - a + i
                break
        box = self.slots[box_idx]
        return box.pop(n // self.box_chance_mul[box_idx])

    def display_question(self, question):
        print(chr(27) + "[2J")
        print(question)
        print("-" * 4)

    def display_result(self, correct_answer):
        print(correct_answer)
        print("=" * 5)

    def continue_playing(self):
        o = input("Were you correct? (Y/n/exit): ")
        if not o or o[0].lower() == "y":
            self.box_idx = min(self.box_idx + 1, len(self.slots) - 1)
        elif o[0].lower() == "n":
            self.box_idx = max(self.box_idx - 1, 0)
        else:
            return False
        self.slots[self.box_idx].append((self.question, self.answer))
        if len(cards) == len(self.slots[-1]):
            print(f"You have memorised all {len(cards)} cards")
            exit_option = input("Exit? (N/y): ")
            return exit_option and exit_option[0].lower() != "y"
        return True

    def calculate_performance(self):
        total_cards = sum(len(slot) for slot in self.slots)
        total_correct = len(self.slots[-1])
        accuracy = (total_correct / total_cards) * 100
        print("\n\nPerformance Metrics:")
        print(f"Total Cards: {total_cards}")
        print(f"Total Correct: {total_correct}")
        print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    game = CardGame()
    game.play()
