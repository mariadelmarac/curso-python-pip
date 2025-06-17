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
   cd game
   python3 main.py
   ```

Here’s an English version of the `README.md` file for your project:

```markdown
# Population Data Visualization Project

This project is a data visualization tool that generates bar charts and pie charts based on population data from South American countries. The data is extracted from a CSV file and used to create visualizations using the `matplotlib` library.

## Project Structure

The project consists of the following files:

- `main.py`: The main script that runs the program. It reads data from the CSV file, filters data for South America, generates a pie chart showing the world population percentages of each country, and allows the user to select a country to generate a bar chart of its historical population.

- `charts.py`: Contains functions to generate bar charts and pie charts using `matplotlib`.

- `read_csv.py`: Reads a CSV file and converts it into a list of dictionaries, where each dictionary represents a country with its respective data.

- `utils.py`: Contains helper functions to retrieve a country's population and filter data by country.

## Requirements

To run this project, you need Python 3 and the following libraries installed:

- `matplotlib`

You can install the required dependencies by running:

```bash
pip3 install -r requirements.txt
```

## Usage Instructions

1. Clone the repository:

   ```bash
   git clone <REPOSITORY_URL>
   ```

2. Navigate to the project directory:

   ```bash
   cd app
   ```

3. Activate the virtual environment (if applicable):

   ```bash
   source env/bin/activate
   ```

4. Install the dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

5. Run the main script:

   ```bash
   python3 main.py
   ```

6. Follow the instructions in the terminal to select a country and generate the charts.

## Example Usage

When you run `main.py`, the program will generate a pie chart showing the world population percentages of South American countries. Then, it will prompt you to enter a country name to generate a bar chart displaying the historical population of that country.

## Contributions

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License

This project is open-source and available under the MIT License. Feel free to modify and distribute it as you see fit.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## Author

mariadelmarac

---

Enjoy the game! 🎮