# lights-out-game

This is Declan Reuschel's project for the IS 3020 class. It is a graphical game built in Python, based on the
Lights Out electronic game, and built on top of an application framework of my own design. For more information
on the framework itself, see below, or see the original repository in my personal profile.

--------

This project is being built as a way of understanding more about Python itself, and its differences
when compared to other languages which I have used in the past. The goal of this project is not only
to eventually reach some kind of useful framework, but also to be written well, using accepted standards
of development, and be designed in a way which could be considered 'Pythonic'.

This is a simple framework for building applications in Python, through integration with pyGame.

This framework is built on the use of entities to represent anything handling logic, rendering, input, output,
sound, or general application controls.

Entities may be given image sources for easy rendering, they may not be rendered at all. They can take
any type of normal input accepted by pyGame, but not all entities need input, and will not request input
if not necessary, so as to save on performance.

This engine is very focused on object-oriented development, and maintains a strict application loop which controls
exactly when and in what order entities may run any logic they have. This application loop can be circumvented,
but this is not necessary for the vast majority of purposes.
