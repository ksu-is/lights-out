# lights-out-game
 
-------

### Recording:

https://kennesawedu.sharepoint.com/sites/Team-IS3020Sp23/Shared%20Documents/Projects%20and%20Presentations/Recordings/Meeting%20in%20_Projects%20and%20Presentations_-20230504_150035-Meeting%20Recording.mp4?web=1

-------

### Introduction

This is Declan Reuschel's project for the IS 3020 class. It is a graphical game built in Python, based on the
Lights Out electronic game, and built on top of an application framework of my own design. For more information
on the framework itself, see below, or see the original repository in my personal profile.

--------

### Overview

'lights-out-game' is based on the electronic Lights Out game. In said game, players must flip a grid of lights
from a randomized pattern to all being turned on. However, players may only flip one light at a time, and doing
so also flips all of the lights around it. In this modified version of the game, there will be multiple difficulties
with infinite levels, as well as a randomized board for each, which will always be guaranteed to be solvable.
The game will be entirely graphical, using the output line strictly for debugging, and may also have sound effects and music.

--------

### General Roadmap (more specific roadmap in dedicated file)

- [x] Setup initial board creation and gameplay
- [x] Create functionality for winning a round, matching the solution
- [x] Set up moving to next round
- [x] Set up move tracking, and ability to undo moves
- [x] Create functionality for losing a round, and resetting
- [x] Create title screen, difficulty selection, and transitions
- [x] Add different difficulties based on selection
- [x] Improve presentation, polish

--------

### Framework

'lights-out-game' is built on top of the 'maybe-a-game' application framework, which is itself built using
Pygame's integration with the SDL library. The framework itself is in a repository on my private profile,
but the summary from the project readme is copied below for reference.

>This project is being built as a way of understanding more about Python itself, and its differences
>when compared to other languages which I have used in the past. The goal of this project is not only
>to eventually reach some kind of useful framework, but also to be written well, using accepted standards
>of development, and be designed in a way which could be considered 'Pythonic'.
>
>This is a simple framework for building applications in Python, through integration with pyGame.
>
>This framework is built on the use of entities to represent anything handling logic, rendering, input, output,
>sound, or general application controls.
>
>Entities may be given image sources for easy rendering, they may not be rendered at all. They can take
>any type of normal input accepted by pyGame, but not all entities need input, and will not request input
>if not necessary, so as to save on performance.
>
>This engine is very focused on object-oriented development, and maintains a strict application loop which controls
>exactly when and in what order entities may run any logic they have. This application loop can be circumvented,
>but this is not necessary for the vast majority of purposes.
