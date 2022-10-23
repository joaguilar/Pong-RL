# Pong-RL
Pong Implementation to try out Reinforcement Learning

Based on these two tutorials:

1. [Learning Pygame by making Pong](https://www.youtube.com/watch?v=Qf3-aDXG8q4) - Base implementation of Pong
2. [Python Pong AI Tutorial - Using NEAT](https://www.youtube.com/watch?v=2f6TmKm7yx0) - Not using NEAT here but got some ideas

# Installation

1. Create a conda environment:

```
conda create --prefix .\Pong-RL python=3.9
```

2. Activate the environment:

```
conda activate .\Pong-RL
```

3. Install prerequisites:

```
pip install -r requirements.txt
```

# Structure

This game was developed using [pygame](https://www.pygame.org/) as a way to both learn pygame and practice Reinforcement Learning, including how to connect the RL process with a pygame game.

Pygame games have two parts:

1. Setup, where all the game logic and datais initialized
2. Game loop, a loop where pygame draws and udpates the game state

## Drawing

* Display Surface
  * Only one, created with:

* Surface (Regular):
  * Used to organize, can have as many as you want, need to be attached to the display surface

* Rect(angle...):
  * Can be put around shapes, used to measure and manipulate them.

* Colors:
  * Values: (red, green, blue)
  * Or color name using `pygame.color('name')`. Names can be found on the [Named Colors](https://www.pygame.org/docs/ref/color_list.html) page.

## Animation

Done by telling pygame to move the coordinates a little bit every cycle in the loop





# Running the Game

