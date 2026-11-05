# Slither and Snack! 🐍 🍎

A simple snake game where you eat apples to grow larger and gain points!

<div align="left">
  <img src="https://github.com/user-attachments/assets/588a3b21-ffc5-4419-956e-f1aaa01f2b46" alt="Slither and Snack Gameplay Screenshot" width="600">
</div>

## How to Run

* Download release files
* Open the file called "Main.exe" 
*The game is ready to play

## How to Play
* Click the space bar to begin
* Use WASD or Arrow Keys to control the snake
* Eat Apples to grow larger and increase your score
* If you crash into a wall or yourself, the game will end
* Try to stay alive for as long as possible

##  Architecture

Our code contains multiple Python files, which can all be executed from the central entry point:
*   `Main.py`

##  Features

*   **Snake Growth:** Adds `+1` block to the snake's length after every apple consumed.
*   **Collision Detection:** Dynamic tracking for impacts against internal walls and the outer window frame.
*   **Smooth Controls:** Full support for both classic `WASD` keys and directional `Arrow Keys`.
*   **Eating System:** Pinpoint collision detection triggers immediate apple relocation upon consumption.
*   **Score Tracker:** Keeps a persistent `+1` score tally per apple eaten.
*   **Leveling System:** Gradually speeds up the snake's movement speed as your score increases, scaling up the difficulty.

##  Built With

*   [Python](https://python.org)
*   [Turtle Graphics Library](https://python.org)
*   `time` Library
*   `random` Library

##  License

This project is licensed under the [MIT License](LICENSE).
