import random
import os
import pygame
import time
import json

class Initialise:
    def __init__(self, word_file, music_object):
        self.score = 5
        self.words = []
        self.available_words = []
        self.word_file = word_file
        self.music = music_object
        self.currentuser = "Guest"
        self.logged_in = False

    def user(self):
        os.system("cls")
        with open("users.txt", "r") as f:
            data = json.load(f)
        print("\n")
        while True:
            print(("Login").center(160))
            print(('\u2500'*36).center(160))
            print("\n")
            print(("Username: (or continue as a guest by typing 'guest'): ").center(160), end="")
            out_user = input("")
            print("\n")
            if (out_user.lower() == "guest"):
                print("\n")
                print(("Continuing as a guest...").center(160))
                time.sleep(3)
                os.system("cls")
                break
            for item in data:
                print(item)
                if item.get("username") == out_user:
                    os.system("cls")
                    print("\n")
                    print(("User data found. Login? (y/n): ").center(160), end="")
                    user_choice = input("")
                    if (user_choice.lower() == "y"):
                        self.currentuser = item.get("username")
                        self.score = item.get("score")
                        self.logged_in = True
                        break
                    elif (user_choice.lower() == "n"):
                        break
            if (self.logged_in):
                break
            else:
                os.system("cls")
                print("\n")
                print((f"Logged in as a new user: {out_user} ").center(160))
                print(('\u2500'*32).center(160))
                new_data = {"username": out_user, "score": 5}
                self.score = 5
                with open("users.txt", "w") as f:
                    json.dump(new_data, f, indent=4)
                print(('\u2500'*32).center(160))
                print("\n")
                print(("Loading...").center(160))
                time.sleep(3)
                break
                    

    def load_words(self):
        with open(self.word_file, "r", encoding="utf-8") as f:
            for line in f:
                spaces = " "
                if line.strip() == "":
                    continue
                word, difficulty, hint = [x.strip() for x in line.split("|", 2)]
                spaces = "_ "*len(word)
                self.words.append({"word": word, "spaces": spaces, "difficulty": difficulty, "hint": hint})

    def available(self):
        for i in range(len(self.words)):
            self.available_words.append(i)

    def clear_screen(self):
        os.system("cls")

    def ascii(self):
        print("\n")
        print(("██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗").center(160))
        print(("██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║").center(160)) 
        print(("███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║").center(160))
        print(("██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║").center(160))
        print(("██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║").center(160))
        print(("╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝").center(160))
        print("\n")
    
    def update_score(self):
        with open("users.txt", "r") as f:
            data = json.load(f)
        for item in data:
            if item.get("username") == self.currentuser:
                self.score = item.get("score")

    def play(self):
        self.music.home()
        self.clear_screen()
        self.load_words()
        self.available()
        self.ascii()
        print(("Press [ENTER] to enter as a guest: ").center(160))
        print(("Enter [1] to login as an existing user. ").center(160))
        breaker = input(("").center(160))
        if breaker == "1":
            self.user()
        self.music.pause()
        while self.available_words:
            hintUsed = False
            untried = [
            'a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z'
            ]       
            checked = []
            randomise = random.choice(self.available_words)
            self.available_words = [x for x in self.available_words if x != randomise]
            if self.words[randomise]["difficulty"] == "hard":
                tries = 9
            elif self.words[randomise]["difficulty"] == "medium":
                tries = 7
            else:
                tries = 6
            self.music.entry()
            while tries != 0:
                # no lines before os.system clear
                # guessing
                self.clear_screen()
                print(("Hangman project").center(160))
                print("")
                print((f"𝗦𝗰𝗼𝗿𝗲: {self.score}").center(160))
                won = False
                print("  " + '\u2500' * 154)
                print("\n")
                print("  Tries: ",end="")
                for _ in range(tries):
                    print("🞸 ",end="")
                print("\n")
                print(f"  Difficulty: {self.words[randomise]['difficulty'].title()}")
                print("\n")
                print(("Untried:").center(160))
                print((", ".join(untried)).center(160))
                print("\n\n")
                print((" Already tried: ").center(160))
                print((", ".join(checked)).center(160))
                print("\n\n")
                if hintUsed == True:
                    print((f"Hint: {self.words[randomise]['hint']}").center(160))
                    print("\n")
                print(("Guess!").center(160))
                print("\n")
                print((self.words[randomise]["spaces"]).center(160))
                print("\n")
                # letter input
                print(("Enter any letter or type 'hint' for hint: ").center(160))
                print("\n")
                print(" "*79,end="")
                letter = input("")
                letter = letter.lower()
                if letter != "hint" and len(letter) != 1:
                    print("\n")
                    print(("Invalid input (only one letter at a time!) [Press ENTER]").center(160))
                    print("\n")
                    print(" "*79,end="")
                    breaker = input((""))
                    continue
                # hint
                if letter == "hint":
                    self.music.warning()
                    if hintUsed == True:
                        breaker = input(("Already used hint! ").center(160))
                        continue
                    if self.score >= 3:
                        hintConfirm = input("\nAre you sure you want to use your hint? (-3 score, you only win 4 points (instead of 5 points) if you are correct) (Y/N): ")
                        if hintConfirm.lower() == "y":
                            self.music.hint()
                            self.score -= 3
                            if (self.logged_in):
                                self.update_score()
                            os.system("cls")
                            print((f"Score: {self.score}").center(160))
                            hintUsed = True
                            print((f"Hint: {self.words[randomise]['hint']}").center(160))
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
                    self.music.already()
                    print("\n")
                    print(("Already tried.").center(160))
                    print(" "*81,end="")
                    breaker=input(("").center(160))
                    print("\n")
                    continue
                # establishing that letter is now tried
                try:
                    untried.remove(letter)
                    checked.append(letter)
                except ValueError:
                    print("\n")
                    print(("Invalid input (only one letter at a time!) [Press ENTER]").center(160))
                    print("\n")
                    print(" "*79,end="")
                    breaker = input((""))
                    continue
                # check if letter in word
                if letter in self.words[randomise]["word"]:
                    self.music.correct()
                    for j in range(len(self.words[randomise]["word"])):
                        if self.words[randomise]["word"][j] == letter:
                            self.words[randomise]["spaces"] = self.words[randomise]["spaces"][:j*2] + letter + self.words[randomise]["spaces"][j*2+1:]
                        # no blank spaces (underscore) = letters guessed and word found
                        if "_" not in self.words[randomise]["spaces"]:
                            self.clear_screen()
                            print("\n\n")
                            if (len(self.words[randomise]["word"]) <= 9):
                                line_length = 24
                            else:
                                line_length = len(self.words[randomise]["word"]) * 2 + 4
                            print(('\u2500'*line_length).center(160))
                            print((self.words[randomise]["spaces"]).center(160))
                            print(("You found the word!").center(160))
                            self.music.win()
                            won = True
                            if hintUsed == True:
                                self.score += 4
                            else:
                                self.score += 5
                            print((f"Score: {self.score}").center(160))
                            print(('\u2500'*line_length).center(160))
                            if (self.logged_in):
                                self.update_score()
                            break
                else:
                    self.music.wrong()
                    tries -= 1
                # 3 more wrong tries for 5 points
                if self.score >= 5 and tries == 0:
                    self.clear_screen()
                    time.sleep(0.5)
                    self.music.warning()
                    option = input("You can buy 3 more wrong tries for 3 points. Try? (Y/N) ")
                    if option.lower() == "y":
                        tries += 3
                        self.score -= 3
                        if (self.logged_in):
                            self.update_score()
                if won == True:
                    break
            if won == False:
                if (len(self.words[randomise]["word"]) <= 9):
                    line_length = 24
                else:
                    line_length = len(self.words[randomise]["word"]) * 2 + 4
                self.clear_screen()
                print("\n\n")
                print(('\u2500'*32).center(160))
                self.music.lose()
                print(("You have lost. ").center(160))
                print((f"Word: {self.words[randomise]['word']}").center(160))
                print("\n")
                print((f"Guess: {self.words[randomise]['spaces']}").center(160))
                print("\n")
                print((f"Score: {self.score}").center(160))
                print(('\u2500'*line_length).center(160))
                print("\n\n")
            breaker = input("Continue [press enter]: ")



        
class Music:
    def __init__(self, home_music, entry_music, warning_music, hint_music, already_music, correct_music, wrong_music, win_music, lose_music):
        pygame.init() 
        self.home_music = home_music
        self.entry_music = entry_music
        self.warning_music = warning_music
        self.hint_music = hint_music
        self.already_music = already_music
        self.correct_music = correct_music
        self.wrong_music = wrong_music
        self.win_music = win_music
        self.lose_music = lose_music
    def home(self):
        pygame.mixer.music.load(self.home_music)
        pygame.mixer.music.play()
    def pause(self):
        pygame.mixer.music.pause()
    def entry(self):
        pygame.mixer.music.load(self.entry_music)
        pygame.mixer.music.play()
    def warning(self):
        pygame.mixer.music.load(self.warning_music)
        pygame.mixer.music.play()
    def hint(self):
        pygame.mixer.music.load(self.hint_music)
        pygame.mixer.music.play()
    def already(self):
        pygame.mixer.music.load(self.already_music)
        pygame.mixer.music.play()
    def correct(self):
        pygame.mixer.music.load(self.correct_music)
        pygame.mixer.music.play()
    def wrong(self):
        pygame.mixer.music.load(self.wrong_music)
        pygame.mixer.music.play()
    def win(self):
        pygame.mixer.music.load(self.win_music)
        pygame.mixer.music.play()
    def lose(self):
        pygame.mixer.music.load(self.lose_music)
        pygame.mixer.music.play()
        
if __name__ == "__main__":
    audio = Music("ROBLOX Music - Alice Deejay - Better Off Alone (Glejs Remix).mp3", "game-entrance.mp3", "warning.mp3", "hint-claim.mp3", 
                  "new-notification-026-380249.mp3", "mouse-click-405459.mp3", "wrong-47985.mp3", "level-win-6416.mp3", "lose-sfx-365579.mp3")
    game = Initialise("words.txt", audio)
    game.play()