# Python Quiz Game 

A simple True/False quiz game built using **Object-Oriented Programming (OOP)** in Python. This project dynamically loads questions, keeps track of the user's score, and allows them to exit at any time.

## Features 
- Loads trivia questions dynamically from a dataset.
- Keeps track of the user's score throughout the game.
- Allows the user to exit anytime by typing "exit".
- Uses **OOP principles** (classes and objects) for a structured approach.

## How It Works 
1. The game pulls a list of True/False questions from `data.py`.
2. Each question is stored as an object using the `Question` class.
3. The `QuizBrain` class manages the question flow and score tracking.
4. The user answers each question until the quiz ends, or they choose to exit.
5. The final score is displayed at the end.

## Installation & Running 
### Prerequisites
- Python 3.x installed

### Steps to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/NomadBeetle/Python-Quiz-Game.git
   cd python-quiz-game
   ```
2. Run the script:
   ```bash
   python main.py
   ```
3. Answer the True/False questions to play the quiz!

## File Structure 📁
```
python-quiz-game/
│-- question_model.py    # Defines the Question class
│-- quiz_brain.py        # Controls quiz flow and score tracking
│-- data.py              # Stores quiz questions
│-- main.py              # Runs the quiz game
│-- README.md            # Project documentation (this file)
```

## Example Gameplay 🎮
```
Q1: In 'Space Station 13', the station has a clown aboard it. (True/False)? : True
You got it right!
The correct answer was: True
Your current score is 1/1

Q2: Activision created Battlefield 1. (True/False)? : True
That's Wrong
The correct answer was: False
Your current score is 1/2
...
```

## Contributions 🤝
Feel free to contribute by adding new features or questions! Fork the repo and submit a pull request.

