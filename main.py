from quests import cards
from random import randint
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_question(question):
    clear_screen()
    print("========================================")
    print(f"\t\tQuestion\n{'=' * 40}\n{question}\n{'=' * 40}")

def get_user_answer():
    return input("\nAnswer: ")

def display_correct_answer(answer):
    print(f"\nThe correct answer was: {answer}\n")

def get_user_feedback():
    return input("Were you correct? (Y/n/exit): ").lower()

def display_completion_message(num_cards):
    print(f"\nCongratulations! You have memorised all {num_cards} cards.")

def main():
    slots = (list(cards.items()), [], [])
    box_chance_mul = [4, 2, 1]
    
    try:
        while True:
            wts = [len(i) * box_chance_mul[idx] for idx, i in enumerate(slots)]
            total_weight = sum(wts)
            random_value = randint(1, total_weight) - 1
            
            box_idx = 0
            cumulative_weight = 0
            
            for idx, weight in enumerate(wts):
                cumulative_weight += weight
                if random_value < cumulative_weight:
                    box_idx = idx
                    n = random_value - cumulative_weight + weight
                    break
            
            question, answer = slots[box_idx].pop(n // box_chance_mul[box_idx])
            
            display_question(question)
            user_answer = get_user_answer()
            display_correct_answer(answer)
            
            feedback = get_user_feedback()
            
            if feedback.startswith("n"):
                box_idx = max(box_idx - 1, 0)
            elif feedback.startswith("y") or not feedback:
                box_idx = min(box_idx + 1, len(slots) - 1)
            else:
                break
            
            slots[box_idx].append((question, answer))
            
            if len(cards) == len(slots[-1]):
                display_completion_message(len(cards))
                exit_option = input("Exit? (N/y): ").lower()
                if exit_option.startswith("y"):
                    break

    except KeyboardInterrupt:
        print("\nExiting gracefully...")
        exit()

if __name__ == "__main__":
    main()