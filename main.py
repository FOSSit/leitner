# from quests import cards
# from random import randint

# def main():
#     slots = (list(cards.items()), [], [])
#     box_chance_mul = [4, 2, 1]
#     while True:
#         wts = [len(i) * box_chance_mul[idx] for idx, i in enumerate(slots)]
#         f = randint(1, sum(wts)) - 1
#         box_idx = 0
#         a = 0
#         n = 0
#         for idx, i in enumerate(wts):
#             a += i
#             if f < a:
#                 box_idx = idx
#                 n = f - a + i
#                 break
#         box = slots[box_idx]
#         q, a = box.pop(n // box_chance_mul[box_idx])
#         print(chr(27) + "[2J")
#         # print(box_idx, f, n)
#         print(q)
#         print("-" * 4)
#         input("Answer: ")
#         o = input(f"The answer was: {a}\nWere you correct? (Y/n/exit): ")
#         print("=" * 5)
#         if not o or o[0].lower() == "y":
#             box_idx = min(box_idx + 1, len(slots) - 1)
#         elif o[0].lower() == "n":
#             box_idx = max(box_idx - 1, 0)
#         else:
#             break
#         slots[box_idx].append((q, a))
#         if len(cards) == len(slots[-1]):
#             print(f"You have memorised all {len(cards)} cards")
#             k = input("Exit? (N/y): ")
#             if o and o[0].lower() == "y":
#                 break

# if __name__ == "__main__":
#     main()



from quests import cards
from quests import cards
from random import randint, choice

class FlashcardGame:
    def __init__(self):
        self.slots = [list(cards.items()), [], []]
        self.box_chance_mul = [4, 2, 1]

    def display_question(self, question):
        print(chr(27) + "[2J")  # Clear the screen
        print(question)
        print("-" * 4)

    def choose_random_question(self):
        weights = [len(slot) * multiplier for slot, multiplier in zip(self.slots, self.box_chance_mul)]
        total_weight = sum(weights)
        rand_index = randint(1, total_weight) - 1
        cumulative_weight = 0

        for idx, weight in enumerate(weights):
            cumulative_weight += weight
            if rand_index < cumulative_weight:
                box_idx = idx
                question_idx = rand_index - (cumulative_weight - weight)
                return box_idx, question_idx

    def play(self):
        while True:
            box_idx, question_idx = self.choose_random_question()
            box = self.slots[box_idx]

            if not box:  # Check if the box is empty
                print("No more questions left in this box.")
                break

            if question_idx >= len(box):  # Check if question_idx is out of range
                print("Invalid question index.")
                continue

            question, answer = box.pop(question_idx)

            self.display_question(question)

            user_answer = input("Answer: ")
            correct_answer = f"The answer was: {answer}\nWere you correct? (Y/n/exit): "
            user_input = input(correct_answer)

            if not user_input or user_input.lower() == "y":
                box_idx = min(box_idx + 1, len(self.slots) - 1)
            elif user_input.lower() == "n":
                box_idx = max(box_idx - 1, 0)
            else:
                break

            self.slots[box_idx].append((question, answer))

            if len(cards) == len(self.slots[-1]):
                print(f"You have memorized all {len(cards)} cards")
                exit_choice = input("Exit? (N/y): ")
                if exit_choice.lower() == "y":
                    break

if __name__ == "__main__":
    game = FlashcardGame()
    game.play()
