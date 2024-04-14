from quests import cards
from random import randint
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    slots = (list(cards.items()), [], [])
    box_chance_mul = [4, 2, 1]
    
    while True:
        # Calculate weights for each box
        wts = [len(i) * box_chance_mul[idx] for idx, i in enumerate(slots)]
        f = randint(1, sum(wts)) - 1
        box_idx = 0
        a = 0
        n = 0
        
        # Determine the box index and position within the box
        for idx, i in enumerate(wts):
            a += i
            if f < a:
                box_idx = idx
                n = f - a + i
                break
        
        box = slots[box_idx]
        q, a = box.pop(n // box_chance_mul[box_idx])  # Pop the question and answer from the box
        clear_screen()
        print(q)  # Display the question
        print("-" * 4)
        input("Press Enter to reveal the answer: ")
        clear_screen()
        print(f"Question: {q}\nAnswer: {a}")  # Display the question and answer
        print("=" * 5)
        
        # Prompt user for correctness and adjust box accordingly
        while True:
            o = input("Were you correct? (Y/n/exit): ").lower()
            if not o or o == "y":
                box_idx = min(box_idx + 1, len(slots) - 1)
                break
            elif o == "n":
                box_idx = max(box_idx - 1, 0)
                break
            elif o == "exit":
                return
        
        slots[box_idx].append((q, a))  # Add the question and answer back to the box

        # Check if all cards have been memorized
        if len(cards) == len(slots[-1]):
            print(f"You have memorized all {len(cards)} cards.")
            k = input("Exit? (y/N): ").lower()
            if k == "y":
                break

if __name__ == "__main__":
    main()
