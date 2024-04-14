
from quests import cards
from random import randint
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    slots = (list(cards.items()), [], [])
    box_chance_mul = [4, 2, 1]
    while True:
        clear_screen()
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
        q, a = box.pop(n // box_chance_mul[box_idx])
        
        print(q)
        print("-" * 4)
        input("Answer: ")
        user_answer =input("Answer: ")
        clear_screen()
        print(f"The answer was: {a}")
        print("=" * 5)
        if user_answer.lower() == a.lower():
            print("Correct")
            box_idx = min(box_idx + 1, len(slots) - 1)
        else
            print("Incorrect!")
            box_idx = max(box_idx - 1, 0)
        imput("Press Enter to continue..")
        slots[box_idx].append((q, a))
        if len(cards) == len(slots[-1]):
            print(f"You have memorised all {len(cards)} cards")
            k = input("Exit? (N/y): ")
            if k.lower() == "y":
                break

if __name__ == "__main__":
    main()
