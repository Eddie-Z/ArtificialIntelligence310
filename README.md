# ArtificialIntelligence310

CMPT310_PACMAN:
Objective: 
  -Implement BFS, DFS for depthFirstSearch and  breadthFirstSearch functions.
  -Implement A* graph search in the empty function aStarSearch in search.py.
  -Implement the CornersProblem search problem in searchAgents.py.
  -Implement a heuristic for the CornersProblem in cornersHeuristic.
Results:
  Using commands in terminal:
    python pacman.py -l tinyMaze -p SearchAgent.
    python pacman.py -l mediumMaze -p SearchAgent.
    python pacman.py -l bigMaze -z .5 -p SearchAgent.
  Shows:
    The Pac-Man board will show an overlay of the states explored, and the order in which they were explored (brighter red means earlier exploration). 


CMPT310_DPLL:
Objective:
  Complete the empty function toCNF in sudoku.py. The function toCNF takes three arguments: the number N, an instance of sudoku of size NxN, and a string (for the name of output file).
  
  Implement unit propagation for propagate-units(F).
  Implement pure elimination for pure-elim(F).
  Implement recursive backtracking for solve(var,F).

Results:
  Using commands in terminal:
  python sudoku.py -n 3 -i sudoku3_unsat.txt
  python sudoku.py -n 5 
  python sudoku.py -n 9 -i sudoku9.txt
  
  python DPLLsat.py -i <inputCNFfile> 
  
  Shows:
    Correctly generated:
    sudoku3_unsat.txt3.cnf
    5.cnf
    sudoku9.txt9.cnf
    
    Program should print “UNSAT” if a formula is unsatisfiable and "SAT" if it is satisfiable.
    
CMPT310_ECOLI:
Objective:
  Implement HMM.logprob() calculates the probability of a particular sequence of states and characters.
  Implement HMM.viterbi() uses the Viterbi algorithm to calculate the most likely sequence of states given a sequence of DNA characters.
 
Results:
  Using commands in terminal:
  python a3_template.py "small.txt"
  python a3_template.py "ecoli.txt"
  
  Shows:
  E. coli output named ecoli_output.txt.


CMPT310_HMM
Objective:
  Implement compute_activations.
  Implement backpropgration.

Results:
  Using commands in terminal
  python digit_classification.py --mode=test --model=model-20190328-164647.pkl

  Shows:
  Displays number.
  
  
  
