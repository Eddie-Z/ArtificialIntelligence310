#!/usr/bin/python3
#CMPT310 A2 Sample solution
import sys, getopt
#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
num_hours_i_spent_on_this_assignment = 0
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
# <Your feedback goes here>
#####################################################
#####################################################

def main(argv):
   inputfile = ''
   N=0
   try:
      opts, args = getopt.getopt(argv,"hn:i:",["N=","ifile="])
   except getopt.GetoptError:
      print ('test.py -n <size of Sodoku> -i <inputputfile>')
      sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':
           print ('test.py -n <size of Sodoku> -i <inputputfile>')
           sys.exit()
       elif opt in ("-n", "--N"):
           N = int(arg)
       elif opt in ("-i", "--ifile"):
           inputfile = arg
   instance = readInstance(N, inputfile)
   toCNF(N,instance,inputfile+str(N)+".cnf")




def readInstance (N, inputfile):
    if inputfile == '':
        return [[0 for j in range(N)] for i in range(N)]
    with open(inputfile, "r") as input_file:
        instance =[]
        for line in input_file:
            number_strings = line.split() # Split the line on runs of whitespace
            numbers = [int(n) for n in number_strings] # Convert to integers
            if len(numbers) == N:
                instance.append(numbers) # Add the "row" to your list.
            else:
                print("Invalid Sudoku instance!")
                sys.exit(3)
        return instance # [[1, 3, 4], [5, 5, 6]]



def toCNF (N, instance, outputfile):
    """ Constructs the CNF formula C in Dimacs format from a sudoku grid."""
    """ OUTPUT: Write Dimacs CNF to output_file """
    output_file = open(outputfile, "w")
    "*** YOUR CODE HERE ***"
    p = N*N*N
    fixednumbers=0
    for i in range(N):
        for j in range(N):
            if instance[i][j] != 0:
                fixednumbers += 1
    cnf = N*N + N*N*N*N*3 - N*N*N*3 + fixednumbers
    output_file.write("p cnf "+str(p)+" "+str(cnf)+"\n" )
    C1(output_file, N)
    C2(output_file, N)
    C3(output_file, N)
    C4(output_file, N)
    C5(output_file, N,instance)
    output_file.close()


def indexToNum (i,j,k,N):
    return (i-1)*N*N + (j-1)*N + k

def C1(output_file, N):
    for i in range(1,N+1):
        for j in range(1,N+1):
            line = ''
            for k in range(1,N+1):
                line += str(indexToNum(i,j,k,N))
                line += " "
            line += "0\n"
            output_file.write(line)

def C2(output_file, N):
    for i in range(1,N+1):
        for j in range(1,N+1):
            for k in range(1,N+1):
                for l in range(1,N+1):
                    line = ''
                    if(k != l):
                        line += str(indexToNum(i,j,k,N)*-1)
                        line += " "
                        line += str(indexToNum(i,j,l,N)*-1)
                        line += " 0\n"
                        output_file.write(line)

def C3(output_file, N):
    for i in range(1,N+1):
        for k in range(1,N+1):
            for j1 in range(1,N+1):
                for j2 in range(1,N+1):
                    line = ''
                    if(j1 != j2):
                        line += str(indexToNum(i,j1,k,N)*-1)
                        line += " "
                        line += str(indexToNum(i,j2,k,N)*-1)
                        line += " 0\n"
                        output_file.write(line)

def C4(output_file, N):
    for j in range(1,N+1):
        for k in range(1,N+1):
            for i1 in range(1,N+1):
                for i2 in range(1,N+1):
                    line = ''
                    if(i1 != i2):
                        line += str(indexToNum(i1,j,k,N)*-1)
                        line += " "
                        line += str(indexToNum(i2,j,k,N)*-1)
                        line += " 0\n"
                        output_file.write(line)


def C5(output_file, N, instance):
    for i in range(N):
        for j in range(N):
            line = ''
            if instance[i][j] != 0:
                line += str(indexToNum(i+1,j+1,instance[i][j],N))
                line += " 0\n"
                output_file.write(line)






if __name__ == "__main__":
   main(sys.argv[1:])
