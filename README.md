CMPT310_PACMAN:<br/>
Objective: <br/>
  -Implement BFS, DFS for depthFirstSearch and  breadthFirstSearch functions.<br/>
  -Implement A* graph search in the empty function aStarSearch in search.py.<br/>
  -Implement the CornersProblem search problem in searchAgents.py.<br/>
  -Implement a heuristic for the CornersProblem in cornersHeuristic.<br/>
Results:<br/>
  Using commands in terminal:<br/>
    -python pacman.py -l tinyMaze -p SearchAgent.<br/>
    -python pacman.py -l mediumMaze -p SearchAgent.<br/>
    -python pacman.py -l bigMaze -z .5 -p SearchAgent.<br/>
  Shows:<br/>
    The Pac-Man board will show an overlay of the states explored, and the order in which they were explored (brighter red means earlier exploration). 


CMPT310_DPLL:<br/>
Objective:<br/>
  -Complete the empty function toCNF in sudoku.py. The function toCNF takes three arguments: the number N, an instance of sudoku of size NxN, and a string (for the name of output file).<br/>
  
  Implement unit propagation for propagate-units(F).<br/>
  Implement pure elimination for pure-elim(F).<br/>
  Implement recursive backtracking for solve(var,F).<br/>

Results:<br/>
  Using commands in terminal:<br/>
  python sudoku.py -n 3 -i sudoku3_unsat.txt<br/>
  python sudoku.py -n 5 <br/>
  python sudoku.py -n 9 -i sudoku9.txt<br/>
  
  python DPLLsat.py -i <inputCNFfile> <br/>
  
  Shows:<br/>
    Correctly generated:<br/>
    sudoku3_unsat.txt3.cnf<br/>
    5.cnf<br/>
    sudoku9.txt9.cnf<br/>
    
   Program should print “UNSAT” if a formula is unsatisfiable and "SAT" if it is satisfiable.<br/>
    
CMPT310_ECOLI:<br/>
Objective:<br/>
  Implement HMM.logprob() calculates the probability of a particular sequence of states and characters.<br/>
  Implement HMM.viterbi() uses the Viterbi algorithm to calculate the most likely sequence of states given a sequence of DNA characters.<br/>
 
Results:<br/>
  Using commands in terminal:<br/>
  python a3_template.py "small.txt"<br/>
  python a3_template.py "ecoli.txt"<br/>
  
  Shows:<br/>
  E. coli output named ecoli_output.txt.<br/>


CMPT310_HMM<br/>
Objective:<br/>
  Implement compute_activations.<br/>
  Implement backpropgration.<br/>

Results:<br/>
  Using commands in terminal<br/>
  python digit_classification.py --mode=test --model=model-20190328-164647.pkl<br/>

  Shows:<br/>
  Displays number.<br/>
  
  
  
