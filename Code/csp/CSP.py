import sys

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
        
    def print_grid(self):
        print("/\t", end = "")
        for k in range(97, 97 + self.get_width()): # Print col index
            print(chr(k) + "\t", end = "")
        print("\n")
        for i in range(self.get_height()):
            print(str(i) + "\t", end = "") # Print row index
            for j in range(self.get_width()):
               print(str(self.get_grid()[i][j]) + "\t", end = "")
            print("\n")
            
    def update_grid(self, piece, new_coordinate):
        self.set_coordinate(new_coordinate[0], new_coordinate[1], self.piece_dict[piece.get_name()])
        
#############################################################################
######## Piece
#############################################################################
class Piece:

    def __init__(self, name, coordinate=None):
        self.name = name
        self.coordinate = coordinate # Not required in this assignment
        self.actionables = [] # Not required in this assignment
    
    def get_name(self):
        return self.name
    
    def get_position(self):
        return self.coordinate
        
    def get_actionables(self):
        return self.actionables
    
    def update_position(self, new_coordinates):
        self.coordinate = new_coordinates
    
    def set_actionables(self, new_actionables):
        self.actionables = new_actionables
    
    @staticmethod
    def check_legality(board, coordinate):
        """
        RETURNS TRUE IF MOVEMENT TO THE POSITION IS LEGAL -> NO OBSTACLES, NOT OCCUPIED BY OTHER PIECES
        """
        flag = False
        if board.get_coordinate_value(coordinate[0], coordinate[1]) != -1 and type(board.get_coordinate_value(coordinate[0], coordinate[1])) != str:
            flag = True
        return flag

    @staticmethod
    def King(board, new_coordinate):
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
            if Piece.check_legality(board, action): # If available, do not remove
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
            if Piece.check_legality(board, (North_x, new_coordinate[1])):
                new_actionables += [ (North_x, new_coordinate[1]) ]
                North_x -= 1
            else:
                break
        while East_y < board.get_width(): # Col increasing
            # Check obstacles and other pieces
            if Piece.check_legality(board, (new_coordinate[0], East_y)):
                new_actionables += [ (new_coordinate[0], East_y) ]
                East_y += 1
            else:
                break
        while South_x < board.get_height(): # Row increasing
            # Check obstacles and other pieces
            if Piece.check_legality(board, (South_x, new_coordinate[1])):
                new_actionables += [ (South_x, new_coordinate[1]) ]
                South_x += 1
            else:
                break
        while West_y >= 0: # Col decreasing
            # Check obstacles and other pieces
            if Piece.check_legality(board, (new_coordinate[0], West_y)):
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
            if Piece.check_legality(board, (NE_x, NE_y)):
                new_actionables += [ (NE_x, NE_y) ]
                NE_x -= 1
                NE_y += 1
            else:
                break
        
        while SE_x < board.get_height() and SE_y < board.get_width(): # Row increasing, Col increasing
            # Check obstacles and other pieces
            if Piece.check_legality(board, (SE_x, SE_y)):
                new_actionables += [ (SE_x, SE_y) ]
                SE_x += 1
                SE_y += 1
            else:
                break
        
        while SW_x < board.get_height() and SW_y >= 0: # Row increasing, Col decreasing
            # Check obstacles and other pieces
            if Piece.check_legality(board, (SW_x, SW_y)):
                new_actionables += [ (SW_x, SW_y) ]
                SW_x += 1
                SW_y -= 1
            else:
                break
                
        while NW_x >= 0 and NW_y >= 0: # Row decreasing, Col decreasing
            # Check obstacles and other pieces
            if Piece.check_legality(board, (NW_x, NW_y)):
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
                if Piece.check_legality(board, (new_coordinate[0] - 2, new_coordinate[1] - 1)):
                    new_actionables += [ (new_coordinate[0] - 2, new_coordinate[1] - 1) ]
            # Right
            if (new_coordinate[1] + 1) < board.get_width():
                if Piece.check_legality(board, (new_coordinate[0] - 2, new_coordinate[1] + 1)):
                    new_actionables += [ (new_coordinate[0] - 2, new_coordinate[1] + 1) ]
                    
        # West First
        if (new_coordinate[1] + 2) < board.get_width():
            # Up
            if (new_coordinate[0] - 1) >= 0:
                if Piece.check_legality(board, (new_coordinate[0] - 1, new_coordinate[1] + 2)):
                    new_actionables += [ (new_coordinate[0] - 1, new_coordinate[1] + 2) ]
            # Down
            if (new_coordinate[0] + 1) < board.get_height():
                if Piece.check_legality(board, (new_coordinate[0] + 1, new_coordinate[1] + 2)):
                    new_actionables += [ (new_coordinate[0] + 1, new_coordinate[1] + 2) ]
        
        # South First
        if (new_coordinate[0] + 2) < board.get_height():
            # Left
            if (new_coordinate[1] - 1) >= 0:
                if Piece.check_legality(board, (new_coordinate[0] + 2, new_coordinate[1] - 1)):
                    new_actionables += [ (new_coordinate[0] + 2, new_coordinate[1] - 1) ]
            # Right
            if (new_coordinate[1] + 1) < board.get_width():
                if Piece.check_legality(board, (new_coordinate[0] + 2, new_coordinate[1] + 1)):
                    new_actionables += [ (new_coordinate[0] + 2, new_coordinate[1] + 1) ]
        
        # East First
        if (new_coordinate[1] - 2) >= 0:
            # Up 
            if (new_coordinate[0] - 1) >= 0:
                if Piece.check_legality(board, (new_coordinate[0] - 1, new_coordinate[1] - 2)):
                    new_actionables += [ (new_coordinate[0] - 1, new_coordinate[1] - 2) ]
            # Down
            if (new_coordinate[0] + 1) < board.get_height():
                if Piece.check_legality(board, (new_coordinate[0] + 1, new_coordinate[1] - 2)):
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
            if Piece.check_legality(board, (action[0], action[1])):
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
    
    def move(self, board, new_coordinate):
        """
        MOVE THE PIECE TO THE NEW POSITION AND UPDATE ITS ACTIONABLES AND COORDINATES
        """
        if self.get_name() == "King":
            self.set_actionables(Piece.King(board, new_coordinate))
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
        # Update Current grid 
        board.update_grid(self, new_coordinate)
        # Update Piece new position 
        self.update_position(new_coordinate)

#############################################################################
######## Node
#############################################################################
class Node:

    def __init__(self, unassigned, assigned, available):
        self.unassigned = unassigned
        self.assigned = assigned
        self.available = available
  
    def get_unassigned(self):
        return self.unassigned

    def get_assigned(self):
        return self.assigned

    def get_available(self):
        return self.available

#############################################################################
######## State
#############################################################################
class State:

    def __init__(self, rows, cols, grid, num_pieces):
        self.board = Board(rows, cols, grid)
        self.unassigned_pieces = {} # Dictionary containing "Piece" (key) : "Quantity" (Value)
        self.available_coordinates = {} # Dictionary containing "Piece" (key) : "set{all available coords}" (value)
        self.pieces_assigned = {} # Dictionary containing "Location" (key) : "Piece" (value)
        self.attack_table = {} # Remember positions to attack to remove from a location

        piece_type = ["King", "Queen", "Bishop", "Rook", "Knight", "Ferz", "Princess", "Empress"]
        # Capture all the pieces to assign
        for i in range(len(num_pieces)):
            if num_pieces[i]>0:
                self.unassigned_pieces[piece_type[i]] = num_pieces[i]
        # Create Attack_table keys
        for piece_type in self.unassigned_pieces.keys():
            self.attack_table[piece_type] = {}

        available_general = set() # Store all available coordinates on the board
        # Generate all available coordinates
        for row in range(self.board.get_height()):
            for col in range(self.board.get_width()):
                if self.board.get_coordinate_value(row, col) != -1:
                    available_general.add((row, col))
        # Deepcopy of all available coordinates for each type of piece
        for piece_type in self.unassigned_pieces.keys():
            self.available_coordinates[piece_type] = available_general.copy()
        
    def get_board(self):
        return self.board

    def get_unassigned_pieces(self):
        return self.unassigned_pieces

    def get_available_coordinates(self):
        return self.available_coordinates

    def get_attack_table(self):
        return self.attack_table

    def get_pieces_assigned(self):
        return self.pieces_assigned

    @staticmethod
    def choose_unassigned_pieces(node):
        mrvh = 1000000 # Most restricted variable heuristic
        piece_to_use = []  
        for piece, coords_available in node.get_available().items():
            if len(coords_available) <= mrvh:
                if len(coords_available) < mrvh:
                    piece_to_use = []
                    mrvh = len(coords_available)
                piece_to_use += [piece]
        if len(piece_to_use) > 1: # Degree Tie-Breaking
            if "Queen" in piece_to_use:
                selection = "Queen"
            elif "Princess" in piece_to_use:
                selection = "Princess"
            elif "Bishop" in piece_to_use:
                selection = "Bishop"
            elif "Empress" in piece_to_use:
                selection = "Empress"
            elif "Rook" in piece_to_use:
                selection = "Rook"
            elif "Knight" in piece_to_use:
                selection = "Knight"
            elif "King" in piece_to_use:
                selection = "King"
            else:
                selection = "Ferz"
        else:
            selection = piece_to_use[0]
        return selection

    def generateActions(self, curr_piece_name, new_coordinate):
        """
        GENERATE ALL LEGAL ACTIONS OF A PIECE AT A PARTICULAR COORDINATE GIVEN THE CURRENT GRID STATE
        FUNCTION DOES NOT UPDATE THE PIECE COORDINATE AND ACTIONABLES 
        """
        if new_coordinate in self.get_attack_table()[curr_piece_name].keys():
            return self.get_attack_table()[curr_piece_name][new_coordinate]
        else:
            if curr_piece_name == "King":
                actionables = Piece.King(self.get_board(), new_coordinate)
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
            self.get_attack_table()[curr_piece_name][new_coordinate] = set(actionables)
        return self.get_attack_table()[curr_piece_name][new_coordinate]

#############################################################################
######## Implement Search Algorithm
#############################################################################
def backtrack(state, curr_node):
    if curr_node.get_unassigned() == {}: # Completed Assignment, return the final outcome
        return curr_node
    else:
        next_piece = Piece(State.choose_unassigned_pieces(curr_node))
        coord_copy = list(curr_node.get_available()[next_piece.get_name()])
        for coord in coord_copy:
            assigned_copy = curr_node.get_assigned().copy()
            unassigned_copy = curr_node.get_unassigned().copy()
            available_copy = {} # Cannot directly copy available as the set objects cause an issue
            attack_coords = state.generateActions(next_piece.get_name(), coord)
            for piece_type, possible_coords in curr_node.get_available().items():
                filtered_coords = set()
                for x in possible_coords:
                    if x in attack_coords or x == coord:
                        continue
                    elif coord in state.generateActions(piece_type, x):
                        continue
                    else:
                        filtered_coords.add(x)
                available_copy[piece_type] = filtered_coords
            assigned_copy[coord] = next_piece
            unassigned_copy[next_piece.get_name()] -= 1
            if unassigned_copy[next_piece.get_name()] == 0:
                del(unassigned_copy[next_piece.get_name()])
                del(available_copy[next_piece.get_name()])
            
            # Create the new_node after the update
            new_node = Node(unassigned_copy, assigned_copy, available_copy)
            flag = True
            # Forward Checking
            for remaining_piece_type in new_node.get_unassigned().keys(): # Unary Consistent
                if new_node.get_unassigned()[remaining_piece_type] > len(new_node.get_available()[remaining_piece_type]): # Not enuff space to put
                    flag = False
                    break
                for other_piece_type in new_node.get_unassigned().keys(): # Binary Consistent
                    if other_piece_type != remaining_piece_type:
                        if sum([new_node.get_unassigned()[remaining_piece_type], new_node.get_unassigned()[other_piece_type]]) > len((new_node.get_available()[remaining_piece_type]).union(new_node.get_available()[other_piece_type])):
                            flag = False
                            break
                if flag == False:
                    break  
            if flag:
                next_cycle = backtrack(state, new_node) # Recurse onwards since solution still exists
                if next_cycle is not None:
                    return next_cycle

def search(rows, cols, grid, num_pieces):
    state = State(rows, cols, grid, num_pieces)
    start_node = Node(state.get_unassigned_pieces().copy(), state.get_pieces_assigned().copy(), state.get_available_coordinates().copy())
    result_node = backtrack(state, start_node)
    result = {}
    for position, piece in result_node.get_assigned().items():
        result[(chr(97 + position[1]), position[0])] = piece.get_name()
    return result


#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
def parse(testcase):
    handle = open(testcase, "r")

    get_par = lambda x: x.split(":")[1]
    rows = int(get_par(handle.readline()))
    cols = int(get_par(handle.readline()))
    grid = [[0 for j in range(cols)] for i in range(rows)]

    num_obstacles = int(get_par(handle.readline()))
    if num_obstacles > 0:
        for ch_coord in get_par(handle.readline()).split():  # Init obstacles
            r, c = from_chess_coord(ch_coord)
            grid[r][c] = -1
    else:
        handle.readline()
    
    piece_nums = get_par(handle.readline()).split()
    num_pieces = [int(x) for x in piece_nums] #List in the order of King, Queen, Bishop, Rook, Knight

    return rows, cols, grid, num_pieces

def add_piece( comma_seperated):
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [(r,c), piece]

#Returns row and col index in integers respectively
def from_chess_coord( ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)

### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# To return: Goal State which is a dictionary containing a mapping of the position of the grid to the chess piece type.
# Chess Pieces (String): King, Queen, Knight, Bishop, Rook (First letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Goal State to return example: {('a', 0) : Queen, ('d', 10) : Knight, ('g', 25) : Rook}
def run_CSP():
    testcase = sys.argv[1] #Do not remove. This is your input testfile.
    rows, cols, grid, num_pieces = parse(testcase)
    goalstate = search(rows, cols, grid, num_pieces)
    return goalstate #Format to be returned
