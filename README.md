
# 🪙 Super Quiz

A desktop-based interactive quiz game developed using **Python and CustomTkinter**. Test your general knowledge, race against a 10-second timer, earn coins for correct answers, and track recent quiz scores.

## ✨ Features

- **Player Name:** Enter your name before playing.
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

Follow these steps to run the project on your computer.

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd YOUR_PROJECT_FOLDER
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python quiz_game.py
```

## 🎮 How to Play

1. Launch the application.
2. Enter your name.
3. Read the displayed question.
4. Select one of the four available answers.
5. Submit your answer using the **Save & Next** button.
6. Answer within the 10-second time limit.
7. Earn 10 coins for every correct answer.
8. Complete all 10 questions to see your results.
9. Select **Play Again** to start another round.

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

Example:

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

Ankur Deep Konch