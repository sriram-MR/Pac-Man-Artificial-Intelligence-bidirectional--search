# Pac-Man-Artificial-Intelligence-bidirectional--search

TO run this,

download, Pac-Man-Artificial-Intelligence-single-Agent-search repository and replace these files of same name with the same name.

Instruction to run Code:

THe Project executes BFS,A*, Biderectioanl Brute Foce Search and Bidirectioanl Heuristics search
Most of the code used is here based out of our Project 1

Requirements:

The Code is written in python and Python 2.7 should be used to run te code.


Search algorithms are added and edited in Search.py
probelms and heuristics are modified in Searchagent.py

Running the code:
Our Problem and heuristics are based out of our project1, so that code will run for only the problem defined in that project.
The program can be run for 4 maze world, similar to that of our project 1

To run the code

To run the BFS in a tiny maze : python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs, prob=PositionSearchProblem, heuristic=foodHeuristic

so for different search algorithms, use 
fn = astar for A* algorithm
fn = bd for Bi directional heuristics algorithm
fn = bd0 for Bi directional Brute force algorithm
in the above line.

similarly, for different Mazes, use
bigMaze, mediumMaze and smallMaze in place of tinyMaze


Thank you,
Happy coding
