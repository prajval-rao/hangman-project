import random
import os
import pygame
import time
pygame.init() 
def hangman():
    # list of words
    words = []
    with open("words.txt", "r", encoding="utf-8") as f:
        for line in f:
            spaces = " "
            if not line.strip():
                continue
            word, difficulty, hint = [x.strip() for x in line.split("|", 2)]
            spaces = "_ "*len(word)
            words.append({"word": word, "spaces": spaces, "difficulty": difficulty, "hint": hint})
    score = 5
    available_words = []
    # immediate below line must be altered for bigger project
    for i in range(len(words)):
        available_words.append(i)
    pygame.mixer.music.load(r"C:\Users\theof\OneDrive\Documents\Python Projects & Files\Hangman\ROBLOX Music - Alice Deejay - Better Off Alone (Glejs Remix).mp3")
    pygame.mixer.music.play()
    os.system("cls")
    print("\n")

    print(("██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗").center(160))
    print(("██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║").center(160)) 
    print(("███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║").center(160))
    print(("██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║").center(160))
    print(("██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║").center(160))
    print(("╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝").center(160))

    print("\n")
    print(("Press [ENTER] to continue: ").center(160))
    breaker = input(("").center(160))
    pygame.mixer.music.pause()

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
        pygame.mixer.music.load(r"C:\Users\theof\OneDrive\Documents\Python Projects & Files\Hangman\game-entrance.mp3")
        pygame.mixer.music.play()
        while tries != 0:
            # no lines before os.system clear
            # guessing
            os.system("cls")
            print(("Hangman project").center(160))
            print("")
            print((f"𝗦𝗰𝗼𝗿𝗲: {score}").center(160))
            won = False
            print("  " + '\u2500' * 154)
            print("\n")
            print("  Tries: ",end="")
            for _ in range(tries):
                print("🞸 ",end="")
            print("\n")
            print(f"  Difficulty: {words[randomise]["difficulty"].title()}")
            print("\n")
            print(("Untried:").center(160))
            print((", ".join(untried)).center(160))
            print("\n\n")
            print((" Already tried: ").center(160))
            print((", ".join(checked)).center(160))
            print("\n\n")
            if hintUsed == True:
                print((f"Hint: {words[randomise]["hint"]}").center(160))
                print("\n")
            print(("Guess!").center(160))
            print("\n")
            print((words[randomise]["spaces"]).center(160))
            print("\n")
            # letter input
            print(("Enter any letter or type 'hint' for hint: ").center(160))
            print("\n")
            print(" "*79,end="")
            letter = input("")
            if letter != "hint" and len(letter) != 1:
                print("\n")
                print(("Invalid input (only one letter at a time!) [Press ENTER]").center(160))
                print("\n")
                print(" "*79,end="")
                breaker = input((""))
                continue
            letter = letter.lower()
            # hint
            if letter == "hint":
                pygame.mixer.music.load(r"C:\Users\theof\OneDrive\Documents\Python Projects & Files\Hangman\warning.mp3")
                pygame.mixer.music.play()
                if hintUsed == True:
                    breaker = input(("Already used hint! ").center(160))
                    continue
                if score >= 2:
                    hintConfirm = input("\nAre you sure you want to use your hint? (-3 score, you only win 4 points (instead of 5 points) if you are correct) (Y/N): ")
                    if hintConfirm.lower() == "y":
                        pygame.mixer.music.load(r"C:\Users\theof\OneDrive\Documents\Python Projects & Files\Hangman\hint-claim.mp3")
                        pygame.mixer.music.play()
                        score -= 3
                        os.system("cls")
                        print((f"Score: {score}").center(160))
                        hintUsed = True
                        print((f"Hint: {words[randomise]["hint"]}").center(160))
                        print("Continue: [enter]".center(160))
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
                pygame.mixer.music.load(r"C:\Users\theof\OneDrive\Documents\Python Projects & Files\Hangman\new-notification-026-380249.mp3")
                pygame.mixer.music.play()
                print("\n")
                print(("Already tried.").center(160))
                print(" "*81,end="")
                breaker=input(("").center(160))
                print("\n")
                continue
            # establishing that letter is now tried
            untried.remove(letter)
            checked.append(letter)
            # check if letter in word
            if letter in words[randomise]["word"]:
                pygame.mixer.music.load(r"C:\Users\theof\OneDrive\Documents\Python Projects & Files\Hangman\mouse-click-405459.mp3")
                pygame.mixer.music.play()
                for j in range(len(words[randomise]["word"])):
                    if words[randomise]["word"][j] == letter:
                        words[randomise]["spaces"] = words[randomise]["spaces"][:j*2] + letter + words[randomise]["spaces"][j*2+1:]
                    # no blank spaces (underscore) = letters guessed and word found
                    if "_" not in words[randomise]["spaces"]:
                        os.system("cls")
                        print("\n\n")
                        print(('\u2500'*24).center(160))
                        print((words[randomise]["spaces"]).center(160))
                        print(("You found the word!").center(160))
                        pygame.mixer.music.load(r"C:\Users\theof\OneDrive\Documents\Python Projects & Files\Hangman\level-win-6416.mp3")
                        pygame.mixer.music.play()
                        won = True
                        if hintUsed == True:
                            score += 4
                        else:
                            score += 5
                        print((f"Score: {score}").center(160))
                        print(('\u2500'*24).center(160))
                        break
            else:
                pygame.mixer.music.load(r"C:\Users\theof\OneDrive\Documents\Python Projects & Files\Hangman\wrong-47985.mp3")
                pygame.mixer.music.play()
                tries -= 1
            # 3 more wrong tries for 5 points
            if score >= 5 and tries == 0:
                os.system("cls")
                time.sleep(0.5)
                pygame.mixer.music.load(r"C:\Users\theof\OneDrive\Documents\Python Projects & Files\Hangman\warning.mp3")
                pygame.mixer.music.play()
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
            print(('\u2500'*32).center(160))
            pygame.mixer.music.load(r"C:\Users\theof\OneDrive\Documents\Python Projects & Files\Hangman\lose-sfx-365579.mp3")
            pygame.mixer.music.play()
            print(("You have lost. ").center(160))
            print((f"Word: {words[randomise]["word"]}").center(160))
            print("\n")
            print((f"Guess: {words[randomise]["spaces"]}").center(160))
            print("\n")
            print((f"Score: {score}").center(160))
            print(('\u2500'*32).center(160))
            print("\n\n")
        breaker = input("Continue [press enter]: ")
# function run
print(hangman())

