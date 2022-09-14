import sys
from collections import deque

# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
######## Board
#############################################################################
class Board:

    def __init__(self, rows, cols, grid):
        self.rows = rows # Height
        self.cols = cols # Width
        self.grid = grid # The layout
        self.piece_dict = { # To map the pieces
            "King": "Ki",
            "Queen": "Qu",
            "Rook": "Ro",
            "Bishop": "Bi",
            "Knight": "Kn",
            "Ferz": "Fe",
            "Princess": "Pr",
            "Empress": "Em"
        }
    
    def get_height(self):
        return self.rows
        
    def get_width(self):
        return self.cols 
        
    def get_grid(self):
        return self.grid
       
    def get_piece_dict(self):
        return self.piece_dict
        
    def get_coordinate_value(self, row, col):
        return self.grid[row][col]
    
    def set_coordinate(self, row, col, new_value):
        self.grid[row][col] = new_value
        # print(f'Coordinate ({row}, {col}) is set to {new_value}')
    
    
    #def print_grid(self):
    #    print("/\t", end = "")
    #    for k in range(97, 97 + self.get_width()): # Print col index
    #        print(chr(k) + "\t", end = "")
    #    print("\n")
    #    for i in range(self.get_height()):
    #      print(str(i) + "\t", end = "") # Print row index
    #       for j in range(self.get_width()):
    #           print(str(self.get_grid()[i][j]) + "\t", end = "")
    #       print("\n")
            
    def update_grid(self, piece, new_coordinate):
        self.set_coordinate(new_coordinate[0], new_coordinate[1], self.piece_dict[piece.get_name()])
        
#############################################################################
######## Piece
#############################################################################
class Piece:

    def __init__(self, name, coordinate, tag):
        self.name = name
        self.coordinate = coordinate
        self.tag = tag
        self.actionables = []
    
    def get_name(self):
        return self.name
    
    def get_position(self):
        return self.coordinate
        
    def get_tag(self):
        return self.tag
        
    def get_actionables(self):
        return self.actionables
    
    def update_position(self, new_coordinates):
        self.coordinate = new_coordinates
    
    def set_actionables(self, new_actionables):
        self.actionables = new_actionables
        
    @staticmethod    
    def check_legality_king(board, coordinate, threatened): # Only for King
        """
        RETURNS TRUE IF MOVEMENT TO THE POSITION IS LEGAL -> NO OBSTACLES, NOT OCCUPIED BY OTHER PIECES, NOT THREATENED
        """
        flag = False
        if board.get_coordinate_value(coordinate[0], coordinate[1]) != -1 and type(board.get_coordinate_value(coordinate[0], coordinate[1])) != str and (coordinate in threatened.keys()) == False:
            flag = True            
        return flag
    
    @staticmethod
    def check_legality_others(board, coordinate):
        """
        RETURNS TRUE IF MOVEMENT TO THE POSITION IS LEGAL -> NO OBSTACLES, NOT OCCUPIED BY OTHER PIECES
        """
        flag = False
        if board.get_coordinate_value(coordinate[0], coordinate[1]) != -1 and type(board.get_coordinate_value(coordinate[0], coordinate[1])) != str:
            flag = True
        return flag

    @staticmethod
    def King(board, new_coordinate, threatened={}):
        """
        RETURNS ALL NEW POSSIBLE ACTIONS THAT CAN BE TAKEN BY THE KING IN ITS NEW POSITION AFTER MOVEMENT
        """
        new_actionables = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_x = new_coordinate[0] + i
                new_y = new_coordinate[1] + j
                if new_x < 0 or new_y < 0 or new_x >= board.get_height() or new_y >= board.get_width(): # Check if they are out of bounds
                    continue
                elif (new_x, new_y) == new_coordinate:
                    continue
                else:
                    new_actionables += [ (new_x , new_y) ]
        for action in new_actionables.copy():
            if Piece.check_legality_king(board, action, threatened): # If available, do not remove
                continue
            else:
                new_actionables.remove(action) # Else remove
        return new_actionables            
        
    @staticmethod
    def Rook(board, new_coordinate):
        """
        RETURNS ALL NEW POSSIBLE ACTIONS THAT CAN BE TAKEN BY THE ROOK IN ITS NEW POSITION AFTER MOVEMENT
        """
        new_actionables = []
        
        North_x = new_coordinate[0] - 1
        East_y = new_coordinate[1] + 1
        South_x = new_coordinate[0] + 1
        West_y = new_coordinate[1] - 1
        
        while North_x >= 0: # Row decreasing
            # Check obstacles and other pieces
            if Piece.check_legality_others(board, (North_x, new_coordinate[1])):
                new_actionables += [ (North_x, new_coordinate[1]) ]
                North_x -= 1
            else:
                break
        while East_y < board.get_width(): # Col increasing
            # Check obstacles and other pieces
            if Piece.check_legality_others(board, (new_coordinate[0], East_y)):
                new_actionables += [ (new_coordinate[0], East_y) ]
                East_y += 1
            else:
                break
        while South_x < board.get_height(): # Row increasing
            # Check obstacles and other pieces
            if Piece.check_legality_others(board, (South_x, new_coordinate[1])):
                new_actionables += [ (South_x, new_coordinate[1]) ]
                South_x += 1
            else:
                break
        while West_y >= 0: # Col decreasing
            # Check obstacles and other pieces
            if Piece.check_legality_others(board, (new_coordinate[0], West_y)):
                new_actionables += [ (new_coordinate[0], West_y) ]
                West_y -= 1
            else:
                break
        return new_actionables       

    @staticmethod    
    def Bishop(board, new_coordinate):
        """
        RETURNS ALL NEW POSSIBLE ACTIONS THAT CAN BE TAKEN BY THE BISHOP IN ITS NEW POSITION AFTER MOVEMENT
        """
        new_actionables = []
        
        NE_x, NE_y = ( new_coordinate[0] - 1, new_coordinate[1] + 1 )
        SE_x, SE_y = ( new_coordinate[0] + 1, new_coordinate[1] + 1 )
        SW_x, SW_y = ( new_coordinate[0] + 1, new_coordinate[1] - 1 )
        NW_x, NW_y = ( new_coordinate[0] - 1, new_coordinate[1] - 1 )
        
        while NE_x >= 0 and NE_y < board.get_width(): # Row decreasing, Col increasing
            # Check obstacles and other pieces
            if Piece.check_legality_others(board, (NE_x, NE_y)):
                new_actionables += [ (NE_x, NE_y) ]
                NE_x -= 1
                NE_y += 1
            else:
                break
        
        while SE_x < board.get_height() and SE_y < board.get_width(): # Row increasing, Col increasing
            # Check obstacles and other pieces
            if Piece.check_legality_others(board, (SE_x, SE_y)):
                new_actionables += [ (SE_x, SE_y) ]
                SE_x += 1
                SE_y += 1
            else:
                break
        
        while SW_x < board.get_height() and SW_y >= 0: # Row increasing, Col decreasing
            # Check obstacles and other pieces
            if Piece.check_legality_others(board, (SW_x, SW_y)):
                new_actionables += [ (SW_x, SW_y) ]
                SW_x += 1
                SW_y -= 1
            else:
                break
                
        while NW_x >= 0 and NW_y >= 0: # Row decreasing, Col decreasing
            # Check obstacles and other pieces
            if Piece.check_legality_others(board, (NW_x, NW_y)):
                new_actionables += [ (NW_x, NW_y) ]
                NW_x -= 1
                NW_y -= 1
            else:
                break
        return new_actionables
    
    @staticmethod    
    def Knight(board, new_coordinate):
        """
        RETURNS ALL NEW POSSIBLE ACTIONS THAT CAN BE TAKEN BY THE KNIGHT IN ITS NEW POSITION AFTER MOVEMENT
        """
        new_actionables = []
        
        # North First
        if (new_coordinate[0] - 2) >= 0:
            # Left
            if (new_coordinate[1] - 1) >= 0:
                if Piece.check_legality_others(board, (new_coordinate[0] - 2, new_coordinate[1] - 1)):
                    new_actionables += [ (new_coordinate[0] - 2, new_coordinate[1] - 1) ]
            # Right
            if (new_coordinate[1] + 1) < board.get_width():
                if Piece.check_legality_others(board, (new_coordinate[0] - 2, new_coordinate[1] + 1)):
                    new_actionables += [ (new_coordinate[0] - 2, new_coordinate[1] + 1) ]
                    
        # West First
        if (new_coordinate[1] + 2) < board.get_width():
            # Up
            if (new_coordinate[0] - 1) >= 0:
                if Piece.check_legality_others(board, (new_coordinate[0] - 1, new_coordinate[1] + 2)):
                    new_actionables += [ (new_coordinate[0] - 1, new_coordinate[1] + 2) ]
            # Down
            if (new_coordinate[0] + 1) < board.get_height():
                if Piece.check_legality_others(board, (new_coordinate[0] + 1, new_coordinate[1] + 2)):
                    new_actionables += [ (new_coordinate[0] + 1, new_coordinate[1] + 2) ]
        
        # South First
        if (new_coordinate[0] + 2) <= board.get_height():
            # Left
            if (new_coordinate[1] - 1) >= 0:
                if Piece.check_legality_others(board, (new_coordinate[0] + 2, new_coordinate[1] - 1)):
                    new_actionables += [ (new_coordinate[0] + 2, new_coordinate[1] - 1) ]
            # Right
            if (new_coordinate[1] + 1) < board.get_width():
                if Piece.check_legality_others(board, (new_coordinate[0] + 2, new_coordinate[1] + 1)):
                    new_actionables += [ (new_coordinate[0] + 2, new_coordinate[1] + 1) ]
        
        # East First
        if (new_coordinate[1] - 2) >= 0:
            # Up 
            if (new_coordinate[0] - 1) >= 0:
                if Piece.check_legality_others(board, (new_coordinate[0] - 1, new_coordinate[1] - 2)):
                    new_actionables += [ (new_coordinate[0] - 1, new_coordinate[1] - 2) ]
            # Down
            if (new_coordinate[0] + 1) < board.get_height():
                if Piece.check_legality_others(board, (new_coordinate[0] + 1, new_coordinate[1] - 2)):
                    new_actionables += [ (new_coordinate[0] + 1, new_coordinate[1] - 2) ]
        
        return new_actionables

    @staticmethod
    def Ferz(board, new_coordinate):
        """
        RETURNS ALL NEW POSSIBLE ACTIONS THAT CAN BE TAKEN BY THE FERZ IN ITS NEW POSITION AFTER MOVEMENT
        """
        new_actionables = []
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                new_x = new_coordinate[0] + i
                new_y = new_coordinate[1] + j
                if new_x < 0 or new_y < 0 or new_x >= board.get_height() or new_y >= board.get_width(): # Check if they are out of bounds
                    continue
                else:
                    new_actionables += [ (new_x , new_y) ]
        for action in new_actionables:
            if Piece.check_legality_others(board, (action[0], action[1])):
                continue
            else:
                new_actionables.remove(action)
        return new_actionables

    @staticmethod
    def Queen(board, new_coordinate):
        """
        RETURNS ALL NEW POSSIBLE ACTIONS THAT CAN BE TAKEN BY THE QUEEN IN ITS NEW POSITION AFTER MOVEMENT
        """
        new_actionables = Piece.Rook(board, new_coordinate) + Piece.Bishop(board, new_coordinate)
        return new_actionables

    @staticmethod 
    def Princess(board, new_coordinate):
        """
        RETURNS ALL NEW POSSIBLE ACTIONS THAT CAN BE TAKEN BY THE PRINCESS IN ITS NEW POSITION AFTER MOVEMENT
        """
        new_actionables = Piece.Bishop(board, new_coordinate) + Piece.Knight(board, new_coordinate)
        return new_actionables       
        
    @staticmethod
    def Empress(board, new_coordinate):
        """
        RETURNS ALL NEW POSSIBLE ACTIONS THAT CAN BE TAKEN BY THE EMPRESS IN ITS NEW POSITION AFTER MOVEMENT
        """
        new_actionables = Piece.Rook(board, new_coordinate) + Piece.Knight(board, new_coordinate)
        return new_actionables
    
    def move(self, board, new_coordinate, threatened={}):
        """
        MOVE THE PIECE TO THE NEW POSITION AND UPDATE ITS ACTIONABLES AND COORDINATES
        """
        if self.get_name() == "King":
            if self.get_tag() == 'enemy':
                threatened = {}
            self.set_actionables(Piece.King(board, new_coordinate, threatened))
        elif self.get_name() == "Queen":
            self.set_actionables(Piece.Queen(board, new_coordinate))
        elif self.get_name() == "Rook":
            self.set_actionables(Piece.Rook(board, new_coordinate))
        elif self.get_name() == "Bishop":
            self.set_actionables(Piece.Bishop(board, new_coordinate))
        elif self.get_name() == "Knight":
            self.set_actionables(Piece.Knight(board, new_coordinate))
        elif self.get_name() == "Ferz":
            self.set_actionables(Piece.Ferz(board, new_coordinate))
        elif self.get_name() == "Princess":
            self.set_actionables(Piece.Princess(board, new_coordinate))
        elif self.get_name() == "Empress":
            self.set_actionables(Piece.Empress(board, new_coordinate))
        else:
            pass
            #print(f'{self.get_name()} is not a valid Chess Piece')
        # Update Current grid 
        # board.update_grid(self, new_coordinate)
        # Update Piece new position 
        self.update_position(new_coordinate)

#############################################################################
######## Node
#############################################################################
class Node:

    def __init__(self, state, parent, path, path_cost, depth):
        self.state = state # Coordinate of current position
        self.parent = parent # Previous Node
        self.path = path # Actions Taken
        self.path_cost = path_cost # Total cost of actions taken
        self.depth = depth # Number of nodes transversed 
    
    def get_state(self):
        return self.state
    
    def get_parent(self):
        return self.parent
        
    def get_path(self):
        return self.path
        
    def get_path_cost(self):
        return self.path_cost
        
    def get_depth(self):
        return self.depth

#############################################################################
######## State
#############################################################################
class State:

    def __init__(self, rows, cols, grid, enemy_pieces, own_pieces, goals):
        self.board = Board(rows, cols, grid)
        self.enemies = [Piece(x[0], x[1], 'enemy') for x in enemy_pieces]
        self.allies = [Piece(y[0], y[1], 'ally') for y in own_pieces]
        self.goals = goals
        # Filled in the initialilzation below with the threatened coords as key, List of enemy Piece object as value
        self.threatened_squares = {}
        self.piece_in_play = None
        
        # Pre-process the initialize grid => Updating the grid with all the pieces position
        for piece in (self.enemies + self.allies):
            piece_row = piece.get_position()[0]
            piece_col = piece.get_position()[1]
            self.board.update_grid( piece, (piece_row, piece_col) )
        
        # Adding the actionables to the pieces starting with enemies follow by allies
        for piece in (self.enemies + self.allies):
            # since enemies are added in first, threatened_squares will be filled before ally king is filled
            piece.move(self.board, piece.get_position(), self.threatened_squares) 
            if piece.get_tag() == 'enemy': # Add enemy pieces actionables to threatened squares
                for threatened_coords in piece.get_actionables():
                    if threatened_coords not in self.threatened_squares.keys():
                        self.threatened_squares[threatened_coords] = []
                    self.threatened_squares[threatened_coords] += [piece]            

    def get_board(self):
        return self.board

    def get_enemies(self):
        return self.enemies

    def get_allies(self):
        return self.allies

    def get_goals(self):
        return self.goals

    def get_threatened_squares(self):
        return self.threatened_squares
    
    def get_piece_in_play(self):
        return self.piece_in_play
    
    def assignment_one(self):
        for piece in self.allies:
            if piece.get_name() == "King":
                self.piece_in_play = piece
                break

    def isGoalState(self, new_coordinate):
        for goal in self.goals:
            if new_coordinate == goal:
                return True
        return False
    
    def generateActions(self, new_coordinate):
        """
        GENERATE ALL LEGAL ACTIONS OF A PIECE AT A PARTICULAR COORDINATE GIVEN THE CURRENT GRID STATE
        FUNCTION DOES NOT UPDATE THE PIECE COORDINATE AND ACTIONABLES 
        """
        if self.get_piece_in_play() == None:
            # print("Currently no pieces are in play")
            return []
        else:
            curr_piece_name = self.get_piece_in_play().get_name()
        if curr_piece_name == "King":
            if self.get_piece_in_play().get_tag() == 'enemy':
                actionables = Piece.King(self.get_board(), new_coordinate)
            else:
                actionables = Piece.King(self.get_board(), new_coordinate, self.get_threatened_squares())
        elif curr_piece_name == "Queen":
            actionables = Piece.Queen(self.get_board(), new_coordinate)
        elif curr_piece_name == "Rook":
            actionables = Piece.Rook(self.get_board(), new_coordinate)
        elif curr_piece_name == "Bishop":
            actionables = Piece.Bishop(self.get_board(), new_coordinate)
        elif curr_piece_name == "Knight":
            actionables = Piece.Knight(self.get_board(), new_coordinate)
        elif curr_piece_name == "Ferz":
            actionables = Piece.Ferz(self.get_board(), new_coordinate)
        elif curr_piece_name == "Princess":
            actionables = Piece.Princess(self.get_board(), new_coordinate)
        elif curr_piece_name == "Empress":
            actionables = Piece.Empress(self.get_board(), new_coordinate)
        else:
            # print(f'{self.get_piece_in_play().get_name()} is not a valid Chess Piece')
            pass
        return actionables
        
#############################################################################
######## Implement Search Algorithm
#############################################################################
def search(rows, cols, grid, enemy_pieces, own_pieces, goals):
    Game_state = State(rows, cols, grid, enemy_pieces, own_pieces, goals)
    result = []
    frontier = deque() 
    explored = set()
    # Specifically to this problem, set the ally king as the piece in play
    Game_state.assignment_one()
    frontier.append( Node(Game_state.get_piece_in_play().get_position(), None, [], 0, 0) ) # Initialized position
    while len(frontier) > 0:
        current_node = frontier.popleft() # Remove the first node in the queue
        if current_node.get_state() in explored:
            continue
        else:
            explored.add( current_node.get_state() ) # Add visited nodes to explored 
        path = current_node.get_path() + [current_node.get_state()] # Update the path with the node explored
        if current_node.get_state() == Game_state.get_piece_in_play().get_position(): 
            # Starting position has no cost
            path_cost = current_node.get_path_cost()
        else:
            # Subsequent movement cost
            path_cost = current_node.get_path_cost() + Game_state.get_board().get_coordinate_value(current_node.get_state()[0], current_node.get_state()[1])
        depth = current_node.get_depth() + 1
        if Game_state.isGoalState(current_node.get_state()):
            for step in range(1, len(path)):
                result += [ [(chr(97 + path[step-1][1]), path[step-1][0]),  (chr(97 + path[step][1]), path[step][0])] ] # converting to letters representation
            return result
        else:
            for action in Game_state.generateActions(current_node.get_state()):
                if action in explored:
                    continue
                else:
                    # Early Goal Test can be added here
                    frontier.append(
                        Node(action, current_node, path, path_cost, depth)
                    )
    return result

#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# Return number of rows, cols, grid containing obstacles and step costs of coordinates, enemy pieces, own piece, and goal positions
def parse(testcase):
    handle = open(testcase, "r")

    get_par = lambda x: x.split(":")[1]
    rows = int(get_par(handle.readline())) # Integer
    cols = int(get_par(handle.readline())) # Integer
    grid = [[1 for j in range(cols)] for i in range(rows)] # Dictionary, label empty spaces as 1 (Default Step Cost)
    enemy_pieces = [] # List
    own_pieces = [] # List
    goals = [] # List

    handle.readline()  # Ignore number of obstacles
    for ch_coord in get_par(handle.readline()).split():  # Init obstacles
        r, c = from_chess_coord(ch_coord)
        grid[r][c] = -1 # Label Obstacle as -1

    handle.readline()  # Ignore Step Cost header
    line = handle.readline()
    while line.startswith("["):
        line = line[1:-2].split(",")
        r, c = from_chess_coord(line[0])
        grid[r][c] = int(line[1]) if grid[r][c] == 1 else grid[r][c] #Reinitialize step cost for coordinates with different costs
        line = handle.readline()
    
    line = handle.readline() # Read Enemy Position
    while line.startswith("["):
        line = line[1:-2]
        piece = add_piece(line)
        enemy_pieces.append(piece)
        line = handle.readline()

    # Read Own King Position
    line = handle.readline()[1:-2]
    piece = add_piece(line)
    own_pieces.append(piece)

    # Read Goal Positions
    for ch_coord in get_par(handle.readline()).split():
        r, c = from_chess_coord(ch_coord)
        goals.append((r, c))
    
    return rows, cols, grid, enemy_pieces, own_pieces, goals

def add_piece( comma_seperated) -> Piece:
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [piece, (r,c)]

def from_chess_coord( ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)

#############################################################################
######## Main function to be called
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# To return: List of moves
# Return Format Example: [[('a', 0), ('a', 1)], [('a', 1), ('c', 3)], [('c', 3), ('d', 5)]]
def run_BFS():    
    testcase = sys.argv[1]
    rows, cols, grid, enemy_pieces, own_pieces, goals = parse(testcase)
    moves = search(rows, cols, grid, enemy_pieces, own_pieces, goals)
    return moves
    