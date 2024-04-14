from quests import cards
from random import randint

def main():
    slots = (list(cards.items()), [], [])
    box_chance_multiplier = [4, 2, 1]
    while True:
        weights = [len(i) * box_chance_multiplier[index] for index, i in enumerate(slots)]
        f = randint(1, sum(weights)) - 1
        box_index = 0
        answer = 0
        n = 0 # calculates the position of the card within that slot
        for index, i in enumerate(weights):
            answer += i
            if f < answer:
                box_index = index
                n = f - answer + i
                break
        box = slots[box_index]
        question, answer = box.pop(n // box_chance_multiplier[box_index])
        print(chr(27) + "[2J]")
        # print(box_index, f, n)
        print(question)
        print("~" * 10)
        input("The answer is : ")
        option = input(f" The answer was : {answer}\n Was the answer correct? (Y/N) : ")
        print("~" * 10)
        if not option or option[0].lower() == "Y":
            box_index = min(box_index + 1, len(slots) - 1)
        elif option[0].lower() == "N":
            box_index = max(box_index - 1, 0)
        else:
            break
        slots[box_index].append((question, answer))
        if len(cards) == len(slots[-1]):
            print(f" You have memorised all {len(cards)} cards")
            k = input("Do you want to exit? (Y/N) : ")
            if option and option[0].lower() == "Y":
                break

if __name__ == "__main__":
    main()