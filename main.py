from quests import cards
from random import randint
import os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def select_flashcard(slots, box_chance_mul):
    """Selects a flashcard randomly based on weighted probability."""
    wts = [len(i) * box_chance_mul[idx] for idx, i in enumerate(slots)]
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
    box = slots[box_idx]
    return box.pop(n // box_chance_mul[box_idx])

def display_flashcard(question):
    """Displays the flashcard question."""
    clear_screen()
    print(question)
    print("-" * len(question))

def main():
    slots = (list(cards.items()), [], [])
    box_chance_mul = [4, 2, 1]
    
    while True:
        q, a = select_flashcard(slots, box_chance_mul)
        display_flashcard(q)
        # Get user input for the answer
        input("Answer: ")
        # Show correct answer and prompt for correctness
        user_input = input(f"The answer was: {a}\nWere you correct? (Y/n/exit): ")
        if not user_input or user_input[0].lower() == "y":
            box_idx = min(box_idx + 1, len(slots) - 1)
        elif user_input[0].lower() == "n":
            box_idx = max(box_idx - 1, 0)
        else:
            break
        slots[box_idx].append((q, a))
        # Check if all cards have been memorized
        if len(cards) == len(slots[-1]):
            print(f"You have memorized all {len(cards)} cards")
            exit_input = input("Exit? (N/y): ")
            if exit_input and exit_input[0].lower() == "y":
                break

if __name__ == "__main__":
    main()
