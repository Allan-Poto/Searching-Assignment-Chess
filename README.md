# Searching-Assignment (Chess)

Individual Assignment for a school module. The actual project tasks pdf are left out due to module policy to not post it online.

## Project 1

Project 1 task is to apply classic search algorithm, namely:

1. Breath-First-Search (BFS)

2. Depth-First-Search (DFS)

3. Uniform-Cost-Search (UCS)

4. A* algorithm

Objective of the project is to solve a maze problem where we need to find a path to the end goal. The problem uses the classic International Chess context, with the addition of some self-made pieces. The implementation of the search algorithm is rather straightforward, with many resources regarding their implementation readily available online as well. I feel that the main challenge instead lies in the OOP code maintainence and extensibility (since they would have to be re-use for project 2 and 3).

### [Breath First Search (BFS)](./Code/uninformed-search/BFS.py)

Implementation of the classic BFS algorithm with early goal test. I included a version of the [Late-Goal-Test BFS](./Code/uninformed-search/LGT_BFS.py) that I started off with as well, which could be useful for other problems. Uses deque as a queue for the frontier.

### [Depth First Search (BFS)](./Code/uninformed-search/DFS.py)

Implementation of the classic DFS algorithm with early goal test. Difference with regards to Early Goal Test BFS is just the deque frontier is used as a stack instead of a queue.

### [Uniform Cost Search (UCS)](./Code/informed-search/UCS.py)

Implementation of the classic UCS algorithm using a "heapq" implemented priority queue as the frontier.

### [A* Search](./Code/informed-search/AStar.py)

Implementation of the classic A* search algorithm using a "heapq" implemented priority queue as the frontier and "euclidean distance" heuristic.

Some testcases can be found in the [Public Testcases](./Code/Public%20Testcases/P1) folder, containing inputs as well as their supposed outputs.

## Project 2

Project 2 task is to apply local-search as well as CSP in solving different versions of the well-known n-queens problem. Here, I found out that the problem was quite different from the project 1 and I had to re-do some of the OOP implementations I did in project 1.

### [Local Search](./Code/local-search/Local.py)

The variation here is of a chessboard filled with many different chess pieces and obstacles. The objective is to remove the minimum number of pieces such that no 2 pieces threatened each other.

I did a implementation of the classic Local search algorithm. Since the problem was given to be static, the approach I adopted here was to keep a total counter of all possible actions for all pieces by assuming an empty board aside from the obstacles (I.E treating all the other pieces as invisible) when the board is first intialized. Then, using the value decrease in counter as the heuristic for the selection of the piece to remove. The value of removing a piece is calculated as follows:
> `Value = SUM( number_of_pieces_threatening_that_piece_position, number_of_positions_threatened_by_that_piece)`

Once the counter reaches 0, it is an indicator that a solution is found where there are no pieces left that are threatened by other pieces.

Other strategies used are:

- *Random restarts*
- *Allowing sideway movements*
- *Steepest descent* when selecting the piece to remove
- *Random Selection as Tie-breakers*

### [Constraint-Search-Problem (CSP)](./Code/csp/CSP.py)

The variation of the n-queen problem here is of an empty chessboard (aside from obstacles). The objective is to placed a stipulated amount of some type of chess pieces onto the board such there are no 2 pieces threatening each other.

Implementation was done using the classic CSP algoritm with forward checking for both unary and binary consistency. Some optimizations included are as follows:

- Most Restricted Variable Heuristic
  - Select the piece with the least amount of positions that can be placed
- Degree Tie-Breaking
  - Select the piece with the most restrictions when placed on the board
  - Order of selection is as follows: Queen -> Princess -> Bishop -> Empress -> Rook -> Knight -> King -> Ferz
- Memoisation
  - Storing all the positions that can be attacked by a piece from a certain position such that re-computation is not required.

Inputs and outputs for testcases can be found in the [Public Testcases](./Code/Public%20Testcases/P2/) P2 folder.  

## Project 3

Project 3 task is to apply adverserial search (alpha-beta pruning) in a game of chess with some tweaking in rules against a few variations of bots created by the professor. Once again, there was a significant change in the OOP implementation due to the difference in the requirement of the problem, which made me realised how hard it was to do up an OOP implementation general enough for multiple problems.

### [Alpha-Beta Pruning](./Code/Adverserial%20Search/AB.py)

My Implementation is done with Alpha-Beta Pruning using the following chess strategies for evaluation function:

- [Material Value](https://www.chessprogramming.org/Material)
  - The value attached each type of chess piece based on their ability and impact
- [Piece-Square Tables](https://www.chessprogramming.org/Piece-Square_Tables)
  - Giving reward or penalty to the pieces for securing specific positions of the board during different part of the game
  - Implemented for Early Game, Mid-Game, and Late-Game where the phase of the game is defined by the material value left on the board
- [King-Safety (Attacking-King-Zone)](https://www.chessprogramming.org/King_Safety#Attacking_King_Zone)
  - Calculation of how safe the King is for either side after making a move

Alpha-Beta Pruning is done only up to a depth of 2 as any further depths will result in the auto-grader for the project timing out (30secs limit), however for a normal implementation, it can done for deeper depths. Result for the implementation are as follows:

`Dummy Agent` - Chooses and plays first available move, does not care even if king is checked.

> `Score: 100% Win (Lose: 0, Draw: 0, Win: 50)`

`Random Agent` - Chooses a random move out of all available moves, does not care if king is checked.

> `Score: 100% Win (Lose: 0, Draw: 0, Win: 50)`

`Greedy Agent` - Chooses according to the following priority (Checkmate -> Checks -> Random moves where their King is Safe).

> `Score: 78% Win, 22% Draw (Lose: 0, Draw: 11, Win: 39)`

`Smart Agent` - Chooses the highest utility valued move (Checkmate -> Check + Capture -> Capture -> Check -> Random moves King Safe).

>`Score: 80% Win, 20% Draw (Lose: 0, Draw: 10, Win: 40)`

`Minimax Agent` - Choose a move based on Minimax Algorithm with a depth of 4 with Smart Agent's evaluation function.

>`Score: 100% Win (Lose: 0, Draw: 0, Win: 50)`

Currently, the agents are not provided in this repository, will add them in the future if I could find time to implement them properly.

## Disclaimer

The projects are done up by the hardworking staffs and professors teaching this module. I am credited only for implementing my version of the solutions for these projects.
