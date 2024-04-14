from quests import cards
from random import randint

def main():
    slots = (list(cards.items()), [], [])
    box_chance_mul = [4, 2, 1]
    hard={}
    
    try:
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
            if q in hard:
                hard[q] += 1
            else:
                hard[q] = 1
            print(chr(27) + "[2J")
            # print(box_idx, f, n)
            print(q)
            print("-" * 4)
            input("Answer: ")
            o = input(f"The answer was: {a}\nWere you correct? (Y/n/exit): ")
            print("=" * 5)
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
