from quests import cards
from random import randint

def calculate_difficulty(cards, slots):
    difficulty_scores = {}
    for idx, slot in enumerate(slots):
        for card in slot:
            question, answer = card
            difficulty_scores[(question, answer)] = idx
    sorted_difficulty = sorted(difficulty_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_difficulty[:5]

def main():
    slots = (list(cards.items()), [], [])
    box_chance_mul = [4, 2, 1]

    while True:
        # Calculate weights for each box
        weights = [len(slot) * mul for slot, mul in zip(slots, box_chance_mul)]
        total_weight = sum(weights)

        # Choose a random number within the total weight
        random_num = randint(1, total_weight) - 1
        
        # Determine the box index
        box_idx = 0
        accum_weight = 0
        for idx, weight in enumerate(weights):
            accum_weight += weight
            if random_num < accum_weight:
                box_idx = idx
                break

        # Retrieve a card from the selected box
        box = slots[box_idx]
        idx_in_box = random_num // box_chance_mul[box_idx]
        question, answer = box.pop(idx_in_box)

        # Clear screen and present the question
        print(chr(27) + "[2J")
        print(question)
        print("-" * 4)

        # Get user input for the answer
        input("Answer: ")
        
        # Determine user response and update box index accordingly
        response = input(f"The answer was: {answer}\nWere you correct? (Y/n/exit): ")
        print("=" * 5)
        if not response or response[0].lower() == "y":
            box_idx = min(box_idx + 1, len(slots) - 1)
        elif response[0].lower() == "n":
            box_idx = max(box_idx - 1, 0)
        else:
            break
        
        # Move the card to the appropriate box
        slots[box_idx].append((question, answer))

        # Check if all cards have been memorized
        if len(cards) == len(slots[-1]):
            print(f"You have memorized all {len(cards)} cards")
            exit_choice = input("Exit? (N/y): ")
            if exit_choice and exit_choice[0].lower() == "y":
                break

    # Show top 5 hardest cards
    print("\nTop 5 Hardest Cards:")
    hardest_cards = calculate_difficulty(cards, slots)
    for idx, (card, difficulty) in enumerate(hardest_cards):
        print(f"{idx+1}. Question: {card[0]}, Answer: {card[1]}, Difficulty: {difficulty}")

if __name__ == "__main__":
    main()
