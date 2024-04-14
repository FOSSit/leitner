import sys
from quests import cards
from random import randint

def main():
    slots = (list(cards.items()), [], [])
    box_chance_mul = [4, 2, 1]
    while True:
        try:
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
            print(f"\nQuestion: {q}\n---")
            answer = input("Your answer: ")
            print(f"\nThe answer was: {a}\nCorrect? (Y/n)")
            if input().lower() == "y":
                box_idx = min(box_idx + 1, len(slots) - 1)
            elif input().lower() == "n":
                box_idx = max(box_idx - 1, 0)
            else:
                break
            slots[box_idx].append((q, a))
            if len(cards) == len(slots[-1]):
                print("You have memorised all the cards.")
                confirm = input("Exit? (N/y) ").lower()
                if confirm == "y":
                    break
        except KeyboardInterrupt:
            print("\nExiting gracefully...")
            sys.exit(0)
        if box_idx == 2:
            print("\nTop 5 hardest cards:")
            hardest_cards = sorted(slots[2], key=lambda x: x[0].count("?"), reverse=True)[:5]
            for q, a in hardest_cards:
                print(f"Question: {q}\nAnswer: {a}\n")

if __name__ == "__main__":
    main()