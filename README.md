# Python Quiz Game

A simple **True/False quiz game** built using **Object Oriented Programming (OOP)** in Python. This project dynamically loads questions, tracks the user's score, and provides a clean GUI using the `tkinter` library.

## Features

* Fetches trivia questions dynamically via API using the `requests` module.
* Displays questions with a clean graphical interface.
* Tracks the user's score in real-time.
* Provides instant feedback after each answer.
* Allows user to quit any time by closing the window.
* Uses **OOP principles** for a modular and maintainable code structure.

## How It Works

1. The app fetches a list of True/False questions from the Open Trivia API.
2. Each question is instantiated as a `Question` object.
3. The `QuizBrain` class manages the game flow, question progression, score, and checking answers.
4. The `QuizInterface` (`ui.py`) handles all GUI logic using `tkinter`.
5. Questions are displayed one by one with True/False buttons.
6. After the last question, the interface shows the final score and disables further input.

## Installation & Running

### Prerequisites

* Python 3.x installed
* `requests` library (install via `pip install requests`)

### Steps to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/NomadBeetle/Python-Quiz-Game.git
   cd python-quiz-game
   ```
2. Run the main script:

   ```bash
   python main.py
   ```
3. Enjoy the quiz with a GUI!

## File Structure

```
python-quiz-game/
│-- question_model.py    # Defines the Question class
│-- quiz_brain.py        # Controls quiz logic and score tracking
│-- ui.py                # Manages the tkinter GUI
│-- main.py              # Entry point of the application
│-- images/              # Folder containing UI image assets
│-- README.md            # Project documentation (this file)
```

## Example Gameplay

A tkinter window opens showing a question:

```
Q: The Great Wall of China is visible from the Moon.
[TRUE] [FALSE]
```

After clicking an answer:

```
Feedback: "That's correct!"
Score: 5/6
```

At the end:

```
You've reached the end of the quiz.
Final Score: 9/10
```

## Contributions

Feel free to contribute by submitting improvements, new features, or bug fixes. Fork the repo and submit a pull request!

## Author

**Azaan (NomadBeetle)**
[GitHub](https://github.com/NomadBeetle) • [LinkedIn](https://linkedin.com/in/NomadBeetle)