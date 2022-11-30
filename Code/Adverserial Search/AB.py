from math import inf
import sys

### IMPORTANT: Remove any print() functions or rename any print functions/variables/string when submitting on CodePost
### The autograder will not run if it detects any print function.

# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
######## Piece
#############################################################################

# Bonus material value given to pieces when they occupy a certain square at a point in the game
# Each phase of game includes bonus material value as well for the type of pieces 
# -> I.E: Bishop has some bonus points in the early game, Rook has more bonus points in the late game.
# VALUES DEFINED ARE FOR WHITE PIECES, FOR BLACK PIECES FLIPPED ALL THE VALUES BEFORE USING

# PIECE_TABLE_STRATEGY
piecesPositionValueTable = {
    "King": {
        "Opening":[ [20, 30, 20, 10, 20, 30, 20],  # Rook side weaker early game due to new pieces
                    [-20, -20, -10, -10, -10, -20, -20],
                    [-30, -30, -30, -30, -30, -30, -30],
                    [-40, -40, -40, -40, -40, -40, -40],
                    [-50, -50, -50, -50, -50, -50, -50],
                    [-50, -50, -50, -50, -50, -50, -50],
                    [-50, -50, -50, -50, -50, -50, -50]
                ],
        "Middle":[ [20, 30, 20, 10, 20, 30, 20],  # Rook side weaker early game due to new pieces
                    [-20, -20, -10, -10, -10, -20, -20],
                    [-30, -30, -30, -30, -30, -30, -30],
                    [-40, -40, -40, -40, -40, -40, -40],
                    [-50, -50, -50, -50, -50, -50, -50],
                    [-50, -50, -50, -50, -50, -50, -50],
                    [-50, -50, -50, -50, -50, -50, -50]
                ],
        "End": [    [-20, -10, 0, 0, 0, -10, -20],
                    [-20, -10, 0, 10, 0, -10, -20],
                    [-20, -20, -20, 20, -20, -20, -20],
                    [-20, -20, -20, -20, -20, -20, -20],
                    [-20, -20, -20, -20, -20, -20, -20],
                    [-30, -20, -20, -30, -20, -20, -30],
                    [-40, -30, -30, -30, -30, -30, -40]
            ]
    },
    "Queen": {
        "Opening":[ [-40, -30, -20, -20, -20, -30, -40], 
                    [-30, 10, 10, 10, 10, 10, -30],
                    [-20, 20, 30, 30, 30, 20, -20],
                    [-10, 0, 10, 10, 10, 0, -10],
                    [-20, -10, -10, -10, -10, -10, -20],
                    [-30, -20, -20, -20, -20, -20, -30],
                    [-40, -20, -20, -20, -20, -20, -40]
                ],
        "Middle":[  [-40, -30, -20, -20, -20, -30, -40],
                    [-30, 10, 10, 10, 10, 10, -30],
                    [-20, 20, 20, 40, 20, 20, -20],
                    [-10, 10, 10, 20, 10, 10, -10],
                    [-10, -10, -10, -10, -10, -10, -10],
                    [-30, -10, -10, -10, -10, -10, -30],
                    [-40, -30, -20, -20, -20, -30, -40]
                ],
        "End": [    [-40, -30, -20, -20, -20, -30, -40],
                    [-30, 10, 10, 10, 10, 10, -30],
                    [-20, 10, 30, 30, 30, 10, -20],
                    [-10, 10, 30, 60, 30, 10, -10],
                    [-10, 10, 30, 30, 30, 10, -10],
                    [-30, 10, 10, 10, 10, 10, -30],
                    [-40, -30, -20, -20, -20, -30, -40]
                ]
    },
    "Bishop": {
        "Opening":[ [-30, -20, -20, -20, -20, -20, -30],
                    [-20, 10, 0, 0, 0, 10, -20],
                    [-20, 20, 20, 20, 20, 20, -20],
                    [-20, 10, 10, 10, 10, 10, -20],
                    [-20, -10, 0, 0, 0, -10, -20],
                    [-20, -10, -10, -10, -10, -10, -20],
                    [-30, -20, -20, -20, -20, -20, -30]
                ],
        "Middle":[  [-30, -20, -20, -20, -20, -20, -30],
                    [-20, 0, -10, -10, -10, 0, -20],
                    [-20, 10, 10, 10, 10, 10, -20],
                    [-20, -10, 0, 0, 0, -10, -20],
                    [-20, -10, 0, 0, 0, -10, -20],
                    [-20, -10, 0, 0, 0, -10, -20],
                    [-30, -20, -20, -20, -20, -20, -30]
                ],
        "End": [    [-30, -20, -20, -20, -20, -20, -30],
                    [-20, 0, -10, -10, -10, 0, -20],
                    [-20, 10, 10, 10, 10, 10, -20],
                    [-20, 0, 20, 20, 20, 0, -20],
                    [-20, 0, 20, 20, 20, 0, -20],
                    [-20, 0, 20, 20, 20, 0, -20],
                    [-30, -20, -20, -20, -20, -20, -30]
                ]
    },
    "Knight": {
        "Opening":[ [-50, -40, -30, -20, -30, -40, -50],
                    [-40, -20, 0, 0, 0, -20, -40],
                    [-30, 20, 20, 20, 20, 20, -30],
                    [-30, 10, 20, 20, 20, 10, -30],
                    [-30, 0, 0, 0, 0, 0, -30],
                    [-40, -20, 0, 0, 0, -20, -40],
                    [-50, -40, -30, -20, -30, -40, -50]
                ],
        "Middle":[  [-50, -40, -30, -20, -30, -40, -50],
                    [-40, -20, 0, 0, 0, -20, -40],
                    [-30, 10, 10, 20, 10, 10, -30],
                    [-30, 0, 20, 30, 20, 0, -30],
                    [-30, 10, 10, 20, 10, 10, -30],
                    [-40, -20, 0, 0, 0, -20, -40],
                    [-50, -40, -30, -20, -30, -40, -50]
                ],
        "End": [    [-50, -40, -30, -20, -30, -40, -50],
                    [-40, -20, 0, 0, 0, -20, -40],
                    [-30, 10, 10, 20, 10, 10, -30],
                    [-30, 0, 20, 40, 20, 0, -30],
                    [-30, 10, 10, 20, 10, 10, -30],
                    [-40, -20, 0, 0, 0, -20, -40],
                    [-50, -40, -30, -20, -30, -40, -50]
                ]
    },
    "Rook": {
        "Opening":[ [0, 0, 0, 10, 0, 0, 0],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [0, 10, 10, 10, 10, 10, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "Middle":[  [0, 0, 0, 10, 0, 0, 0],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [10, 20, 20, 20, 20, 20, 10],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "End": [    [0, 0, 0, 10, 0, 0, 0],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [10, 30, 30, 30, 30, 30, 10],
                    [0, 0, 0, 0, 0, 0, 0]   
                ]
    },
    "Pawn": {
        "Opening":[ [0, 0, 0, 0, 0, 0, 0],
                    [0, 20, 20, 20, 20, 20, 0], # Allow queen/bishop movements, king protecting pawns to stay put
                    [-20, 10, 10, 10, 10, 10, -20],
                    [-10, -30, -30, -30, -30, -30, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-50, -50, -50, -50, -50, -50, -50]
                ],
        "Middle":[  [0, 0, 0, 0, 0, 0, 0],
                    [0, 20, 20, 20, 20, 20, 0],
                    [-10, 10, 10, -20, 10, 10, -20],
                    [-10, 10, 10, 10, 10, 10, -10],
                    [-10, -30, -30, -30, -30, -30, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-50, -50, -50, -50, -50, -50, -50]
                ],
        "End": [    [0, 0, 0, 0, 0, 0, 0],
                    [0, 10, 10, 10, 10, 10, 0],
                    [-10, 30, 30, 30, 30, 30, -20],
                    [-10, 10, 10, 10, 10, 10, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-10, -10, -10, -10, -10, -10, -10],
                    [-50, -50, -50, -50, -50, -50, -50]
                ]
    },
    "Ferz": {
        "Opening":[ [-30, -10, -10, -10, -10, -10, -30],
                    [-10, 10, 10, 10, 10, 10, -10],
                    [-10, 20, 20, 20, 20, 20, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-10, -20, -20, -20, -20, -20, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-30, 0, 0, 0, 0, 0, -30]
                ],
        "Middle":[  [-30, -10, -10, -10, -10, -10, -30],
                    [-10, 10, 10, 10, 10, 10, -10],
                    [-10, 20, 20, 20, 20, 20, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-10, -20, -20, -20, -20, -20, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-30, 0, 0, 0, 0, 0, -30]
                ],
        "End": [    [-30, -10, -10, -10, -10, -10, -30],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-10, 0, 10, 10, 10, 0, -10],
                    [-10, 0, 10, 20, 10, 0, -10],
                    [-10, 0, 10, 10, 10, 0, -10],
                    [-10, 0, 0, 0, 0, 0, -10],
                    [-30, 0, 0, 0, 0, 0, -30]
                ]
    },
    "Empress": {
        "Opening":[[-50, -40, -30, -10, -30, -40, -50], 
                    [-50, -20, 0, 0, 0, -20, -50], 
                    [-40, 10, 10, 10, 10, 10, -40], 
                    [-40, 0, 10, 10, 10, 0, -40], 
                    [-40, -10, -10, -10, -10, -10, -40], 
                    [-30, 0, 0, 0, 0, 0, -30], 
                    [-50, -40, -30, -20, -30, -40, -50]
                ],

        "Middle":[[-50, -40, -30, -10, -30, -40, -50], 
                [-50, -20, 0, 0, 0, -20, -50], 
                [-40, 10, 10, 20, 10, 10, -40], 
                [-40, 0, 20, 30, 20, 0, -40], 
                [-40, 10, 10, 20, 10, 10, -40], 
                [-30, 10, 30, 30, 30, 10, -30], 
                [-50, -40, -30, -20, -30, -40, -50]
            ],

        "End": [[-50, -40, -30, -10, -30, -40, -50], 
                [-50, -20, 0, 0, 0, -20, -50], 
                [-40, 10, 10, 20, 10, 10, -40], 
                [-40, 0, 20, 40, 20, 0, -40], 
                [-40, 10, 10, 20, 10, 10, -40], 
                [-30, 10, 30, 30, 30, 10, -30], 
                [-50, -40, -30, -20, -30, -40, -50]
            ]
    },
    "Princess": {
        "Opening":[[-80, -60, -50, -40, -50, -60, -80], 
                    [-60, -10, 0, 0, 0, -10, -60], 
                    [-50, 40, 40, 40, 40, 40, -50], 
                    [-50, 20, 30, 30, 30, 20, -50], 
                    [-50, -10, 0, 0, 0, -10, -50], 
                    [-60, -30, -10, -10, -10, -30, -60], 
                    [-80, -60, -50, -40, -50, -60, -80]
            ],
        "Middle":[[-80, -60, -50, -40, -50, -60, -80], 
                    [-60, -20, -10, -10, -10, -20, -60], 
                    [-50, 30, 30, 40, 30, 30, -50], 
                    [-50, 0, 30, 40, 30, 0, -50], 
                    [-50, 10, 20, 30, 20, 10, -50], 
                    [-60, -20, 10, 10, 10, -20, -60], 
                    [-80, -60, -50, -40, -50, -60, -80]
            ],
        "End": [[-80, -60, -50, -40, -50, -60, -80], 
                [-60, -20, -10, -10, -10, -20, -60], 
                [-50, 30, 30, 40, 30, 30, -50], 
                [-50, 0, 50, 70, 50, 0, -50], 
                [-50, 10, 40, 50, 40, 10, -50], 
                [-60, -20, 30, 30, 30, -20, -60], 
                [-80, -60, -50, -40, -50, -60, -80]
            ]

    }
}

# SETUP BOARD
initialChessBoard = {

    ("d", 6): ('King', 'Black'), 
    ("c", 6): ('Queen', 'Black'), 
    ("b", 6): ('Bishop', 'Black'), 
    ("a", 6): ('Knight', 'Black'), 
    ("g", 6): ('Rook', 'Black'), 
    ("e", 6): ('Princess', 'Black'), 
    ("f", 6): ('Empress', 'Black'), 
    ("b", 5): ('Pawn', 'Black'), 
    ("c", 5): ('Pawn', 'Black'), 
    ("d", 5): ('Pawn', 'Black'), 
    ("e", 5): ('Pawn', 'Black'), 
    ("f", 5): ('Pawn', 'Black'), 
    ("a", 5): ('Ferz', 'Black'), 
    ("g", 5): ('Ferz', 'Black'), 
    ("d", 0):('King', 'White'), 
    ("c", 0): ('Queen', 'White'), 
    ("b", 0): ('Bishop', 'White'), 
    ("a", 0): ('Knight', 'White'), 
    ("g", 0): ('Rook', 'White'), 
    ("e", 0): ('Princess', 'White'), 
    ("f", 0): ('Empress', 'White'), 
    ("b", 1): ('Pawn', 'White'), 
    ("c", 1): ('Pawn', 'White'), 
    ("d", 1): ('Pawn', 'White'), 
    ("e", 1): ('Pawn', 'White'), 
    ("f", 1): ('Pawn', 'White'), 
    ("a", 1): ('Ferz', 'White'), 
    ("g", 1): ('Ferz', 'White')
}

# KING_SAFETY_STRATEGY (ATTACKING KING ZONE)
attackWeights = {
    0:0,
    1:0,
    2:50,
    3:75,
    4:88,
    5:94,
    6:97,
    7:99,
    8:110,
    9:130,
    10:150,
    11:200,
    12:300
}
threatValues = {
    "King": 30,
    "Queen": 120, # Rook Bishop
    "Bishop": 40,
    "Knight": 30,
    "Rook": 60,
    "Pawn": 10,
    "Ferz": 20,
    "Empress": 100, # Rook Knight
    "Princess": 80 # Bishop Knight
}

class Piece:
    
    def __init__(self, name, coordinate, tag):
        self.name = name
        self.coordinate = coordinate
        self.tag = tag
        self.material_value = 0
    
        # According to AlphaZero Valuations, Initialized value without considering position and game state
        if name == "King":
            self.material_value = 888888
        elif name == "Queen": # Rook Bishop
            self.material_value = 1800
        elif name == "Bishop":
            self.material_value = 400
        elif name == "Knight":
            self.material_value = 400
        elif name == "Rook":
            self.material_value = 600
        elif name == "Empress": # Rook Knight
            self.material_value = 1600
        elif name == "Ferz":
            self.material_value = 300
        elif name == "Princess": # Bishop Knight
            self.material_value = 1200
        else:
            # Pawn
            self.material_value = 100

    def get_name(self):
        return self.name
    
    def get_position(self):
        return self.coordinate

    def get_tag(self):
        return self.tag

    def get_material_value(self):
        return self.material_value    

    def update_position(self, new_coordinates):
        self.coordinate = new_coordinates

    def actual_material_value(self, game_phase):
        valueTable = piecesPositionValueTable[self.get_name()][game_phase]
        pos = self.get_position()
        if self.tag == "Black":
            return self.get_material_value() + valueTable[(6-pos[0])][pos[1]]
        return self.get_material_value() + valueTable[pos[0]][pos[1]]

    @staticmethod
    def King(board, new_coordinate, tag):
        """
        RETURNS MOVEMENT (FROM_DEST, TO_DEST), COVERAGE [LIST OF DEST (INCLUDE ALLY)] THAT CAN BE TAKEN BY THE KING IN ITS POSITION
        """
        COVERAGE = set()
        MOVEMENT = set()
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
        for action in new_actionables:
            value = board.get_coordinate_value(action[0], action[1]) 
            if value == 0:# If available, do not remove
                MOVEMENT.add((new_coordinate, action))
            elif value.get_tag() != tag:
                MOVEMENT.add((new_coordinate, action))
            COVERAGE.add(action)
        return MOVEMENT, COVERAGE 
        
    @staticmethod
    def Rook(board, new_coordinate, tag):
        """
        RETURNS MOVEMENT (FROM_DEST, TO_DEST), COVERAGE [LIST OF DEST (INCLUDE ALLY)] THAT CAN BE TAKEN BY THE ROOK IN ITS POSITION
        """
        MOVEMENT = set()
        COVERAGE = set()

        North_x = new_coordinate[0] - 1
        East_y = new_coordinate[1] + 1
        South_x = new_coordinate[0] + 1
        West_y = new_coordinate[1] - 1
        
        while North_x >= 0: # Row decreasing
            value = board.get_coordinate_value(North_x, new_coordinate[1]) 
            if value == 0:
                MOVEMENT.add( ( new_coordinate, (North_x, new_coordinate[1]) ) )
                COVERAGE.add( (North_x, new_coordinate[1]) )
                North_x -= 1
                continue
            elif value.get_tag() != tag:
                MOVEMENT.add( ( new_coordinate, (North_x, new_coordinate[1]) ) )
                COVERAGE.add( (North_x, new_coordinate[1]) )
                break
            else:
                COVERAGE.add( (North_x, new_coordinate[1]) )
                break
        while East_y < board.get_width(): # Col increasing
            value = board.get_coordinate_value(new_coordinate[0], East_y) 
            if value == 0:
                MOVEMENT.add( ( new_coordinate, (new_coordinate[0], East_y) ) )
                COVERAGE.add( (new_coordinate[0], East_y) )
                East_y += 1
                continue
            elif value.get_tag() != tag:
                MOVEMENT.add( ( new_coordinate, (new_coordinate[0], East_y) ) )
                COVERAGE.add( (new_coordinate[0], East_y) )
                break
            else:
                COVERAGE.add( (new_coordinate[0], East_y) )
                break
        while South_x < board.get_height(): # Row increasing
            value = board.get_coordinate_value(South_x, new_coordinate[1]) 
            if value == 0:
                MOVEMENT.add( ( new_coordinate, (South_x, new_coordinate[1]) ) )
                COVERAGE.add( (South_x, new_coordinate[1]) )
                South_x += 1
                continue
            elif value.get_tag() != tag:
                MOVEMENT.add( ( new_coordinate, (South_x, new_coordinate[1]) ) )
                COVERAGE.add( (South_x, new_coordinate[1]) )
                break
            else:
                COVERAGE.add( (South_x, new_coordinate[1]) )
                break

        while West_y >= 0: # Col decreasing
            value = board.get_coordinate_value(new_coordinate[0], West_y) 
            if value == 0:
                MOVEMENT.add( ( new_coordinate, (new_coordinate[0], West_y) ) )
                COVERAGE.add( (new_coordinate[0], West_y) )
                West_y -= 1
                continue
            elif value.get_tag() != tag:
                MOVEMENT.add( ( new_coordinate, (new_coordinate[0], West_y) ) )
                COVERAGE.add( (new_coordinate[0], West_y) )
                break
            else:
                COVERAGE.add( (new_coordinate[0], West_y) )
                break
        return MOVEMENT, COVERAGE  

    @staticmethod    
    def Bishop(board, new_coordinate, tag):
        """
        RETURNS MOVEMENT (FROM_DEST, TO_DEST), COVERAGE [LIST OF DEST (INCLUDE ALLY)] THAT CAN BE TAKEN BY THE BISHOP IN ITS POSITION
        """
        MOVEMENT = set()
        COVERAGE = set()
        
        NE_x, NE_y = ( new_coordinate[0] - 1, new_coordinate[1] + 1 )
        SE_x, SE_y = ( new_coordinate[0] + 1, new_coordinate[1] + 1 )
        SW_x, SW_y = ( new_coordinate[0] + 1, new_coordinate[1] - 1 )
        NW_x, NW_y = ( new_coordinate[0] - 1, new_coordinate[1] - 1 )
        
        while NE_x >= 0 and NE_y < board.get_width(): # Row decreasing, Col increasing
            value = board.get_coordinate_value(NE_x, NE_y) 
            if value == 0:
                MOVEMENT.add( ( new_coordinate, (NE_x, NE_y) ) )
                COVERAGE.add( (NE_x, NE_y) )
                NE_x -= 1
                NE_y += 1
                continue
            elif value.get_tag() != tag:
                MOVEMENT.add( ( new_coordinate, (NE_x, NE_y) ) )
                COVERAGE.add( (NE_x, NE_y) )
                break
            else:
                COVERAGE.add( ( new_coordinate, (NE_x, NE_y) ) )
                break
        
        while SE_x < board.get_height() and SE_y < board.get_width(): # Row increasing, Col increasing
            value = board.get_coordinate_value(SE_x, SE_y) 
            if value == 0:
                MOVEMENT.add( ( new_coordinate, (SE_x, SE_y) ) )
                COVERAGE.add( (SE_x, SE_y) )
                SE_x += 1
                SE_y += 1
                continue
            elif value.get_tag() != tag:
                MOVEMENT.add( ( new_coordinate, (SE_x, SE_y) ) )
                COVERAGE.add( (SE_x, SE_y) )
                break
            else:
                COVERAGE.add( (SE_x, SE_y) )
                break
        
        while SW_x < board.get_height() and SW_y >= 0: # Row increasing, Col decreasing
            value = board.get_coordinate_value(SW_x, SW_y) 
            if value == 0:
                MOVEMENT.add( ( new_coordinate, (SW_x, SW_y) ) )
                COVERAGE.add( (SW_x, SW_y) )
                SW_x += 1
                SW_y -= 1
                continue
            elif value.get_tag() != tag:
                MOVEMENT.add( ( new_coordinate, (SW_x, SW_y) ) )
                COVERAGE.add( (SW_x, SW_y) )
                break
            else:
                COVERAGE.add( (SW_x, SW_y) )
                break
                
        while NW_x >= 0 and NW_y >= 0: # Row decreasing, Col decreasing
            value = board.get_coordinate_value(NW_x, NW_y) 
            if value == 0:
                MOVEMENT.add( ( new_coordinate, (NW_x, NW_y) ) )
                COVERAGE.add( (NW_x, NW_y) )
                NW_x -= 1
                NW_y -= 1
                continue
            elif value.get_tag() != tag:
                MOVEMENT.add( ( new_coordinate, (NW_x, NW_y) ) )
                COVERAGE.add( (NW_x, NW_y) )
                break
            else:
                COVERAGE.add( (NW_x, NW_y) )
                break

        return MOVEMENT, COVERAGE
    
    @staticmethod    
    def Knight(board, new_coordinate, tag):
        """
       RETURNS MOVEMENT (FROM_DEST, TO_DEST), COVERAGE [LIST OF DEST (INCLUDE ALLY)] THAT CAN BE TAKEN BY THE KNIGHT IN ITS POSITION
        """
        MOVEMENT = set()
        COVERAGE = set()
        
        # North First
        if (new_coordinate[0] - 2) >= 0:
            # Left
            if (new_coordinate[1] - 1) >= 0:
                value = board.get_coordinate_value(new_coordinate[0] - 2, new_coordinate[1] - 1)
                if value == 0 or value.get_tag() != tag:
                    MOVEMENT.add( ( new_coordinate, (new_coordinate[0] - 2, new_coordinate[1] - 1) ) )
                    COVERAGE.add( (new_coordinate[0] - 2, new_coordinate[1] - 1) )
                else:
                    COVERAGE.add( (new_coordinate[0] - 2, new_coordinate[1] - 1) )
            # Right
            if (new_coordinate[1] + 1) < board.get_width():
                value = board.get_coordinate_value(new_coordinate[0] - 2, new_coordinate[1] + 1)
                if value == 0 or value.get_tag() != tag:
                    MOVEMENT.add( ( new_coordinate, (new_coordinate[0] - 2, new_coordinate[1] + 1) ) )
                    COVERAGE.add( (new_coordinate[0] - 2, new_coordinate[1] + 1) )
                else:
                    COVERAGE.add( (new_coordinate[0] - 2, new_coordinate[1] + 1) )
                    
        # West First
        if (new_coordinate[1] + 2) < board.get_width():
            # Up
            if (new_coordinate[0] - 1) >= 0:
                value = board.get_coordinate_value(new_coordinate[0] - 1, new_coordinate[1] + 2)
                if value == 0 or value.get_tag() != tag:
                    MOVEMENT.add( ( new_coordinate, (new_coordinate[0] - 1, new_coordinate[1] + 2) ) )
                    COVERAGE.add( (new_coordinate[0] - 1, new_coordinate[1] + 2) )
                else:
                    COVERAGE.add( (new_coordinate[0] - 1, new_coordinate[1] + 2) )
            # Down
            if (new_coordinate[0] + 1) < board.get_height():
                value = board.get_coordinate_value(new_coordinate[0] + 1, new_coordinate[1] + 2)
                if value == 0 or value.get_tag() != tag:
                    MOVEMENT.add( ( new_coordinate, (new_coordinate[0] + 1, new_coordinate[1] + 2) ) )
                    COVERAGE.add( (new_coordinate[0] + 1, new_coordinate[1] + 2) )
                else:
                    COVERAGE.add( (new_coordinate[0] + 1, new_coordinate[1] + 2) )
        
        # South First
        if (new_coordinate[0] + 2) < board.get_height():
            # Left
            if (new_coordinate[1] - 1) >= 0:
                value = board.get_coordinate_value(new_coordinate[0] + 2, new_coordinate[1] - 1)
                if value == 0 or value.get_tag() != tag:
                    MOVEMENT.add( ( new_coordinate, (new_coordinate[0] + 2, new_coordinate[1] - 1) ) )
                    COVERAGE.add( (new_coordinate[0] + 2, new_coordinate[1] - 1) )
                else:
                    COVERAGE.add( (new_coordinate[0] + 2, new_coordinate[1] - 1) )
            # Right
            if (new_coordinate[1] + 1) < board.get_width():
                value = board.get_coordinate_value(new_coordinate[0] + 2, new_coordinate[1] + 1)
                if value == 0 or value.get_tag() != tag:
                    MOVEMENT.add( ( new_coordinate, (new_coordinate[0] + 2, new_coordinate[1] + 1) ) )
                    COVERAGE.add( (new_coordinate[0] + 2, new_coordinate[1] + 1) )
                else:
                    COVERAGE.add( (new_coordinate[0] + 2, new_coordinate[1] + 1) )
        
        # East First
        if (new_coordinate[1] - 2) >= 0:
            # Up 
            if (new_coordinate[0] - 1) >= 0:
                value = board.get_coordinate_value(new_coordinate[0] - 1, new_coordinate[1] - 2)
                if value == 0 or value.get_tag() != tag:
                    MOVEMENT.add( ( new_coordinate, (new_coordinate[0] - 1, new_coordinate[1] - 2) ) )
                    COVERAGE.add( (new_coordinate[0] - 1, new_coordinate[1] - 2) )
                else:
                    COVERAGE.add( (new_coordinate[0] - 1, new_coordinate[1] - 2) )
            # Down
            if (new_coordinate[0] + 1) < board.get_height():
                value = board.get_coordinate_value(new_coordinate[0] + 1, new_coordinate[1] - 2)
                if value == 0 or value.get_tag() != tag:
                    MOVEMENT.add( ( new_coordinate, (new_coordinate[0] + 1, new_coordinate[1] - 2) ) )
                    COVERAGE.add( (new_coordinate[0] + 1, new_coordinate[1] - 2) )
                else:
                    COVERAGE.add( (new_coordinate[0] + 1, new_coordinate[1] - 2) )
        
        return MOVEMENT, COVERAGE

    @staticmethod
    def Ferz(board, new_coordinate, tag):
        """
        RETURNS MOVEMENT (FROM_DEST, TO_DEST), COVERAGE [LIST OF DEST (INCLUDE ALLY)] THAT CAN BE TAKEN BY THE FERZ IN ITS POSITION
        """
        new_actionables = []
        COVERAGE = set()
        MOVEMENT = set()

        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                new_x = new_coordinate[0] + i
                new_y = new_coordinate[1] + j
                if new_x < 0 or new_y < 0 or new_x >= board.get_height() or new_y >= board.get_width(): # Check if they are out of bounds
                    continue
                else:
                    new_actionables += [ (new_x , new_y) ]
        for action in new_actionables:
            value = board.get_coordinate_value(action[0], action[1])
            if value == 0 or value.get_tag() != tag:
                MOVEMENT.add((new_coordinate, action))
                COVERAGE.add(action)
            else:
                COVERAGE.add(action)
        return MOVEMENT, COVERAGE

    @staticmethod
    def Queen(board, new_coordinate, tag):
        """
        RETURNS MOVEMENT (FROM_DEST, TO_DEST), COVERAGE [LIST OF DEST (INCLUDE ALLY)] THAT CAN BE TAKEN BY THE QUEEN IN ITS POSITION
        """
        MR, CR = Piece.Rook(board, new_coordinate, tag)
        MB, CB = Piece.Bishop(board, new_coordinate, tag)
        return MR.union(MB), CR.union(CB)

    @staticmethod 
    def Princess(board, new_coordinate, tag):
        """
        RETURNS MOVEMENT (FROM_DEST, TO_DEST), COVERAGE [LIST OF DEST (INCLUDE ALLY)] THAT CAN BE TAKEN BY THE PRINCESS IN ITS POSITION
        """
        MB, CB = Piece.Bishop(board, new_coordinate, tag)
        MK, CK = Piece.Knight(board, new_coordinate, tag)
        return MB.union(MK), CB.union(CK)     
        
    @staticmethod
    def Empress(board, new_coordinate, tag):
        """
        RETURNS MOVEMENT (FROM_DEST, TO_DEST), COVERAGE [LIST OF DEST (INCLUDE ALLY)] THAT CAN BE TAKEN BY THE EMPRESS IN ITS POSITION
        """
        MR, CR = Piece.Rook(board, new_coordinate, tag)
        MK, CK = Piece.Knight(board, new_coordinate, tag)
        return MR.union(MK), CR.union(CK)

    @staticmethod
    def Pawn(board, new_coordinate, tag):
        """
        RETURNS MOVEMENT (FROM_DEST, TO_DEST), COVERAGE [LIST OF DEST (INCLUDE ALLY)] THAT CAN BE TAKEN BY THE PAWN IN ITS POSITION
        """
        MOVEMENT = set()
        COVERAGE = set()
        if tag == "Black":
            if new_coordinate[0]-1 < 0: # Reached end of the board, no movement left
                pass
            else: 
                if board.get_coordinate_value(new_coordinate[0]-1, new_coordinate[1]) == 0: # No piece infront of the pawn
                    MOVEMENT.add( (new_coordinate, (new_coordinate[0]-1, new_coordinate[1]) ) )
                for i in range(-1, 2, 2): 
                    if new_coordinate[1]+i < 0 or new_coordinate[1]+i >= board.get_width():
                        continue
                    elif board.get_coordinate_value(new_coordinate[0]-1, new_coordinate[1]+i) == 0:
                        continue
                    else: 
                        if board.get_coordinate_value(new_coordinate[0]-1, new_coordinate[1]+i).get_tag() != tag: # Can capture a piece on either diagonals
                            MOVEMENT.add( (new_coordinate, (new_coordinate[0]-1, new_coordinate[1]+i) ) )
                    COVERAGE.add( (new_coordinate[0]-i, new_coordinate[1]+i) )
        else:
            if new_coordinate[0]+1 >= board.get_height():
                pass
            else: 
                if board.get_coordinate_value(new_coordinate[0]+1, new_coordinate[1]) == 0: # No piece infront of the pawn
                    MOVEMENT.add( (new_coordinate, (new_coordinate[0]+1, new_coordinate[1]) ) )
                for i in range(-1, 2, 2): 
                    if new_coordinate[1]+i <0 or new_coordinate[1]+i >= board.get_width():
                        continue
                    elif board.get_coordinate_value(new_coordinate[0]+1, new_coordinate[1]+i) == 0:
                        continue
                    else: 
                        if board.get_coordinate_value(new_coordinate[0]+1, new_coordinate[1]+i).get_tag() != tag: # Can capture a piece on either diagonals
                            MOVEMENT.add( (new_coordinate, (new_coordinate[0]+1, new_coordinate[1]+i) ) )
                    COVERAGE.add( (new_coordinate[0]+1, new_coordinate[1]+i) )

        return MOVEMENT, COVERAGE

    def move(self, board, new_coordinate):
        """
        RETURNS MOVEMENT (FROM_DEST, TO_DEST), COVERAGE [LIST OF DEST (INCLUDE ALLY)] OF A PIECE AT A PARTICULAR COORDINATE GIVEN 
        THE CURRENT GRID STATE
        """
        curr_piece_name = self.get_name()
        if curr_piece_name == "King":
            MOVEMENT, COVERAGE = Piece.King(board, new_coordinate, self.get_tag())
        elif curr_piece_name == "Queen":
            MOVEMENT, COVERAGE = Piece.Queen(board, new_coordinate, self.get_tag())
        elif curr_piece_name == "Rook":
            MOVEMENT, COVERAGE = Piece.Rook(board, new_coordinate, self.get_tag())
        elif curr_piece_name == "Bishop":
            MOVEMENT, COVERAGE = Piece.Bishop(board, new_coordinate, self.get_tag())
        elif curr_piece_name == "Knight":
            MOVEMENT, COVERAGE = Piece.Knight(board, new_coordinate, self.get_tag())
        elif curr_piece_name == "Ferz":
            MOVEMENT, COVERAGE = Piece.Ferz(board, new_coordinate, self.get_tag())
        elif curr_piece_name == "Princess":
            MOVEMENT, COVERAGE = Piece.Princess(board, new_coordinate, self.get_tag())
        elif curr_piece_name == "Empress":
            MOVEMENT, COVERAGE = Piece.Empress(board, new_coordinate, self.get_tag())
        elif curr_piece_name == "Pawn":
            MOVEMENT, COVERAGE = Piece.Pawn(board, new_coordinate, self.get_tag())
        else:
            # print(f'{self.get_piece_in_play().get_name()} is not a valid Chess Piece')
            pass
        return MOVEMENT, COVERAGE


#############################################################################
######## Board
#############################################################################
class Board:
    
    def __init__(self, white_pieces, black_pieces):
        # Creating the grid
        self.grid = [ [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0] ] 
        self.height = 7
        self.width = 7
        self.white_pieces = white_pieces
        self.black_pieces = black_pieces

        all_pieces = white_pieces.copy()
        all_pieces.update(black_pieces)
        for piece, pos in all_pieces.items():
            self.grid[pos[0]][pos[1]] = piece
            
    def get_grid(self):
        return self.grid

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_white_pieces(self):
        return self.white_pieces

    def get_black_pieces(self):
        return self.black_pieces

    def get_coordinate_value(self, row, col):
        return self.get_grid()[row][col]

    def apply_action(self, state, movement, player_turn):
        src, dest = movement
        new_white_pieces = {}
        new_black_pieces = {}
        if player_turn == "White":
            for white_piece, pos in self.get_white_pieces().items():
                if src == pos:
                    pos = dest # Set new position for that chess piece
                new_white_pieces[white_piece] = pos # Others all constant
            for black_piece, pos in self.get_black_pieces().items():
                if dest == pos:
                    if self.get_coordinate_value(pos[0], pos[1]).get_name() == "King":
                        state.captured_king("Black")   
                    continue
                new_black_pieces[black_piece] = pos
        else:
            for black_piece, pos in self.get_black_pieces().items():
                if src == pos:
                    pos = dest
                new_black_pieces[black_piece] = pos
            for white_piece, pos in self.get_white_pieces().items():
                if dest == pos:
                    if self.get_coordinate_value(pos[0], pos[1]).get_name() == "King":
                        state.captured_king("White")
                    continue
                new_white_pieces[white_piece] = pos
        return Board(new_white_pieces, new_black_pieces)

    def print_grid(self):
        print("/\t", end = "")
        for k in range(97, 97 + self.get_width()): # Print col index
            print(chr(k) + "\t", end = "")
        print("\n")
        for i in range(self.get_height()):
            print(str(i) + "\t", end = "") # Print row index
            for j in range(self.get_width()):
                if self.get_grid()[i][j] == 0:
                    print(str(self.get_grid()[i][j]) + "\t", end = "")
                else:
                    print(self.get_grid()[i][j].get_name() + "\t", end = "")
            print("\n")
        

#############################################################################
######## State
#############################################################################
class State:
     # Start State Material Value Total Excluding King = 4340
    
    def __init__(self, board, white_king, black_king):
        self.board = board
        self.white_king = white_king
        self.black_king = black_king
        self.white_coverage = {} # Dict containing Coord: {White Pieces threatening that coordinate} # Include Ally Position
        self.black_coverage = {} # Dict containing Coord: {Black Pieces threatening that coordinate} # Include Ally Position
        self.white_movements = set() # Contain Legal movements (FROM, TO_DEST) that can be made by the white pieces
        self.black_movements = set() # Contain Legal movements (FROM, TO_DEST) that can be made by the black pieces
        self.black_plain_mv = sum([x.get_material_value() for x in self.board.get_black_pieces()]) - 888888 # Exclude King
        self.white_plain_mv = sum([x.get_material_value() for x in self.board.get_white_pieces()]) - 888888 # Exclude King
        self.game_phase = ""

        for piece, pos in self.board.get_white_pieces().items():
            movements, actions = piece.move(self.board, pos)
            for movement in movements:
                self.white_movements.add(movement)
            for action in actions:
                if action not in self.white_coverage.keys():
                    self.white_coverage[action] = set()
                self.white_coverage[action].add(piece)

        for piece, pos in self.board.get_black_pieces().items():
            movements, actions = piece.move(self.board, pos)
            for movement in movements:
                self.black_movements.add(movement)
            for action in actions:
                if action not in self.black_coverage.keys():
                    self.black_coverage[action] = set()
                self.black_coverage[action].add(piece)

        pieces_remaining = len(self.board.get_white_pieces()) + len(self.board.get_black_pieces())
        if pieces_remaining < 10 or self.black_plain_mv < 2200 or self.white_plain_mv < 2200: # Excluding Kings
            self.game_phase = "End"
        elif pieces_remaining < 22 or self.black_plain_mv < 5500 or self.white_plain_mv < 5500: # Excluding Kings
            self.game_phase = "Middle"
        else:
            self.game_phase = "Opening"
    
    def get_board(self):
        return self.board
    
    def get_king(self, tag):
        if tag == "White":
            return self.white_king
        else:
            return self.black_king

    def get_white_movements(self):
        return self.white_movements

    def get_black_movements(self):
        return self.black_movements

    def get_white_coverage(self):
        return self.white_coverage

    def get_black_coverage(self):
        return self.black_coverage

    def get_white_plain_mv(self):
        return self.white_plain_mv

    def get_black_plain_mv(self):
        return self.black_plain_mv

    def get_game_phase(self):
        return self.game_phase

    def captured_king(self, tag):
        if tag == "White":
            self.white_king = None
        else:
            self.black_king = None

    def get_total_material_value(self, tag):
        if tag == "White":
            total_material_value = sum([x.actual_material_value(self.get_game_phase()) for x in self.board.get_white_pieces()])
        else:
            total_material_value = sum([x.actual_material_value(self.get_game_phase()) for x in self.board.get_black_pieces()])
        return total_material_value

    # chessprogramming definition
    # King zone is usually defined as squares to which enemy King can move plus two or three additional squares facing enemy position
    # Board is small, just stick with one grid movement around King
    def king_safety_evaluation(self, tag):

        if tag == "White":
            king_piece = self.get_king("White")
            coverage = self.get_black_coverage()
        else:
            king_piece = self.get_king("Black")
            coverage = self.get_white_coverage()

        actionables = set()
        king_row, king_col = king_piece.get_position()
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_x = king_row + i
                new_y = king_col + j
            if new_x < 0 or new_y < 0 or new_x >= self.board.get_height() or new_y >= self.board.get_width(): 
                continue
            else: 
                if self.board.get_coordinate_value(new_x, new_y) != 0:
                    if self.board.get_coordinate_value(new_x, new_y).get_tag() == king_piece.get_tag():
                        continue
                actionables.add((new_x , new_y))

        attackingPieces = set()
        num_squares_attack = {}
        for action in actionables:
            if action not in coverage.keys():
                continue
            attackers = coverage[action]
            for attacker in attackers:
                if attacker not in num_squares_attack.keys():
                    num_squares_attack[attacker] = 0
                num_squares_attack[attacker] += 1
            attackingPieces = attackingPieces.union(attackers)
        attackingPiecesCount = len(attackingPieces)
        valueOfAttacks = 0
        for piece, n_squares in num_squares_attack.items():
            valueOfAttacks += (threatValues[piece.get_name()] * n_squares)

        return valueOfAttacks * attackWeights[attackingPiecesCount]/100             

    def evaluate_gamestate(self, tag):
        if tag == "White":
            material_diff = self.get_total_material_value(tag) - self.get_total_material_value("Black")
            threat_value = self.king_safety_evaluation("Black")
        else:
            material_diff = self.get_total_material_value(tag) - self.get_total_material_value("White")
            threat_value = self.king_safety_evaluation("White")
        return material_diff + threat_value


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
    gameboard = {}
    
    enemy_piece_nums = get_par(handle.readline()).split()
    num_enemy_pieces = 0 # Read Enemy Pieces Positions
    for num in enemy_piece_nums:
        num_enemy_pieces += int(num)

    handle.readline()  # Ignore header
    for i in range(num_enemy_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        gameboard[coords] = (piece, "Black")    

    own_piece_nums = get_par(handle.readline()).split()
    num_own_pieces = 0 # Read Own Pieces Positions
    for num in own_piece_nums:
        num_own_pieces += int(num)

    handle.readline()  # Ignore header
    for i in range(num_own_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        gameboard[coords] = (piece, "White")    

    return rows, cols, gameboard

def add_piece(comma_seperated):
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [(r,c), piece]

def from_chess_coord( ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)

# You may call this function if you need to set up the board
def setUpBoard():
    config = sys.argv[1]
    rows, cols, gameboard = parse(config)

### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# Chess Pieces: King, Queen, Knight, Bishop, Rook, Princess, Empress, Ferz, Pawn (First letter capitalized)
# Colours: White, Black (First Letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Parameters:
# gameboard: Dictionary of positions (Key) to the tuple of piece type and its colour (Value). This represents the current pieces left on the board.
# Key: position is a tuple with the x-axis in String format and the y-axis in integer format.
# Value: tuple of piece type and piece colour with both values being in String format. Note that the first letter for both type and colour are capitalized as well.
# gameboard example: {('a', 0) : ('Queen', 'White'), ('d', 10) : ('Knight', 'Black'), ('g', 25) : ('Rook', 'White')}
#
# Return value:
# move: A tuple containing the starting position of the piece being moved to the new ending position for the piece. x-axis in String format and y-axis in integer format.
# move example: (('a', 0), ('b', 3))
            
#Implement your minimax with alpha-beta pruning algorithm here.
def minimax(gamestate, depth, player_turn, alpha=-inf, beta=inf):
    if gamestate.get_king("White") is None:
        return -888888
    elif gamestate.get_king("Black") is None:
        return 888888
    elif depth == 1:
        return gamestate.evaluate_gamestate(player_turn)
    else:
        if player_turn == "White":
            next_player_turn = "Black"
            best_value = -inf
            for movement in gamestate.get_white_movements():
                next_gamestate = State(gamestate.get_board().apply_action(gamestate, movement, player_turn), gamestate.get_king("White"), gamestate.get_king("Black"))
                curr_value = minimax(next_gamestate, depth-1, next_player_turn, alpha, beta)
                best_value = max(curr_value, best_value)
                alpha = max(best_value, alpha)
                if beta <= alpha:
                    break
            return best_value

        else:
            next_player_turn = "White"
            best_value = inf
            for movement in gamestate.get_black_movements():
                next_gamestate = State(gamestate.get_board().apply_action(gamestate, movement, player_turn), gamestate.get_king("White"), gamestate.get_king("Black"))
                curr_value = minimax(next_gamestate, depth-1, next_player_turn, alpha, beta)
                best_value = min(best_value, curr_value)
                beta = min(best_value, beta)
                if beta <= alpha:
                    break
            return best_value

def ab(gamestate):
    player_turn = "White"
    depth = 3
    best_value = -inf
    alpha = -inf
    for movement in gamestate.get_white_movements():
        next_gamestate = State(gamestate.get_board().apply_action(gamestate, movement, player_turn), gamestate.get_king("White"), gamestate.get_king("Black"))
        curr_value = minimax(next_gamestate, depth-1, "Black", alpha)
        if curr_value > best_value:
            best_value = curr_value
            best_move = movement
            alpha = best_value
    movement = ( (chr(best_move[0][1] + 97), best_move[0][0]), (chr(best_move[1][1] + 97), best_move[1][0]) ) 
    return movement

def studentAgent(gameboard):
    white_pieces = {}
    black_pieces = {}
    white_king = None
    black_king = None
    for pos, piece in gameboard.items():
        tag = piece[1]
        pos = (pos[1], ord(pos[0])-97)
        if tag == "White":
            new_piece = Piece(piece[0], pos, "White")
            if piece[0] == "King":
                white_king = new_piece
            white_pieces[new_piece] = pos
        else:
            new_piece = Piece(piece[0], pos, "Black")
            if piece[0] == "King":
                black_king = new_piece
            black_pieces[new_piece] = pos
    # You can code in here but you cannot remove this function, change its parameter or change the return type
    move = ab(State(Board(white_pieces, black_pieces), white_king, black_king))
    return move #Format to be returned (('a', 0), ('b', 3))

