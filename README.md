# Slither and Snack! 🐍 🍎

A revamped version of the original snake game! This game includes navigating walls, avoiding leaving the confines of the world, and eating apples.

<div align="center">
  <img src="https://github.com/user-attachments/assets/588a3b21-ffc5-4419-956e-f1aaa01f2b46" alt="Slither and Snack Gameplay Screenshot" width="600">
</div>

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
