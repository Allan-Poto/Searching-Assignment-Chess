from ctypes.wintypes import tagMSG
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
# VALUES DEFINED ARE FOR BLACK PIECES, FOR WHITE PIECES FLIPPED ALL THE VALUES BEFORE USING
piecesPositionValueTable = {
    "King": {
        "Opening":[ [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "Middle":[  [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "End": [    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
            ]
    },
    "Queen": {
        "Opening":[ [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "Middle":[  [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "End": [    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ]
    },
    "Bishop": {
        "Opening":[ [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "Middle":[  [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "End": [    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ]
    },
    "Knight": {
        "Opening":[ [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "Middle":[  [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "End": [    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ]
    },
    "Rook": {
        "Opening":[ [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "Middle":[  [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "End": [    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ]
    },
    "Pawn": {
        "Opening":[ [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "Middle":[  [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "End": [    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ]
    },
    "Ferz": {
        "Opening":[ [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "Middle":[  [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "End": [    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ]
    },
    "Empress": {
        "Opening":[ [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "Middle":[  [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "End": [    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ]
    },
    "Princess": {
        "Opening":[ [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "Middle":[  [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
        "End": [    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ]
    }
}

InitialChessBoard = {
    (6, 3): ('King', 'Black'), 
    (6, 2): ('Queen', 'Black'), 
    (6, 1): ('Bishop', 'Black'), 
    (6, 0): ('Knight', 'Black'), 
    (6, 6): ('Rook', 'Black'), 
    (6, 4): ('Princess', 'Black'), 
    (6, 5): ('Empress', 'Black'), 
    (5, 1): ('Pawn', 'Black'), 
    (5, 2): ('Pawn', 'Black'), 
    (5, 3): ('Pawn', 'Black'), 
    (5, 4): ('Pawn', 'Black'), 
    (5, 5): ('Pawn', 'Black'), 
    (5, 0): ('Ferz', 'Black'), 
    (5, 6): ('Ferz', 'Black'), 
    (0, 3):('King', 'White'), 
    (0, 2): ('Queen', 'White'), 
    (0, 1): ('Bishop', 'White'), 
    (0, 0): ('Knight', 'White'), 
    (0, 6): ('Rook', 'White'), 
    (0, 4): ('Princess', 'White'), 
    (0, 5): ('Empress', 'White'), 
    (1, 1): ('Pawn', 'White'), 
    (1, 2): ('Pawn', 'White'), 
    (1, 3): ('Pawn', 'White'), 
    (1, 4): ('Pawn', 'White'), 
    (1, 5): ('Pawn', 'White'), 
    (1, 0): ('Ferz', 'White'), 
    (1, 6): ('Ferz', 'White')
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
            self.material_value = 900
        elif name == "Bishop":
            self.material_value = 330
        elif name == "Knight":
            self.material_value = 300
        elif name == "Rook":
            self.material_value = 570
        elif name == "Empress": # Rook Knight
            self.material_value = 870
        elif name == "Ferz":
            self.material_value = 120
        elif name == "Princess": # Bishop Knight
            self.material_value = 630
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
        if self.tag == "White":
            valueTable.reverse()
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
            value = board.get_coordinate_value(new_coordinate[0], East_y) 
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
            value = board.get_coordinate_value(new_coordinate[0], East_y) 
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
                COVERAGE.add( new_coordinate, (NE_x, NE_y) )
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
        if tag == "White":
            if board.get_coordinate_value(new_coordinate[0], new_coordinate[1]-1) == 0: # No piece infront of the pawn
                MOVEMENT.add( (new_coordinate, (new_coordinate[0], new_coordinate[1]-1) ) )
            for i in range(-1, 2, 2): 
                if board.get_coordinate_value(new_coordinate[0]+i, new_coordinate[1]-1).get_tag() != tag: # Can capture a piece on either diagonals
                    MOVEMENT.add( (new_coordinate, (new_coordinate[0]+i, new_coordinate[1]-1) ) )
                COVERAGE.add( (new_coordinate[0]+i, new_coordinate[1]-1) )
        else:
            if board.get_coordinate_value(new_coordinate[0], new_coordinate[1]+1) == 0: # No piece infront of the pawn
                MOVEMENT.add( (new_coordinate, (new_coordinate[0], new_coordinate[1]+1) ) )
            for i in range(-1, 2, 2): 
                if board.get_coordinate_value(new_coordinate[0]+i, new_coordinate[1]+1).get_tag() != tag: # Can capture a piece on either diagonals
                    MOVEMENT.add( (new_coordinate, (new_coordinate[0]+i, new_coordinate[1]+1) ) )
                COVERAGE.add( (new_coordinate[0]+i, new_coordinate[1]+1) )

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
    
    def __init__(self, pieces):
        self.grid = [[0]*7]*7 # Creating the grid
        self.white_pieces = {}
        self.black_pieces = {}

        for pos, piece in pieces.items():
            tag = piece[1]
            pos = (ord(pos[0])-97, pos[1])
            if tag == "white":
                new_piece = Piece(piece[0], pos, "white")
                self.white_pieces[new_piece] = pos
                self.grid[pos[0]][pos[1]] = new_piece
            else:
                new_piece = Piece(piece[0], pos, "black")
                self.black_pieces[new_piece] = pos
                self.grid[pos[0]][pos[1]] = new_piece
            
    def get_grid(self):
        return self.grid

    def get_white_pieces(self):
        return self.white_pieces

    def get_black_pieces(self):
        return self.black_pieces
        

#############################################################################
######## State
#############################################################################
class State:
     # Start State Material Value Total Excluding King = 4340
    
    def __init__(self, board):
        self.board = board
        self.white_coverage = {} # Dict containing Coord: {White Pieces threatening that coordinate}
        self.black_coverage = {} # Dict containing Coord: {Black Pieces threatening that coordinate}
        self.white_movements = set() # Contain Legal movements (FROM, TO_DEST) that can be made by the white pieces
        self.black_movements = set() # Contain Legal movements (FROM, TO_DEST) that can be made by the black pieces
        self.black_plain_mv = sum([x.get_material_value() for x in self.board.get_black_pieces()]) - 888888 # Exclude King
        self.white_plain_mv = sum([x.get_material_value() for x in self.board.get_white_pieces()]) - 888888 # Exclude King
        self.game_phase = ""

        for piece, pos in self.board.get_white_pieces().items():
            self.white_movements, actions = piece.move(self.board, pos)
            for action in actions:
                if action not in self.white_coverage.keys():
                    self.white_coverage[action] = set()
                self.white_coverage[action].add(piece)

        for piece, pos in self.board.get_black_pieces().items():
            self.black_movements, actions = piece.move(self.board, pos)
            for action in actions:
                if action not in self.black_coverage.keys():
                    self.black_coverage[action] = set()
                self.black_coverage[action].add(piece)

        pieces_remaining = len(self.board.get_white_pieces()) + len(self.board.get_black_pieces())
        if pieces_remaining < 10 or self.black_plain_mv < 1300 or self.white_plain_mv < 1300: # Including Kings
            self.game_phase = "Late"
        elif pieces_remaining < 22 or self.black_plain_mv < 3800 or self.white_plain_mv < 3800: # Including Kings
            self.game_phase = "Middle"
        else:
            self.game_phase = "Opening"
    
    def get_total_material_value(self, tag):
        if tag == "White":
            total_material_value = sum([x.actual_material_value(self.game_phase) for x in self.board.get_white_pieces()])
        else:
            total_material_value = sum([x.actual_material_value(self.game_phase) for x in self.board.get_black_pieces()])
        return total_material_value
            
#Implement your minimax with alpha-beta pruning algorithm here.
def ab(gameboard):
    pass
    # return start_position, end_position

def max_black():
    pass

def mini_white():
    pass

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

def studentAgent(gameboard):
    # You can code in here but you cannot remove this function, change its parameter or change the return type
    move = ab(gameboard)
    return move #Format to be returned (('a', 0), ('b', 3))

