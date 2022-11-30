import sys
import random

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
        #print(f'Coordinate ({row}, {col}) is set to {new_value}')
    
    
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

    def __init__(self, name, coordinate):
        self.name = name
        self.coordinate = coordinate
        self.actionables = []
    
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
        # board.update_grid(self, new_coordinate)
        # Update Piece new position 
        # self.update_position(new_coordinate)

#############################################################################
######## Node
#############################################################################
class Node:

    def __init__(self, state, value, threatened):
        self.state = state # Pieces left
        self.length = len(state) # Number of Pieces left
        self.value = value # Current number of coordinates threatened by more than 1 square
        self.threatened = threatened

    def get_state(self):
        return self.state
    
    def get_value(self):
        return self.value
    
    def get_length(self):
        return self.length
    
    def get_threatened(self):
        return self.threatened

#############################################################################
######## State
#############################################################################
class State:

    def __init__(self, rows, cols, grid, pieces, limit):
        self.board = Board(rows, cols, grid)
        self.pieces = [Piece(v, k) for k, v in pieces.items()]
        self.limit = int(limit)
        self.threatened = {}
        self.initial_value = 0
        
        # Fill in the board
        for piece in (self.pieces):
            piece_row = piece.get_position()[0]
            piece_col = piece.get_position()[1]
            self.board.update_grid( piece, (piece_row, piece_col) )
        # Need to account for obstacles separately
        mock_board = []
        for r in self.board.get_grid():
            curr_row = []
            for c in r:
                if type(c) == str:
                    curr_row += [0]
                else:
                    curr_row += [c]
            mock_board += [curr_row]
        self.mock_board = Board(rows, cols, mock_board)
        # Update the self.threatened with their moves
        for piece in self.pieces:
            piece.move(self.mock_board, piece.get_position())
            for action in piece.get_actionables():
                if action not in self.threatened.keys():
                    self.threatened[action] = []
                self.threatened[action] += [piece]
                self.initial_value += 1
        
    def get_board(self):
        return self.board

    def get_mock_board(self):
        return self.mock_board

    def get_pieces(self):
        return self.pieces

    def get_threatened(self):
        return self.threatened

    def get_limit(self):
        return self.limit

    def get_value(self):
        return self.initial_value
    
    @staticmethod
    def remove_piece(threatened, piece):
        if piece.get_position() in threatened.keys():
            for other in threatened[piece.get_position()]:
                other.get_actionables().remove(piece.get_position())
            del(threatened[piece.get_position()]) # Remove the piece coord because nothing is being threatened anymore
        for action in piece.get_actionables():
            threatened[action].remove(piece)
            if threatened[action] == []:
                del(threatened[action])
        return threatened

    @staticmethod 
    def value(threatened, piece, curr_value): # Number of cells with more than 1 piece threatening
        counter = curr_value - len(piece.get_actionables())
        if piece.get_position() in threatened.keys():
            counter -= len(threatened[piece.get_position()])
        return counter

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
        return actionables

#############################################################################
######## Implement Search Algorithm
#############################################################################
def search(rows, cols, grid, pieces, k):
    for i in range(300):
        random.seed(i*i)
        initialized_state = State(rows, cols, grid, pieces, k)

        # Random Restart
        random_first_piece = initialized_state.get_pieces()[random.randint(0, len(initialized_state.get_pieces())-1)]
        random_first_value = State.value(initialized_state.get_threatened(), random_first_piece, initialized_state.get_value())
        random_first_threatened = State.remove_piece(initialized_state.get_threatened(), random_first_piece)
        initialized_state.get_pieces().remove(random_first_piece)
        random_remaining_pieces = initialized_state.get_pieces()
        curr_node = Node(random_remaining_pieces, random_first_value, random_first_threatened)

        while (curr_node.get_length() > initialized_state.get_limit()):
            curr_node_move_list = []
            curr_best_value = curr_node.get_value()
            for piece in curr_node.get_state():
                value = State.value(curr_node.get_threatened(), piece, curr_node.get_value())
                if value == 0: # Goal Obtained
                    curr_node.get_state().remove(piece)
                    final_pieces = curr_node.get_state()
                    result = {}
                    for final_piece in final_pieces:
                        position = final_piece.get_position()
                        result[(chr(97 + position[1]), position[0])] = final_piece.get_name()
                    return result
                elif value <= curr_best_value: # Consider Plateaus
                    if value < curr_best_value: # If strictly less, remove all other options
                        curr_node_move_list = []
                        curr_best_value = value # Change value
                    curr_node_move_list += [(piece, value)] # Else add on to the possible moves to be considered
                else:
                    continue
            if curr_node_move_list == []: # No possible moves, stuck -> Restart
                break
            else:
                move_made = curr_node_move_list[random.randint(0, len(curr_node_move_list)-1)] # Choose a random move from list
                new_value = move_made[1]
                new_threatened = State.remove_piece(curr_node.get_threatened(), move_made[0])
                curr_node.get_state().remove(move_made[0])
                remaining_pieces = curr_node.get_state()
                curr_node = Node(remaining_pieces, new_value, new_threatened)
    return {}

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
    k = 0
    pieces = {}

    num_obstacles = int(get_par(handle.readline()))
    if num_obstacles > 0:
        for ch_coord in get_par(handle.readline()).split():  # Init obstacles
            r, c = from_chess_coord(ch_coord)
            grid[r][c] = -1
    else:
        handle.readline()
    
    k = handle.readline().split(":")[1].strip() # Read in value of k

    piece_nums = get_par(handle.readline()).split()
    num_pieces = 0
    for num in piece_nums:
        num_pieces += int(num)

    handle.readline()  # Ignore header
    for i in range(num_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        pieces[coords] = piece    

    return rows, cols, grid, pieces, k

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
def run_local():
    testcase = sys.argv[1] #Do not remove. This is your input testfile.
    rows, cols, grid, pieces, k = parse(testcase)
    goalstate = search(rows, cols, grid, pieces, k)
    return goalstate #Format to be returned
