# Rock, Paper, Scissors Game

This is a simple Python implementation of the classic Rock, Paper, Scissors game. The game is played between the user and the computer, and the first to win 3 rounds is declared the winner.

## How to Play

1. **Run the Script**: Execute the Python script in your terminal or IDE.
2. **Choose Your Move**: When prompted, type `rock`, `paper`, or `scissors` to make your selection.
3. **See the Result**: The computer will randomly select its move, and the winner of the round will be displayed.
4. **Win the Game**: The game continues until either the user or the computer wins 3 rounds.

## Game Rules

- **Rock beats Scissors**: Rock crushes scissors.
- **Scissors beats Paper**: Scissors cut paper.
- **Paper beats Rock**: Paper covers rock.

If both the user and the computer choose the same option, the round is a tie.

## Code Overview

The game is implemented using a `while` loop that continues until one of the players reaches 3 wins. Here's a breakdown of the code:

- **Options**: The game options (`rock`, `paper`, `scissors`) are stored in a tuple.
- **Score Tracking**: Variables `user_wins` and `computer_wins` keep track of the number of wins for each player.
- **Round Counter**: The `rounds` variable keeps track of the current round number.
- **User Input**: The user is prompted to enter their choice, which is then converted to lowercase.
- **Computer Choice**: The computer randomly selects an option using `random.choice()`.
- **Determine the Winner**: The code compares the user's choice with the computer's choice to determine the winner of the round.
- **End Game**: The game ends when either the user or the computer reaches 3 wins.

## Example Output

```
**********
Round 1
**********
User wins: 0
Computer wins: 0
Rock, paper or scissors -> rock
User option -> rock
Computer option -> scissors
User wins!
**********
Round 2
**********
User wins: 1
Computer wins: 0
Rock, paper or scissors -> paper
User option -> paper
Computer option -> paper
It's a tie
**********
Round 3
**********
User wins: 1
Computer wins: 0
Rock, paper or scissors -> scissors
User option -> scissors
Computer option -> rock
Computer wins!
...
The user is the winner!
```

## Requirements

- Python 3.x

## How to Run

1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the following command:

   ```bash
   python3 main.py
   ```

## License

This project is open-source and available under the MIT License. Feel free to modify and distribute it as you see fit.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## Author

[Your Name]

---

Enjoy the game! 🎮