from quests import cards
from random import randint

def main():
    # Initialize the slots with cards
    slots = (list(cards.items()), [], [])
    # Multiplier for box chances
    box_chance_mul = [4, 2, 1]

    while True:
        # Calculate weights for each slot
        weights = [len(slot) * box_chance_mul[idx] for idx, slot in enumerate(slots)]
        # Randomly select a box based on weights
        random_value = randint(1, sum(weights)) - 1
        selected_box_idx = 0
        accumulated_weight = 0

        # Find the selected box index
        for idx, weight in enumerate(weights):
            accumulated_weight += weight
            if random_value < accumulated_weight:
                selected_box_idx = idx
                # Calculate the index within the selected box
                index_within_box = random_value - accumulated_weight + weight
                break

        # Get the selected box
        selected_box = slots[selected_box_idx]
        # Pop a card from the selected box based on the index
        question, answer = selected_box.pop(index_within_box // box_chance_mul[selected_box_idx])

        # Clear the console
        print(chr(27) + "[2J")
        # Display the question
        print(question)
        print("-" * 4)
        # Prompt user for answer
        input("Answer: ")
        # Ask user if the answer was correct
        user_input = input(f"The answer was: {answer}\nWere you correct? (Y/n/exit): ")
        print("=" * 5)

        if not user_input or user_input[0].lower() == "y":
            # Move to the next box if the answer was correct or no input provided
            selected_box_idx = min(selected_box_idx + 1, len(slots) - 1)
        elif user_input[0].lower() == "n":
            # Move to the previous box if the answer was incorrect
            selected_box_idx = max(selected_box_idx - 1, 0)
        else:
            # Exit the program if the user enters 'exit'
            break
        
        # Add the card back to the appropriate box
        slots[selected_box_idx].append((question, answer))

        # Check if all cards have been memorized
        if len(cards) == len(slots[-1]):
            print(f"You have memorized all {len(cards)} cards")
            user_input = input("Exit? (N/y): ")
            if user_input and user_input[0].lower() == "y":
                break

if __name__ == "__main__":
    main()
