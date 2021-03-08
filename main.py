import random
import string

words = ["python", "java", "kotlin", "javascript"]
english_symbol_check = string.ascii_lowercase
print("H A N G M A N")
while True:
    chose = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if chose == "play":
        count = 0
        random_word = random.choice(words)
        secret_word = "-" * len(random_word)
        symbol_list = []
        while True:
            print()
            print(secret_word)
            symbol = input("Input a letter: ")
            # Check is int
            try:
                error = int(symbol)
                if len(symbol) != 1:
                    print("You should input a single letter")
                else:
                    print("Please enter a lowercase English letter")
                continue
            except ValueError:
                # Input > 1?
                if len(symbol) != 1:
                    print("You should input a single letter")
                    continue
            # If symbol not english lower case
            if symbol not in english_symbol_check:
                print("Please enter a lowercase English letter")
                continue
            # No improvements, That letter doesn't appear in the word or Nothing
            if symbol in random_word and symbol not in secret_word:
                symbol_list.append(symbol)
                for i in range(len(random_word)):
                    if random_word[i] == symbol:
                        secret_word = secret_word[:i] + symbol + secret_word[i + 1:]
            elif symbol in symbol_list:
                print("You've already guessed this letter")
                continue
            else:
                symbol_list.append(symbol)
                print("That letter doesn't appear in the word")
                count += 1
            # Win or lost
            if "-" not in secret_word:
                print(f"You guessed the word {random_word}!")
                print("You survived!")
                break
            elif count >= 8:
                print("You lost!")
                break
    elif chose == "exit":
        break
