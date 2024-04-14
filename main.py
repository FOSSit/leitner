from quests import cards
from random import randint

def main():
    slots = (list(cards.items()), [], [])
    card_stats = {}  # Dictionary to track card statistics: {card: [total_attempts, incorrect_attempts]}
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
        print(box_idx)
        incorrect = 0
        print(q)
        print("-" * 4)
        
        user_answer = input("Answer: ")
        print(f"The answer was: {a}")
        
        if user_answer.lower() == a.lower():
            print("Correct!")
            box_idx = min(box_idx + 1, len(slots) - 1)
        else:
            print("Incorrect!")
            box_idx = max(box_idx - 1, 0)
            incorrect += 1
        
        # Update card statistics
        card_stats.setdefault(q, [0, 0])
        card_stats[q][0] += 1
        card_stats[q][1] += incorrect
        
        slots[box_idx].append((q, a))
        
        if len(cards) == len(slots[-1]):
            print(f"You have memorised all {len(cards)} cards")
            break
    
    # Calculate percentage of incorrect answers for each card
    card_percentages = {card: (stats[1] / stats[0]) * 100 for card, stats in card_stats.items()}
    
    # Sort cards by percentage of incorrect answers and pick top 5
    top_wrong_cards = sorted(card_percentages.items(), key=lambda x: x[1], reverse=True)[:5]
    
    # Display top wrong cards
    print("Top 5 cards with highest percentage of wrong answers:")
    for card, percentage in top_wrong_cards:
        print(f"Card: {card} - Incorrect percentage: {percentage:.2f}%")

if __name__ == "__main__":
    main()