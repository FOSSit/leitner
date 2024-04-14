from quests import cards
from random import randint
import sys, os

class leitner:
    def __init__(self):
        self.result = 0
        self.slots = (list(cards.items()), [], [])
        self.box_chance_mul = [4, 2, 1]
    
    def leitner(self):
        while True:
            wts = [len(i) * self.box_chance_mul[idx] for idx, i in enumerate(self.slots)]
            
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
            
            box = self.slots[box_idx]
            
            q, a = box.pop(n // self.box_chance_mul[box_idx])
            
            if 'nt' in os.name:
                os.system('cls')
            else:
                os.system('clear')
            
            # print question
            print(q)
            print("-" * 4)
            
            # ask answer
            input("Answer: ")
            
            o = input(f"The answer was: {a}\nWere you correct? (Y/n/exit): ")
            
            if o=='y' or o=='Y':
                self.result += 1
            
            print("=" * 5)
            
            if not o or o[0].lower() == "y":
                box_idx = min(box_idx + 1, len(self.slots) - 1)
            elif o[0].lower() == "n":
                box_idx = max(box_idx - 1, 0)
            else:
                break
            
            self.slots[box_idx].append((q, a))
            
            if len(cards) == len(self.slots[-1]):
                print(f"You have memorised all {len(cards)} cards")
                k = input("Exit? (N/y): ")
                if o and o[0].lower() == "y":
                    break

if __name__ == "__main__":
    leitnerObj = leitner()
    try:
        leitnerObj.leitner()
    except KeyboardInterrupt:
        print(f'\nYou answered {leitnerObj.result} cards correctly.')
        sys.exit(0)