from quests import cards
from random import randint

def main():
    slots = (list(cards.items()), [], [])
    box_chance_mul = [4, 2, 1]
    correct_count = 0
    total_questions = len(cards)
    
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
            print(q)
            print("-" * 4)
            user_answer = input("Answer: ")
            correct_answer = f"The answer was: {a}\nWere you correct? (Y/n/exit): "
            o = input(correct_answer)
            print("=" * 5)
            if not o or o[0].lower() == "y":
                box_idx = min(box_idx + 1, len(slots) - 1)
                correct_count += 1
            elif o[0].lower() == "n":
                box_idx = max(box_idx - 1, 0)
            else:
                break
            slots[box_idx].append((q, a))
            if len(cards) == len(slots[-1]):
                print(f"You have memorised all {total_questions} cards")
                accuracy = correct_count / total_questions if total_questions > 0 else 0
                print(f"Performance Metrics:\nCorrect Answers: {correct_count}/{total_questions}\nAccuracy: {accuracy:.2%}")
                k = input("Exit? (N/y): ")
                if k and k[0].lower() == "y":
                    break
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
