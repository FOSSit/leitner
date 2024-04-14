from quests import cards
from random import randint

def clear_page():
    print("\n" * 50)  # Adjust the number of newlines as needed for your terminal size

def format_question(question):
    return f"Question: {question}"

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
        clear_page()
        print(format_question(q))
        print("-" * len(format_question(q)))
        user_answer = input("Answer: ")
        print("=" * 5)
        print(f"The answer was: {a}")
        o = input("Were you correct? (Y/n/exit): ")
        if not o or o[0].lower() == "y":
            box_idx = min(box_idx + 1, len(slots) - 1)
        elif o[0].lower() == "n":
            box_idx = max(box_idx - 1, 0)
        else:
            break
        slots[box_idx].append((q, a))
        if len(cards) == len(slots[-1]):
            print(f"You have memorised all {len(cards)} cards")
            exit_choice = input("Exit? (N/y): ")
            if exit_choice and exit_choice[0].lower() == "y":
                break

if __name__ == "__main__":
    main()
