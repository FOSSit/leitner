from quests import cards  # Assuming cards is a dictionary or list of flashcards
from random import randint
import signal

def print_card(question, answer):
    """Prints a card with a border and centered text."""
    border_length = max(len(question), len(answer)) + 4
    print("+" + "-" * border_length + "+")
    print("|" + question.center(border_length - 2) + "|")
    print("+" + "-" * border_length + "+")
    print("|" + answer.center(border_length - 2) + "|")
    print("+" + "-" * border_length + "+")

def clear_screen():
    """Clears the screen."""
    print(chr(27) + "[2J")  # Clear screen

def display_question(question, answer):
    """Displays the question and answer using the print_card function."""
    clear_screen()
    print_card(question, answer)

def choose_random_question(slots, box_chance_mul):
    """Chooses a random question from the specified slot."""
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
    return box.pop(n // box_chance_mul[box_idx])

def get_user_answer(question):
    """Prompts the user for an answer to the given question."""
    print("-" * 4)
    answer = input(f"{question}: ")
    return answer

def check_answer(correct_answer, user_answer):
    """Checks if the user's answer matches the correct answer."""
    return correct_answer.lower() == user_answer.lower()

def update_slot(slots, box_idx, question, answer):
    """Updates the specified slot with the question and answer."""
    slots[box_idx].append((question, answer))

def calculate_performance(correct, total_questions):
    """Calculates the user's performance metrics."""
    if total_questions == 0:
        return 0.0  # Avoid division by zero
    return correct / total_questions * 100

def display_performance(correct, total_questions):
    """Displays the user's performance in a formatted manner."""
    performance = calculate_performance(correct, total_questions)
    print(f"\nYour performance: {performance:.2f}%")
    print(f"Correct answers: {correct}")
    print(f"Total questions: {total_questions}")

def handle_ctrl_c(signum, frame):
    slots = (list(cards.items()), [], [])
    """Handles Ctrl+C by displaying performance and exiting."""
    print("\nInterrupt received (Ctrl+C).")
    correct = len([q for q, a in slots[-1]])  # Count correct answers in last slot
    display_performance(correct, len(cards))
    exit(0)  # Exit gracefully

def main():
    slots = (list(cards.items()), [], [])
    box_chance_mul = [4, 2, 1]
    correct = 0  # Track correct answers

    # Register Ctrl+C handler (pass slots as argument to the function)
    signal.signal(signal.SIGINT, handle_ctrl_c)

    while True:
        box_idx = 0
        question, answer = choose_random_question(slots, box_chance_mul)
        display_question(question, answer)

        user_answer = get_user_answer("Answer")
        correct += check_answer(answer, user_answer)

        print("=" * 5)
        if correct:
            print("Correct!")
            box_idx = min(box_idx + 1, len(slots) - 1)
        else:
            print("Incorrect.")
            box_idx = max(box_idx - 1, 0)

        update_slot(slots, box_idx, question, answer)

        if len(cards) == len(slots[-1]):
            print(f"You have memorised all {len(cards)} cards!")
            display_performance(correct, len(cards))
            break

if __name__ == "_main_":
    main()