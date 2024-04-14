from quests import cards
from random import randint

def main():
    slots = (list(cards.items()), [], [])
    box_chance_mul = [4, 2, 1]
    total_questions = 0
    correct_answers = 0
    completionness = 0
    card_stats = {card: [0, 0] for card in cards}  
    try:
        while True:
            total_questions += 1
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
            card_stats[q][0] += 1
            print(chr(27) + "[2J")
            print(q)
            print("-" * 4)
            input("Answer: ")
            o = input(f"The answer was: {a}\nWere you correct? (Y/n/exit): ")
            print("=" * 5)
            if not o or o[0].lower() == "y":
                correct_answers += 1
                box_idx = min(box_idx + 1, len(slots) - 1)
            elif o[0].lower() == "n":
                card_stats[q][1] += 1
                box_idx = max(box_idx - 1, 0)
            else:
                break
            slots[box_idx].append((q, a))
            if len(cards) == len(slots[-1]):
                print(f"You have memorised all {len(cards)} cards")
                completionness = 1
                k = input("Exit? (N/y): ")
                if o and o[0].lower() == "y":
                    break
    except KeyboardInterrupt:
        if total_questions > 0:
            performance = (correct_answers / total_questions) * 100

            #issue 1
            print(f"\nPerformance: {performance:.2f}% ({correct_answers}/{total_questions})")
            if(completionness):
                print("You have memorised all the cards!")
            else:
                print(f"You have {len(cards) - len(slots[-1])} cards left to memorise.")
            
            #issue 2
            incorrect_percentages = {card: (stats[1] / stats[0]) * 100 for card, stats in card_stats.items() if stats[0] > 0}
            sorted_cards = sorted(incorrect_percentages.items(), key=lambda x: x[1], reverse=True)
            # print top 5 cards with highest incorrect percentage
            for card, percentage in sorted_cards[:5]:
                print(f"Card: {card}, Incorrect Answers: {percentage:.2f}%")
        else:
            print("\nNo questions were asked.")
        exit()

if __name__ == "__main__":
    main()