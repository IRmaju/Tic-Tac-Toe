# 🎮 Tic-Tac-Toe Game - Play Against Each Other!

Welcome to the **Tic-Tac-Toe** game, where you can play with another person! The objective is simple: get three of your marks (either "X" or "O") in a row to win. Enjoy the game on a 3x3 board!

## 📝 Features:
- **Two Players Mode**: You play against another person, switching between "X" and "O".
- **Winner Detection**: The game will show you a message when one player wins, or when the game is a draw.
- **Game Reset**: You can restart the game easily with the "Restart Game" button.

## 🚀 How to Run

1. **Install Streamlit**:
   First, install Streamlit using pip if you haven't already:

   ```bash
   pip install streamlit
🎨 App Interface
Game Board: The 3x3 grid is displayed, and you can click on the empty spaces to place "X" or "O".

Turn Indicator: It shows whose turn it is ("X" or "O").

Winner Notifications: After each game, a message will pop up to tell you if a player won or if it was a draw.

⚙️ Game Logic Breakdown
1. Turn Switching:
Players alternate turns between "X" and "O" after each move.

The game automatically checks if a player wins after every move.

2. Winner Detection:
The game checks all rows, columns, and diagonals to determine if there is a winner.

3. Game Reset:
The "Restart Game" button resets the board, allowing you to play again from the beginning.

💡 How It Works
Game Play Flow:
The game starts with Player X.

Players alternate placing "X" and "O" on the board.

The game checks for a winner after each move.

If someone wins, it displays a winning message. If the board is full and no one wins, it’s a draw.

The "Restart Game" button resets everything for a new round.

📄 License
This project is open-source and available under the MIT License.

🧑‍💻 Tech Stack
Python: For backend logic.

Streamlit: To build the interactive web interface.

Session State: To keep track of the game state (board, current turn, winner).

🖍️ Contributing
Feel free to fork the repository and submit pull requests to improve the game, add new features, or fix bugs. Your ideas are welcome!
🏆 Try Your Luck!
Can you outsmart your opponent and win? Play now to challenge your friends and family to a game of Tic-Tac-Toe!


