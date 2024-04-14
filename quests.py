from operator import itemgetter

# Sort the cards by the length of the answer
sorted_cards = sorted(cards.items(), key=lambda x: len(x[1]), reverse=True)

# Display the top 5 hardest cards
print("Top 5 Hardest Cards:")
for i, (question, answer) in enumerate(sorted_cards[:5], 1):
    print(f"{i}. {question}")
    print("   Answer:", answer)
    print("-" * 4)
