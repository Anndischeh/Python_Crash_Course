# Favorite Number
import json

number = input("What's your favorite number? ")

with open('favorite_number.json', 'w') as f:
    json.dump(number, f)
    print("Thanks! I'll remember that.")



with open('favorite_number.json') as f:
    number = json.load(f)

print(f"I know your favorite number! It's {number}.")