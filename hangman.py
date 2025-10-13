import random
import os
def hangman():
    # list of words
    words = [{"word": "apple", "spaces": "_ _ _ _ _", "difficulty": "easy","hint": "A fruit"},
    {"word": "dream", "spaces": "_ _ _ _ _", "difficulty": "easy","hint": "During sleep"}, 
    {"word": "independence", "spaces": "_ _ _ _ _ _ _ _ _ _ _ _", "difficulty": "hard"},
    {"word": "orange", "spaces": "_ _ _ _ _ _", "difficulty": "easy","hint": "A fruit"},
    {"word": "python", "spaces": "_ _ _ _ _ _", "difficulty": "easy", "hint": "A programming language"},
    {"word": "elephant", "spaces": "_ _ _ _ _ _ _ _", "difficulty": "medium", "hint": "An animal"},
    {"word": "architecture", "spaces": "_ _ _ _ _ _ _ _ _ _ _ _", "difficulty": "hard", "hint": "An art of science of designing"},
    {"word": "guitar", "spaces": "_ _ _ _ _ _", "difficulty": "medium","hint": "A musical instrument"},
    {"word": "democracy", "spaces": "_ _ _ _ _ _ _ _ _", "difficulty": "medium", "hint": "A form of government"},
    {"word": "banana", "spaces": "_ _ _ _ _ _", "difficulty": "easy", "hint": "A fruit"},
    {"word": "mountain", "spaces": "_ _ _ _ _ _ _ _", "difficulty": "medium", "hint": "A natural elevation"},
    {"word": "philosophy", "spaces": "_ _ _ _ _ _ _ _ _ _", "difficulty": "hard", "hint": "A field of study"},
    {"word": "ocean", "spaces": "_ _ _ _ _", "difficulty": "easy", "hint": "A body of water"},
    {"word": "pyramid", "spaces": "_ _ _ _ _ _ _", "difficulty": "medium", "hint": "Something famous in Egypt"},
    {"word": "jupiter", "spaces": "_ _ _ _ _ _ _", "difficulty": "medium", "hint": "Largest planet in our solar system"},
    {"word": "kangaroo", "spaces": "_ _ _ _ _ _ _ _", "difficulty": "medium", "hint": "Marsupial animal famous for hopping in Australia"},
    {"word": "avocado", "spaces": "_ _ _ _ _ _ _", "difficulty": "easy", "hint": "Green fruit often used in guacamole"},
    {"word": "volcano", "spaces": "_ _ _ _ _ _ _", "difficulty": "medium", "hint": "Mountain that erupts molten lava"},
    {"word": "himalayas", "spaces": "_ _ _ _ _ _ _ _ _", "difficulty": "hard", "hint": "Mountain range home to Mount Everest"},
    {"word": "pneumonia", "spaces": "_ _ _ _ _ _ _ _ _", "difficulty": "hard", "hint": "A serious lung infection"},
    {"word": "chocolate", "spaces": "_ _ _ _ _ _ _ _ _", "difficulty": "easy", "hint": "Sweet treat made from cocoa"},
    {"word": "sphinx", "spaces": "_ _ _ _ _ _", "difficulty": "hard", "hint": "Ancient Egyptian statue with a lion's body and human head"},
    {"word": "microsoft", "spaces": "_ _ _ _ _ _ _ _ _", "difficulty": "easy", "hint": "American software company"},
    {"word": "rainbow", "spaces": "_ _ _ _ _ _ _", "difficulty": "easy", "hint": "Colours that appear in the sky after rain"},
    {"word": "astronomy", "spaces": "_ _ _ _ _ _ _ _ _", "difficulty": "medium", "hint": "The scientific study of celestial objects"},
    {"word": "telescope", "spaces": "_ _ _ _ _ _ _ _ _", "difficulty": "medium", "hint": "Instrument used to view distant stars and planets"},
    {"word": "butterfly", "spaces": "_ _ _ _ _ _ _ _ _", "difficulty": "easy", "hint": "Insect with colourful wings that flies"},
    {"word": "avalanche", "spaces": "_ _ _ _ _ _ _ _ _", "difficulty": "hard", "hint": "Mass of snow sliding rapidly down a mountain"},
    {"word": "trolley", "spaces": "_ _ _ _ _ _ _", "difficulty": "medium", "hint": "Something found in a supermarket"},
    {"word": "marathon", "spaces": "_ _ _ _ _ _ _ _", "difficulty": "medium", "hint": "A long-distance running race"}
    ]
    score = 5
    available_words = []
    # immediate below line must be altered for bigger project
    for i in range(len(words)):
        available_words.append(i)
    while available_words:
        hintUsed = False
        untried = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z'
        ]       
        checked = []
        randomise = random.choice(available_words)
        available_words = [x for x in available_words if x != randomise]
        if words[randomise]["difficulty"] == "hard":
            tries = 9
        elif words[randomise]["difficulty"] == "medium":
            tries = 7
        else:
            tries = 6
        while tries != 0:
            # no lines before os.system clear
            # guessing
            os.system("cls")
            print("="*180)
            print(("Hangman Project\n").center(164))
            print((f"Score: {score}").center(164))
            won = False
            print("="*180)
            print("\n")
            print("Tries: ",end="")
            for _ in range(tries):
                print("🞸 ",end="")
            print("\n")
            print(f"Difficulty: {words[randomise]["difficulty"].title()}")
            print("\n")
            print(("Untried:").center(164))
            print((", ".join(untried)).center(164))
            print("\n\n")
            print(("Already tried: ").center(164))
            print((", ".join(checked)).center(164))
            print("\n\n")
            if hintUsed == True:
                print((f"Hint: {words[randomise]["hint"]}").center(164))
                print("\n")
            print(("Guess!").center(164))
            print("\n")
            print((words[randomise]["spaces"]).center(164))
            print("\n")
            # letter input
            print(("Enter any letter or type 'hint' for hint: ").center(164))
            print("\n")
            print(" "*81,end="")
            letter = input("")
            if letter != "hint" and len(letter) != 1:
                print(("Invalid input [Press ENTER]").center(164))
                print("\n")
                print(" "*81,end="")
                breaker = input((""))
                continue
            letter = letter.lower()
            # hint
            if letter == "hint":
                if hintUsed == True:
                    breaker = input(("Already used hint! ").center(164))
                    continue
                if score >= 2:
                    hintConfirm = input("\nAre you sure you want to use your hint? (-3 score, you only win 4 points (instead of 5 points) if you are correct) (Y/N): ")
                    if hintConfirm.lower() == "y":
                        score -= 3
                        os.system("cls")
                        print((f"Score: {score}").center(164))
                        hintUsed = True
                        print((f"Hint: {words[randomise]["hint"]}").center(164))
                        print("Continue: [enter]".center(164))
                        print(" "*81,end="")
                        breaker = input((""))
                        continue
                    else:
                        continue
                else:
                    breaker = input("You do not have enough score to use a hint. [ENTER]")
                    continue
            # already tried letters
            if letter in checked:
                print("\n")
                print(("Already tried.").center(164))
                print(" "*81,end="")
                breaker=input(("").center(164))
                print("\n")
                continue
            # establishing that letter is now tried
            untried.remove(letter)
            checked.append(letter)
            # check if letter in word
            if letter in words[randomise]["word"]:
                for j in range(len(words[randomise]["word"])):
                    if words[randomise]["word"][j] == letter:
                        words[randomise]["spaces"] = words[randomise]["spaces"][:j*2] + letter + words[randomise]["spaces"][j*2+1:]
                    # no blank spaces (underscore) = letters guessed and word found
                    if "_" not in words[randomise]["spaces"]:
                        os.system("cls")
                        print("\n\n")
                        print(("------------------------").center(164))
                        print((words[randomise]["spaces"]).center(164))
                        print(("You found the word!").center(164))
                        won = True
                        if hintUsed == True:
                            score += 4
                        else:
                            score += 5
                        print((f"Score: {score}").center(164))
                        print(("------------------------").center(164))
                        break
            else:
                tries -= 1
            # 3 more wrong tries for 5 points
            if score >= 5 and tries == 0:
                os.system("cls")
                option = input("You can buy 3 more wrong tries for 5 points. Try? (Y/N) ")
                if option.lower() == "y":
                    tries += 3
                    score -= 5
            if won == True:
                break
        # lost
        if won == False:
            os.system("cls")
            print("\n\n")
            print(("--------------------------------").center(164))
            print(("You have lost. ").center(164))
            print((f"Word: {words[randomise]["word"]}").center(164))
            print("\n")
            print((f"Guess: {words[randomise]["spaces"]}").center(164))
            print("\n")
            print((f"Score: {score}").center(164))
            print(("--------------------------------").center(164))
            print("\n\n")
        breaker = input("Continue [press enter]: ")
# function run
print(hangman())


