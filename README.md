# Hangman Project

A simple command-line classic Hangman game, built entirely in Python and played in the terminal, using the basic principles of object-oriented programming. It is a word-guessing game, where each word has a difficulty level and a hint. Depending on the difficulty level, there are a number of "tries", or wrong guesses, and the user must guess all the letters of the word without running out of tries. If the user runs out of tries, they can purchase them if they can afford it, based on the currency of the game. This currency is the "score", which increases if the user guesses the word. You can also purchase a hint for each word using this score.

## Table of contents

* [Requirements](#Requirements)
* [Features](#Features)
* [Project Structure](#Project-Structure)
* [Game](#Game)
* [Future improvements](#Future-improvements)

## Requirements

Language: Python 3

External libraries:
* pygame: For sound effects and music

Standard libraries:
* random: To randomise the words
* os: To display all relevant content on the screen at a time
* time: For buffer

Files:
* hangman.py: Main program file
* words.txt: A list of words with difficulties [See here](https://github.com/prajval-rao/hangman-project/blob/main/words.txt)
* Music files: Files for each method of the class Music() as shown [here](https://github.com/prajval-rao/hangman-project/blob/main/hangman.py)

## Features

These are the primary features of the game:
- Word-guessing gameplay similar to Hangman
- Words, difficulty levels, and hints loaded from an external file
- Object-oriented design with separate classes for game logic and audio handling
- Scoring system with rewards
- Hint system with score deduction
- Difficulty-based number of attempts
- Sound effects for game events
- Input validation and handling of repeated guesses
- Ability to buy more attempts by using score points

## Project Structure

📁 Hangman

- [hangman.py](https://github.com/prajval-rao/hangman-project/blob/main/hangman.py) – main program
- [words.txt](https://github.com/prajval-rao/hangman-project/blob/main/words.txt) – word list
- mp3 files – for Music() class methods
- [Hangman.bat](https://github.com/prajval-rao/hangman-project/blob/main/Hangman.bat) – optional startup of program

## Game

Home screen:

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/9f1d9261-a527-4639-9379-979f5a4231de" />


Game screen:

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/4c2dfb34-5d01-40bc-adcb-e83af16d5285" />

## Future improvements

* Adding the option to login under a specific username, along with which the user's score is stored
* Maintaining score changes (storing history of scores of every user in an Excel file and accessing, creating and deleting the entries through the program) and having a ranking system based on score, along with Matplotlib visualisations displaying the history of scores of the top users.




