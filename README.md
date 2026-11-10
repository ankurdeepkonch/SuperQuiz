# 🪙 Super Quiz

A desktop-based interactive quiz game developed using **Python and CustomTkinter**. Test your general knowledge, race against a 10-second timer, earn coins for correct answers and track your recent quiz scores.

## ✨ Features

- **Player Name:** Enter your name before starting the quiz.
- **Start Button:** Begin the quiz by clicking the Start button after entering your name.
- **Question Bank:** Includes 100 general knowledge questions.
- **Random Questions:** Each round selects 10 random questions.
- **Multiple-Choice Questions:** Four answer options (A, B, C, D).
- **Countdown Timer:** Get 10 seconds to answer each question.
- **Score Tracking:** Earn one point for every correct answer.
- **Coin Reward System:** Earn 10 coins for each correct answer.
- **Results Screen:** View your final score and total coins.
- **Score History:** Displays the five most recent quiz results.
- **File Handling:** Saves player scores locally in a text file.
- **Play Again:** Start a new round with a fresh set of questions.
- **Custom Interface:** A modern desktop interface with a purple-blue theme.

## 🛠️ Technologies Used

- Python
- CustomTkinter
- Random Module
- File Handling
- Exception Handling
- Tkinter GUI and Timer (`after()`)

## 🚀 Getting Started

Follow these steps to set up and run the project manually on your computer.

### 1. Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

Make sure to enable **Add Python to PATH** during installation.

### 2. Create the Project Folder

Create a new folder named `Super-Quiz` on your computer.

### 3. Create the Project Files

Inside the folder, manually create these three files:

- `quiz_game.py` – Main Python application.
- `requirements.txt` – Project dependencies.
- `scores.txt` – Stores quiz results.

### 4. Install CustomTkinter

Open the terminal in your project folder and run:

```bash
pip install customtkinter
```

**Important:** Install this package before running the application.

### 5. Run the Application

Execute the following command in the terminal:

```bash
python quiz_game.py
```

## 🎮 How to Play

1. Launch the application.
2. Enter your name in the player name field.
3. Click the **Start** button to begin the quiz.
4. Read the displayed question.
5. Select one of the four available answers.
6. Submit your answer using the **Save & Next** button.
7. Answer within the 10-second time limit.
8. Earn 10 coins for every correct answer.
9. Complete all 10 questions to see your results.
10. Select **Play Again** to start another round.

## 📁 Project Structure

```text
Super-Quiz/
│
├── quiz_game.py
├── requirements.txt
├── scores.txt
└── README.md
```

## 💾 Score Storage

Quiz results are stored locally in `scores.txt`.

Each result contains:
- Player name
- Final score out of 10
- Total coins earned

**Example:**

```text
Ankur : 8/10 (80 Coins)
Player : 6/10 (60 Coins)
```

## 🔮 Future Improvements

- Add more question categories.
- Introduce difficulty levels.
- Improve the score leaderboard.
- Add sound effects and animations.
- Expand the question bank.

## 👨‍💻 Author

**Ankur Deep Konch**