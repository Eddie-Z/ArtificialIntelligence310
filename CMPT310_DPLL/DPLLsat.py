#!/usr/bin/python3
#CMPT310 A2 Sample solution

import sys, getopt
import copy
import random

class SatInstance:
    def __init__(self):
        pass
    def from_file(self, inputfile):
        self.clauses = list()
        self.VARS = set()
        self.p = 0
        self.cnf = 0
        with open(inputfile, "r") as input_file:
            self.clauses.append(list())
            maxvar = 0
            for line in input_file:
                tokens = line.split()
                if len(tokens) != 0 and tokens[0] not in ("p", "c"):
                    for tok in tokens:
                        lit = int(tok)
                        maxvar = max(maxvar, abs(lit))
                        if lit == 0:
                            self.clauses.append(list())
                        else:
                            self.clauses[-1].append(lit)
                if tokens[0] == "p":
                    self.p = int(tokens[2])
                    self.cnf = int(tokens[3])
            assert len(self.clauses[-1]) == 0
            self.clauses.pop()
            if not (maxvar == self.p):
                print("Non-standard CNF encoding!")
                sys.exit(5)
      # Variables are numbered from 1 to p
        for i in range(1,self.p+1):
            self.VARS.add(i)
    def __str__(self):
        s = ""
        for clause in self.clauses:
            s += str(clause)
            s += "\n"
        return s

def main(argv):
   inputfile = ''
   verbosity=False
   inputflag=False
   try:
      opts, args = getopt.getopt(argv,"hi:v",["ifile="])
   except getopt.GetoptError:
      print ('DPLLsat.py -i <inputCNFfile> [-v] ')
      sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':
           print ('DPLLsat.py -i <inputCNFfile> [-v]')
           sys.exit()
    ##-v sets the verbosity of informational output
    ## (set to true for output veriable assignments, defaults to false)
       elif opt == '-v':
           verbosity = True
       elif opt in ("-i", "--ifile"):
           inputfile = arg
           inputflag = True
   if inputflag:
       instance = SatInstance()
       instance.from_file(inputfile)
       solve_dpll(instance, verbosity)
   else:
       print("You must have an input file!")
       print ('DPLLsat.py -i <inputCNFfile> [-v]')


""" Question 2 """
# Finds a satisfying assignment to a SAT instance,
# using the DPLL algorithm.
# Input: a SAT instance and verbosity flag
# Output: print "UNSAT" or
#    "SAT"
#    list of true literals (if verbosity == True)
#    list of false literals (if verbosity == True)
#
#  You will need to define your own
#  solve(VARS, F), pure-elim(F), propagate-units(F), and
#  any other auxiliary functions

def propagate_units(F):
	unitClauses = []
	newUnitClauses = False
	for clause in F:
		if(len(clause) == 1):
			unitClauses.append(clause[0])
    # for each unit clause [x]
    #remove all non-unit clauses containing x
	for unit_clause in unitClauses:
		F[:] = [clause for clause in F if not (unit_clause in clause and len(clause) > 1)]
    # for each unit clause [x]
    #remove all -x
	for unit_clause in unitClauses:
		for clause in F:
			if (-1*unit_clause) in clause:
				clause.remove(-1*unit_clause)
				if(len(clause) == 1):
					newUnitClauses = True
	if(newUnitClauses):
		propagate_units(F)
	return F

def printer(F):
  true = []
  false = []
  for i in F:
    if i[0] > 0:
      true.append(i)
    else:
      false.append(i)
      # print("list of false literals: " + str(false))

  print("list of true literals: " + str(true))
  print("list of false literals: " + str(false))

	# x = flatten(propagate_units(F))

def pure_elim(F):
    #Get all literals
    literals = []
    for clause in F:
      for literal in clause:
        if not literal in literals:
          literals.append(literal)
#for each literals x
    #if x is pure in F and [x] not in F then add [x] to F
    for x in literals:
      isPure = True
      for clause in F:
        if -x in clause:
          isPure = False
          break
      if isPure and [x] not in F:
          F.append([x])
          propagate_units(F)

#Pick the first literal from a random nonUnit clause.
def pick_a_variable(F):
  nonUnitClauses = [clause for clause in F if len(clause) > 1]
  if(len(nonUnitClauses)>0):
    return random.choice(nonUnitClauses)[0]
  else:
    return 0;


def solve(VARS, F):
	propagate_units(F)
	pure_elim(F)

	for clause in F:
		if len(clause) == 0:
			return []
	setOfUnitVars = set()
	for clauses in F:
		if len(clauses)>1:
			break;
		else:
			setOfUnitVars.add(abs(clauses[0]))
	if(len(setOfUnitVars) == len(VARS)):
		return F
	x = pick_a_variable(F)
    #If x==0, no more x can be choosen and there are no empty clauses in F
    #So we have some "Don't care" variables
    # Return F as is
	if(x==0):
		return F
	tmpF1 = copy.deepcopy(F)
	tmpF2 = copy.deepcopy(F)
	sol = solve(VARS, tmpF1 + [[x]])
	if not sol == []:
		return sol # works to have +x
	else :
		return solve(VARS, tmpF2 + [[-1*x]]) # check -x

def solve_dpll(instance, verbosity):
    # print(instance)
    #instance.VARS goes 1 to N in a dict
    # print(instance.VARS)
    # print(verbosity)
    ###########################################
    # Start your code

    clauses = instance.clauses
    variables = instance.VARS

    result = solve(variables, clauses)
    if(result == []):
        print("UNSAT")
    else:
        print("SAT")
        if verbosity == True:
            	printer(result)




    # End your code
    return True
    ###########################################


if __name__ == "__main__":
   main(sys.argv[1:])
