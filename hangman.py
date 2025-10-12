import random
def hangman():
    words = [{"word": "apple", "spaces": "_ _ _ _ _", "difficulty": "easy"},{"word": "dream", "spaces": "_ _ _ _ _", "difficulty": "easy"}, {"word": "independence", "spaces": "_ _ _ _ _ _ _ _ _ _ _ _", "difficulty": "hard"}]
    score = 0
    # immediate below line must be altered for bigger project
    incomplete = [0, 1, 2]
    while True:
        randomise = random.choice(incomplete)
        incomplete = [x for x in incomplete if x != randomise]
        tries = 7
        print(words[randomise]["difficulty"].title())
        while tries != 0:
            won = False
            print(words[randomise]["spaces"])
            letter = input("Enter any letter: ")
            letter = letter.lower()
            if letter in words[randomise]["word"]:
                for j in range(len(words[randomise]["word"])):
                    if words[randomise]["word"][j] == letter:
                        words[randomise]["spaces"] = words[randomise]["spaces"][:j*2] + letter + words[randomise]["spaces"][j*2+1:]
                    if "_" not in words[randomise]["spaces"]:
                        print("\n\n------------------------")
                        print(words[randomise]["spaces"])
                        print("You found the word!")
                        won = True
                        score += 5
                        print(f"Score: {score}")
                        print("------------------------\n\n")
                        break
            else:
                print("Not found. ")
                tries -= 1
            if won == True:
                break

        if won == False:
            print("\n\n------------------------")
            print("You have lost. ")
            print(f"Word: {words[randomise]["word"]}\nGuess: {words[randomise]["spaces"]}\nScore: {score}")
            print("------------------------\n\n")







                

            
            
                




print(hangman())

