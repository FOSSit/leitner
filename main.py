from quests import cards
from random import randint

def main():
    slots = (list(cards.items()), [], [])
    box_chance_mul = [4, 2, 1]
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
            print(chr(27) + "[2J")
            # print(box_idx, f, n)
            print(q)
            print("-" * 4)
            user_input = input("Answer: ")
            if user_input.lower() == 'exit':
                break
            print(f"The answer was: {a}")
            if user_input.lower() == 'n':
                box_idx = max(box_idx - 1, 0)
            elif user_input.lower() != 'y':
                continue
            box_idx = min(box_idx + 1, len(slots) - 1)
            slots[box_idx].append((q, a))
            if len(cards) == len(slots[-1]):
                print(f"You have memorized all {len(cards)} cards")
                k = input("Exit? (N/y): ")
                if k.lower() == 'y':
                    break
    except KeyboardInterrupt:
        print("Exiting gracefully")

if __name__ == "__main__":
    main()