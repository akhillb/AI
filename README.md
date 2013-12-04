AI
==

This is the repo for my AI assignments

FILE STRUCTURE:
The folder consists of 6 source files:
-> main.py
     The main file
-> buildgraph.py
     This file declares the classes and functions for a city,edge and Graph respectively.
-> greedy.py
      This file is for the implementation of greedy algorithm 
-> input.py
      This file is for building the distance matrix for the given number of cities
-> nearest.py
      This file contains the implementation of Nearest Neighbour algorithm
-> savings.py 
      This file contains the implementation of Savings Heuristic
It consists of 2 input files euc_7 and euc_100. euc_7 has 7 cities and euc_100 has 100 cities 

INPUT FORMAT:
Input should be from a file and the file should be in the following format
The first line will be the number of cities. The next lines should be the coordinates of the each city. The numbering of the cities start from 1 till the number of cities. This will be followed by the distance of each city to other cities in the respective order.

OUTPUT FORMAT:
For the Nearest Neighbour it prints only the order of the cities seperated by a space, for the greedy it  prints the edge it is considering, and the partial tours it has constructed so far and then later it prints the path it found. For savings it prints the two cycles it is merging with and the result of the merging and then later it prints the path it found.
