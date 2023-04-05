### Project Roadmap

- [x] Setup initial board creation and gameplay
- [x] Create functionality for winning a round, matching the solution
- [x] Set up moving to next round
- [ ] Set up move tracking, and ability to undo moves
  - [x] ~~Add entity to track available number of moves~~
  - [x] ~~Add assets for said entity~~
  - [x] Add in ability to render move-tracking images to LightControl entity
  - [x] Add assets for said images
  - [ ] Set up these images to track the move counter already in the LightControl entity
  - [ ] Add in move tracker to keep track of previous moves (in LightControl entity)
  - [ ] Add in ability to undo moves through a button (add button entity)
- [ ] Create functionality for losing a round, and resetting
  - [ ] Add in functionality for lights flashing incorrect if all moves are used, but the solution has not been reached
  - [ ] Set up LightControl to automatically undo the last move if this occurs.
  - Note: there will be no actual 'losing' to this game, players may take as much time as they need to find the solution, or give up and return to the title screen
- [ ] Create title screen, difficulty selection, and transitions
- [ ] Add different difficulties based on selection
- [ ] Improve presentation, polish
