from quests import cards
from random import randint


def main():
    # Initialize slots for cards
    slots = (list(cards.items()), [], [])

    # Multiplier for box chance
    box_chance_mul = [4, 2, 1]

    while True:
        # Calculate weights for each box
        weights = [len(slot) * mul for slot, mul in zip(slots, box_chance_mul)]
        
        # Choose a random number
        random_num = randint(1, sum(weights)) - 1

        # Determine the box index and card index
        box_idx = 0
        accum = 0
        card_idx = 0
        for idx, weight in enumerate(weights):
            accum += weight
            if random_num < accum:
                box_idx = idx
                card_idx = random_num - accum + weight
                break
        
        # Select the box and the card
        selected_box = slots[box_idx]
        question, answer = selected_box.pop(card_idx // box_chance_mul[box_idx])

        # Clear the screen
        print(chr(27) + "[2J")

        # Print question
        print(question)
        print("-" * 4)

        # Get user's answer
        input("Answer: ")

        # Check if the user's answer is correct
        user_answer = input(f"The answer was: {answer}\nWere you correct? (Y/n/exit): ")
        print("=" * 5)

        # Determine the next box index based on user's response
        if not user_answer or user_answer[0].lower() == "y":
            box_idx = min(box_idx + 1, len(slots) - 1)
        elif user_answer[0].lower() == "n":
            box_idx = max(box_idx - 1, 0)
        else:
            break

        # Move the card to the appropriate box
        slots[box_idx].append((question, answer))

        # Check if all cards are memorized
        if len(cards) == len(slots[-1]):
            print(f"You have memorized all {len(cards)} cards")
            exit_choice = input("Exit? (N/y): ")
            if exit_choice and exit_choice[0].lower() == "y":
                break


if __name__ == "__main__":
    main()