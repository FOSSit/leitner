from quests import cards
from random import randint

def main():
    slots = (list(cards.items()), [], [])
    box_chance_mul = [4, 2, 1]
    hard = {}
    count = 0

    try:
        while True:
            count += 1
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
            if q in hard:
                hard[q] += 1
            else:
                hard[q] = 1
            
            print(chr(27) + "[2J")  # Clear the screen
            print("-" * 20)  # Separator
            print(f"Question {count}:")
            print(q)
            print("-" * 20)  # Separator
            input("Answer: ")
            o = input(f"The answer is : {a}\nWere you correct? (Y/n/exit): ")
            print("=" * 5)  # Separator
            if not o or o[0].lower() == "y":
                box_idx = min(box_idx + 1, len(slots) - 1)
            elif o[0].lower() == "n":
                box_idx = max(box_idx - 1, 0)
            else:
                break

        print("\nTop 5 Hardest Cards:")
        sorted_difficulty = sorted(hard.items(), key=lambda x: x[1], reverse=True)
        for i, (card, difficulty) in enumerate(sorted_difficulty[:5], 1):
            print(f"{i}. {card} - Difficulty: {difficulty}")

    except KeyboardInterrupt:
        print("\nExiting")

if _name_ == "_main_":
    main()
