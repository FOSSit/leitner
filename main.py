from quests import cards
from random import randint

def main():
    slots = (list(cards.items()), [], [])
    box_chance_mul = [4, 2, 1]
    while True:
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
        print(chr(27) + "[2J")

        print("====================================")
        print("              Flashcard              ")
        print("====================================")
        print(f"Question: {q}")
        print("-" * 4)
        input("Answer: ")
        print(f"The answer was: {a}")
        print("=" * 5)

        if not input("Were you correct? (Y/n/exit): ").strip()[:1].lower() in ["n", ""]:
            box_idx = min(box_idx + 1, len(slots) - 1)
        else:
            box_idx = max(box_idx - 1, 0)

        slots[box_idx].append((q, a))
        
        if len(cards) == len(slots[-1]):
            print(f"You have memorised all {len(cards)} cards")
            if input("Exit? (N/y): ").strip()[:1].lower() == "y":
                break

if __name__ == "__main__":
    main()
