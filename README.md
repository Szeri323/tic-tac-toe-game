# Tic Tac Toe Game ❌/⭕
## Rules 📜
### This is a typical Tic Tac Toe game where two players place crosses and O's on the board. The main goal of the game is to make three identical signs in a horizontal, vertical, or diagonal direction before the opponent.
## Project Assumptions ✔️
### Gameplay Assumptions: 
- Two-Player Mode - The game should support a two-player mode where each player takes turns to make a move.
- Turn-Based System - Turns should alternate between the two players, allowing each player to move one after the other.
- Game End Conditions:
    The game ends when a player successfully places three identical marks in a horizontal, vertical, or diagonal line.
    The game also ends in a draw if all 9 rounds (moves) are completed without any player achieving the winning condition.
### Architecture Assumptions
- Object-Oriented Programming (OOP) - The project should utilize object-oriented programming principles as much as possible to ensure modularity and reusability of the code.
- Error Handling - The program should be robust and handle user input errors gracefully. This includes:
  - Preventing inputs that exceed the board's dimensions.
  - Handling non-numeric inputs appropriately.
  - Ensuring players cannot place a mark in an already occupied cell.
- Code Structure - The project should be organized into classes and methods that clearly define the game's components and logic. This may include:
  - A Game class to manage the overall game state and flow.
  - A Board class to manage the board's state and display.
  - A Player class to manage player-specific information and actions.
- User Interface - Although the initial version may use a simple text-based interface, the code should be structured in a way that allows for easy updates or enhancements, such as adding a graphical user interface (GUI) in the future.
### Game flow and how to play the game:
- Player Input - Players will be prompted to enter their moves in the format "row,column". For example, entering "1,2" will place the player's mark in the *second row and the *third column.
- Switching Turns - The game will automatically switch turns between the two players after each valid move.
- Winning Condition - The game will check for a winning condition (three identical signs in a row, column, or diagonal) after each move. If a player wins, a message will be displayed.
- Draw Condition - If all spots on the board are filled and there is no winner, the game will declare a draw.
- Restarting the Game - After a game ends, players can choose to restart the game by following the prompts.
## Main Problems 👷🏻‍♂️
### At the moment, the biggest problem for me is the logic and optimal array operations. I created some end-game patterns to match, but they don't account for the opponent's moves. In other words, if there were only one player, the logic would be fine, but the patterns don't include the opponent's moves.
## Download and Installation 📥
### This project doesn't require any external libraries. You only need to have Python 3.x installed. To run the game, follow these steps:
- Clone the repository:
  - Open your terminal and execute the following command:
    ``` bash
    git clone https://github.com/Szeri323/tic-tac-toe-game.git
    ```
  - Navigate to the project directory:
    ``` bash
    cd tic-tac-toe-game
    ```
  - Run the game script:
    ``` bash
    python main.py
    ```
    or if you on linux/mac:
    ``` bash
    python3 main.py
    ```
  
  
