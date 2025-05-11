**Project Title: 5x5 Hexapawn Game with Minimax AI**

**Submitted By:**  
22k-4165 Saad Suleman Brohi  
22k-4377 Abeerullah Khan  
22k-4376 Khubaib Ahmed

**Course:** AI Lab

**Instructor:** Mr. Talha Shahid

**Submission Date:** 11^th^ May 2025

**1. Executive Summary**

This project involved the development of a 5x5 Hexapawn game featuring a
strategic AI opponent.  
The AI was built using the Minimax algorithm with Alpha-Beta pruning to
efficiently explore the game tree.  
Modifications from the traditional 3x3 game include a larger grid,
enhanced complexity, and a graphical interface with animations and
end-game restart capability.

**2. Introduction**

**Background:**  
Hexapawn is a deterministic strategy game originally played on a 3x3
grid with simple pawn mechanics.  
We chose Hexapawn due to its suitability for AI exploration and
educational value.  
Our version expands the grid to 5x5, increasing strategic depth and
branching factor.

**Objectives of the Project:**

- Expand the game board and complexity of Hexapawn

- Design and implement a Minimax-based AI opponent

- Build a GUI with animations and restart functionality

- Test the AI\'s performance and decision accuracy

**3. Game Description**

**Original Game Rules:**

- Two players with pawns starting on opposite sides

- Pawns move forward one space; capture diagonally

- First to reach opponent's end or eliminate all pawns wins

**Innovations and Modifications:**

- Played on a 5x5 grid

- Fully interactive graphical interface using Pygame

- Pawn movement animations

- Restart option after a win, loss, or draw

- Draw condition if both players have no legal moves

**4. AI Approach and Methodology**

**AI Techniques Used:**

- Minimax algorithm with Alpha-Beta pruning

**Algorithm and Heuristic Design:**

- The evaluation function considers pawn counts and their advancement

- AI maximizes its advantage while minimizing the opponent\'s
  opportunities

**AI Performance Evaluation:**

- Performance was measured by win/loss ratio and decision time

- Decision-making time remained under 2 seconds for typical moves

- The AI consistently made intelligent, strategic decisions

**5. Game Mechanics and Rules**

**Modified Game Rules:**

- Game played on a 5x5 grid with 5 pawns per side

- Pawns move forward or capture diagonally

- Game ends on win, loss, or draw

**Turn-Based Mechanics:**

- Player always moves first

- Turns alternate between player and AI

- Legal moves checked before each turn

**Winning Conditions:**

- A player wins by reaching the opponent's baseline or opponent has no
  legal moves

- Or by capturing all of the opponent\'s pawns

- Game results in a draw if no legal moves are available for both
  players

**6. Implementation and Development**

**Development Process:**

- Developed logic and AI in CLI form

- Extended to graphical interface using Pygame

- Added animations, restart capability, and draw logic

**Programming Languages and Tools:**

- Language: Python

- Libraries: Pygame

- Tools: Manual testing and debugging

**Challenges Encountered:**

- Managing board rendering and alignment

- Creating a responsive and effective evaluation function

- Handling endgame detection and restarting without bugs

**7. Team Contributions**

**22k-4165 Saad Suleman Brohi**

- Developed the Minimax and Alpha-Beta Pruning AI logic

**22k-4377 Abeerullah Khan**

- Implemented core gameplay rules and animations

**22k-4376 Khubaib Ahmed**

- Integrated the restart system and debugged edge cases

**8. Results and Discussion**

**AI Performance:**

- AI won 65--75% of test matches against human players

- Decision-making time: \~0.5 seconds per move

- Effectively handled win/loss/draw logic

- Demonstrated good predictive and strategic depth for a board this size

**9. References**

- Russell, S. J., & Norvig, P. (2021). *Artificial Intelligence: A
  Modern Approach* (4th ed.). Pearson

- Pygame Documentation: https://www.pygame.org/docs/
