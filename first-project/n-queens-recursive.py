"""
N-Queens problem - BFS (Breath First Search)

Team members: 
- Carreón Guzmán Mariana Ivette
- Martínez Ostoa Néstor Iván
- Meza Ortega Fernando
- Pedraza Martínez José Alberto

N-Queens problem is a classic computer science problem could be stated as 
following: 

Description. Find (or count) all the possible ways to arrange n queens (1 <= n <
 inf) inside a nxn chess board in such that the queens must not attack each other.

Input. A integer n that represents the number of queens inside a nxn chess board.

Output. If n is relatively small (n < 8) then the problem should output all the 
possible chess board combinations where the queens cannot attack each other 
and enumerate each of them. Otherwise, just output the number of combinations 
inside the nxn chess board where the queens cannot attack each other.
"""

import copy

class NQueenSolver:
    def __init__(self, num_queens, num_sols_print):
        """NQueenSolver is a class that solves the n-queen problem by using breath
        first search (BFS) tree traversal algorithm. The idea behind this solution
        is to generate, on each iteration, a new set of chessboards combinations
        with one more queen than the previous state. For example, the first state
        will be a nxn chessboard with 0 queens and the second state will be all
        the possible chessboard combinations with 1 queen and so on until we reach
        the n state where the chessboard will accomodate n queens that aren't
        attacking each other.

        Parameters
        ----------
        num_queens: int
            integer representing the number of queens to solve

        Attributes
        ----------
        cost: int
            represents the cost of obtaining all the possible chessboards

        initial_state: list
            list of matrix that contains an nxn 0 matrix. This will be the initial
            state of the algorithm

        num_boards: int
            this integer contains the number of chessboards that contain n queens
            that aren't attacking each other. One can think of this attribute
            as the solution to the problem
        """
        self.num_queens = num_queens
        self.cost = 0
        self.inital_state = [
            [[0]*self.num_queens for _ in range(self.num_queens)]
        ]
        self.num_boards = 0
        self.num_sols_print = num_sols_print

    def find_num_boards(self):
        """Initial function that sets motion for the BFS algorithms. It will start
        the BFS walk and return the solution of the problem which is composed 
        by the number of chessboards that satisfy the condition of the problem 
        and the cost of generating that number of chessboards.

        The bfs function can be stated as having the following parameters:

        bfs parameters
        --------------
        state: list
            list of matrixes representing the current state of the problem. A matrix
            represents a chessboard 
        
        num_level: int
            represents the current level we are exploring. Let's remember that 
            our problem will start in level 0 with the intial state of a list
            of 1 element that contains a matrix of nxn zeros. The problem will stop
            once we have reached the nth level of exploration.

            Each time we go from one level to the other, we are generating only the
            chessboards that satisfy the probem condition. 

        output
        ------
        solution: tuple
            - num_boards: int
                solution to the problem. It represents the number of boards that
                satisfy the problem condition of the n queens.
            - cost: int
                represents the computational cost of generating the num_boards
                solution
        """
        self.bfs(self.inital_state, 0)
        return (self.num_boards, self.cost)

    def bfs(self, level, level_number):
        """This function will have the responsibility of exploring through all the
        possible solutions to the problem and stops whenever the current level 
        is the nth level, which means we have generated all the chessboards
        to a given n in which the positioned queens in the chessboard aren't 
        attacking each other. If we are in the nth level, then, the it will print
        the current node in the graph, in other words, the current chessboard that
        satisfies the problem condition.

        Otherwise, it will call itself again with a new state and increasing the
        current level number in 1. 

        parameters
        ----------
        level: list
            list of matrixes (chessboards) that satisfy the problem condition which
            is a matrix where all the positioned queens do not attack each other. 

        level_number: int
            represents the current level of exploration we are in. Let's remember
            that the problem starts with a level_number = 0 (i.e., a list of 1
            item which is a matrix full of zeros -> chessboard with no queens in 
            it) and ends with level_number = n (i.e., a list of matrixes that
            contain all the possible solutions to the problem -> matrixes that
            contained positioned queens that aren't attacking each other)
        """
        if level_number == self.num_queens:
            for board in level:
                self.num_boards += 1
                if self.num_sols_print > 0:
                    self.print_chessboard(board)
                    self.num_sols_print -= 1
            return
        self.bfs(self.generate_level(level,level_number), level_number + 1)

    def print_chessboard(self, chessboard):
        """ Prints a given chessboard

        Parameters
        ----------
        chessboard: list
            list of matrixes where one matrix represents a solution to the 
            problem
        """
        print(f"Chessboard #{self.num_boards}")
        for pos in range(self.num_queens):
            print(chessboard[pos])
        print()

    def generate_level(self, level, level_number):
        """The purpose of this function is to iterate over all the states in the
        given level. A state is a matrix that contains level_number queens inside
        itself that satisfy the problem condition. In each given state, we generate
        its childrens which are all the possible chessboards with level_number + 1
        queens that satisfy the condition. After doing this, we simply return 
        the new level that contains all the chessboard solutions with level_number
        + 1 queens. 

        Parameters
        ----------
        level: list
            list of matrixes (chessboards) that satisfy the problem condition which
            is a matrix where all the currently positioned queens do not attack 
            each other. 

        level_number: int
            represents the current level of exploration we are in

        Output
        ------
        msg : str
            message that indicates that all the possile children for a given level
            have been generated. After seeing this message, we can be sure that
            no more queens will be added to the chessboard

        new_level: list
            list of nxn matrixes. Each matrix contains level_number + 1 queens 
            that do not attack each other.

        """
        new_level=[]
        for state in level:
            children = self.generate_children(state)
            for child in children:
                new_level.append(child)
            del children
        return new_level

    def generate_children(self, state): 
        """With a given state (chessboard) we generate all the possible children
        that only containt the state's level number + 1 queens that aren't attacking
        each other. We can be sure that the state's level number + 1 will never be
        greater than n (n-queens) since at the function bfs() we validate that
        condition. 

        parameters
        ----------
        state: nxn matrix
            matrix (list of lists) that contains a 0 in a position if there is no
            queen in it and a 1 in a position of there is a queen. This state
            will contain the state's level number of queens and we want to generate
            a new state that containts the state's level number + 1. 

        output
        ------
        children: nxn matrix
            matrix (list of lists) that contains a possible way of accomodating
            state's level number + 1 queen.
        """
        
        children=[]

        """finds an empty column in the current state (chessboard) and will
        update the the empty_column_index with the position of that column. 

        if empty_column_index = -1 means that in the chessboard there isn't an
        empty column, therefore, it's not possible to add a queen.
        """
        queens_in_board=[]
        empty_column_index = -1
        queen = 0	
        for i in range(self.num_queens):
            for j in range(self.num_queens):
                if state[j][i]==1:
                    queens_in_board.append([j,i])
                    queen=1
            if queen == 0: 
                empty_column_index=i 
            queen=0
        
        if empty_column_index==-1:
            return []

        """With the current positions of the queens in the current state, this part
        will be in charge of validating if it's possible to add a new queen
        in a i,j position of the chessboard, if it's possible, then, it will append
        that new chessboard to the list of children.
        """
        possible_to_add_queen = True
        for i in range(self.num_queens):
            for r in queens_in_board:
                if i == r[0]:
                    possible_to_add_queen = False
                    break

                curr_queen_first_diagonal=empty_column_index-i 
                new_queen_first_diagonal = r[1] - r[0]
                curr_queen_second_diagonal = empty_column_index + i 	
                new_queen_second_diagonal = r[1] + r[0] 	
                
                if curr_queen_first_diagonal == new_queen_first_diagonal or curr_queen_second_diagonal == new_queen_second_diagonal:	
                    possible_to_add_queen = False
                    break
            self.cost += 1
            if possible_to_add_queen: 
                new_state=copy.deepcopy(state)
                new_state[i][empty_column_index]=1
                children.append(new_state)
                del new_state
            possible_to_add_queen = True
        del queens_in_board
        return children

if __name__ == "__main__":
    n_queens = int(input("N-queen problem. Insert the number of queens: "))
    n_sols = int(input("Insert the number of solutions to print: "))
    (num_boards, cost) = NQueenSolver(n_queens, n_sols).find_num_boards()
    print("Number of possible chessboards: ", num_boards)
    print("Final cost: ", cost)