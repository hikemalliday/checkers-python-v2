# Checkers V2

RESET = "\033[0m"
RED = "\033[0;31m"
BLUE = "\033[0;34m"
YELLOW = "\033[0;33m"
GREEN = "\033[32m"

class Checkers_Piece:
    def __init__(self, color):
        self.color = color
        self.king = False
    def __str__(self):
            if self.king == True and self.color == 'red':
                return RED + '♛' + RESET
            elif self.king == True and self.color == 'blue':
                return BLUE + '♛' + RESET
            elif self.king == False and self.color == 'red':
                return RED + '0' + RESET
            elif self.king == False and self.color == 'blue':
                return BLUE + '0' + RESET
            
class Checkers_Board:
    def __init__(self):
        self.board = []
        self.current_player = 'blue'
        self.blue_score = 0
        self.red_score = 0
        self.game_over = False

    def make_board(self):
        self.board = [[None] * 9 for _ in range(9)]
        # iterate over the board
        for row in range(1, 4):
            for col in range(1, 9):
                if (row + col) % 2 != 0:
                    self.board[row][col] = Checkers_Piece('red')
        for row in range(6, 9):
            for col in range(1, 9):
                if (row + col) % 2 != 0:
                    self.board[row][col] = Checkers_Piece('blue')

    def print_board(self):
        for row in range(9):
            for col in range(9):
                if row == 0:
                    print(col, end=' ')
                    continue
                if row != 0 and col == 0:
                    print(row, end= ' ')
                    continue
                if self.board[row][col] is not None:
                    print(self.board[row][col], end=' ')
                else:
                    print('.', end=' ')
            print('')

    def change_player(self):
        if self.current_player == 'red':
            self.current_player = 'blue'
        else:
            self.current_player = 'red'

    def create_king(self):
        for i, piece in enumerate(self.board[1]):
             if piece is not None:
                if piece.color == 'blue' and piece.king == False:
                    self.board[1][i].king = True

        for i, piece in enumerate(self.board[8]):
             if piece is not None:
                if piece.color == 'red' and piece.king == False:
                    self.board[8][i].king = True

    def is_jump_valid(self, starting_space, ending_space, player_color):
        # The conditional leading up to this function call ALREADY checked for ending_space to be None
        # If this func returns false, we need to tell the user that the jump / move is invalid (in the greater scoped func that this one is nested in / called from)
        enemy_piece_is_king = False
        if player_color == 'red':
            opponent_color = 'blue'
        if player_color == 'blue':
            opponent_color = 'red'

        if player_color == 'red':
            if starting_space[0] - ending_space[0] == -2 and starting_space[1] - ending_space[1] == 2: # DOWN / LEFT
                if self.board[starting_space[0] + 1][starting_space[1] - 1].color == opponent_color:
                    # Jump is valid
                    self.board[starting_space[0]][starting_space[1]] = None
                    if self.board[starting_space[0] + 1][starting_space[1] - 1].king == True:
                        enemy_piece_is_king = True
                    self.board[starting_space[0] + 1][starting_space[1] - 1] = None
                    self.board[ending_space[0]][ending_space[1]] = Checkers_Piece('red')
                    if enemy_piece_is_king == True:
                        self.board[ending_space[0]][ending_space[1]].king = True
                        starting_space = ending_space
                        self.king_double_jump_check(starting_space, player_color)
                        return True
                    starting_space = ending_space
                    self.double_jump_check(starting_space, player_color)
                    return True
                else:
                    # Jump is invalid. Return False
                    return False
            elif starting_space[0] - ending_space[0] == -2 and starting_space[1] - ending_space[1] == -2: # DOWN / RIGHT
                if self.board[starting_space[0] + 1][starting_space[1] + 1].color == opponent_color:
                    # Jump is valid
                    self.board[starting_space[0]][starting_space[1]] = None
                    if self.board[starting_space[0] + 1][starting_space[1] + 1].king == True: 
                        enemy_piece_is_king = True
                    self.board[starting_space[0] + 1][starting_space[1] + 1] = None
                    self.board[ending_space[0]][ending_space[1]] = Checkers_Piece('red')
                    if enemy_piece_is_king == True:
                        self.board[ending_space[0]][ending_space[1]].king == True
                        starting_space = ending_space
                        self.king_double_jump_check(starting_space, player_color)
                        return True
                    starting_space = ending_space
                    self.double_jump_check(starting_space, player_color)
                    return True
                else:
                    # Jump is invalid. Return False
                    return False
        elif player_color == 'blue':
            if starting_space[0] - ending_space[0] == 2 and starting_space[1] - ending_space[1] == 2: # UP / LEFT
                if self.board[starting_space[0] - 1][starting_space[1] - 1].color == opponent_color:
                    # Jump is Valid
                    self.board[starting_space[0]][starting_space[1]] = None
                    if self.board[starting_space[0] - 1][starting_space[1] - 1].king == True:
                        enemy_piece_is_king == True
                    self.board[starting_space[0] - 1][starting_space[1] - 1] = None
                    self.board[ending_space[0]][ending_space[1]] = Checkers_Piece('blue')
                    if enemy_piece_is_king == True:
                        self.board[ending_space[0]][ending_space[1]].king == True
                        starting_space = ending_space
                        self.king_double_jump_check(starting_space, player_color)
                        return True
                    starting_space = ending_space
                    self.double_jump_check(starting_space, player_color)
                    return True
                else:
                    # Jump is invalid. Return False
                    return False
            elif starting_space[0] - ending_space[0] == 2 and starting_space[1] - ending_space[1] == -2: # UP / RIGHT
                if self.board[starting_space[0] - 1][starting_space[1] + 1].color == opponent_color:
                    # Jump is Valid
                    self.board[starting_space[0]][starting_space[1]] = None
                    if self.board[starting_space[0] - 1][starting_space[1] + 1].king == True:
                        enemy_piece_is_king == True
                    self.board[starting_space[0] - 1][starting_space[1] + 1] = None
                    self.board[ending_space[0]][ending_space[1]] = Checkers_Piece('blue')
                    if enemy_piece_is_king == True:
                        self.board[ending_space[0]][ending_space[1]].king == True
                        starting_space = ending_space
                        self.king_double_jump_check(starting_space, player_color)
                        return True
                    starting_space = ending_space
                    self.double_jump_check(starting_space, player_color)
                    return True
                    # Jump logic here, make sure to handle king pieces
                else:
                    return False 
        else:
            return False
            
    def double_jump_check(self, starting_space, player_color):
        
        opponent_color = ''
        if player_color == 'red':
            opponent_color = 'blue'
        if player_color == 'blue':
            opponent_color = 'red'

        valid_jumps = []

        # Helper function to process the 'valid_jumps' elements:
        def process_valid_jumps(valid_jumps, starting_space, player_color):
            # Might not need the enemy color var:
            enemy_piece_is_king = False
            opponent_color = ''
            if player_color == 'red':
                opponent_color = 'blue'
            if player_color == 'blue':
                opponent_color = 'red'
            
            if len(valid_jumps) == 1:
                if player_color == 'red':
                    if valid_jumps[0] == 'down left':
                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] + 1][starting_space[1] - 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] + 1][starting_space[1] - 1] = None
                        self.board[starting_space[0] + 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] + 2][starting_space[1] - 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] + 2, starting_space[1] - 2]
                        self.double_jump_check(starting_space, player_color)
                        return
                    elif valid_jumps[0] == 'down right':
                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] + 1][starting_space[1] + 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] + 1][starting_space[1] + 1] = None
                        self.board[starting_space[0] + 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] + 2][starting_space[1] + 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] + 2, starting_space[1] + 2]
                        self.double_jump_check(starting_space, player_color)
                        return
                    
                elif player_color == 'blue':
                    if valid_jumps[0] == 'up left':
                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] - 1][starting_space[1] - 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] - 1][starting_space[1] - 1] = None
                        self.board[starting_space[0] - 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] - 2][starting_space[1] - 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] - 2, starting_space[1] - 2]                   
                        self.double_jump_check(starting_space, player_color)
                        return
                    elif valid_jumps[0] == 'up right':
                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] - 1][starting_space[1] + 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] - 1][starting_space[1] + 1] = None
                        self.board[starting_space[0] - 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] - 2][starting_space[1] + 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] - 2, starting_space[1] + 2]                   
                        self.double_jump_check(starting_space, player_color)
                        return

            elif len(valid_jumps) > 1:
                valid_input = False
                while valid_input == False:
                    ending_space = input('Enter the direction in which you would like to jump to (ex: up left, up right): ')
                    if player_color == 'red':
                        if ending_space == 'up left' or ending_space == 'up right':
                            print('ERROR: invalid input!1')
                            continue

                    if player_color == 'blue':
                        if ending_space == 'down left' or ending_space == 'down right':
                            print('ERROR: invalid input!2')
                            continue

                    if ending_space not in valid_jumps:
                        print('ERROR: invalid input!3')
                        continue

                    elif ending_space == 'up left':
                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] - 1][starting_space[1] - 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] - 1][starting_space[1] - 1] = None
                        self.board[starting_space[0] - 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] - 2][starting_space[1] - 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] - 2, starting_space[1] - 2]                   
                        self.double_jump_check(starting_space, player_color)
                        return
                    
                    elif ending_space == 'up right':
                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] - 1][starting_space[1] + 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] - 1][starting_space[1] + 1] = None
                        self.board[starting_space[0] - 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] - 2][starting_space[1] + 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] - 2, starting_space[1] + 2]                   
                        self.double_jump_check(starting_space, player_color)
                        return
                    
                    elif ending_space == 'down left':
                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] + 1][starting_space[1] - 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] + 1][starting_space[1] - 1] = None
                        self.board[starting_space[0] + 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] + 2][starting_space[1] - 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] + 2, starting_space[1] - 2]
                        self.double_jump_check(starting_space, player_color)
                        return
                    
                    elif ending_space == 'down right':
                        self.board[starting_space[0]][starting_space[1]] = None
                        if self.board[starting_space[0] + 1][starting_space[1] + 1].king == True:
                            enemy_piece_is_king = True
                        self.board[starting_space[0] + 1][starting_space[1] + 1] = None
                        self.board[starting_space[0] + 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                        if enemy_piece_is_king == True:
                            self.board[starting_space[0] + 2][starting_space[1] + 2].king = True
                            enemy_piece_is_king = False
                        starting_space = [starting_space[0] + 2, starting_space[1] + 2]
                        self.double_jump_check(starting_space, player_color)
                        return
            else: # No double jumps found
                return
                    
        if player_color == 'red':
            try: 
                if starting_space[0] < 7 and starting_space[1] > 2:
                    if self.board[starting_space[0] + 1][starting_space[1] - 1] is not None and self.board[starting_space[0] + 1] != 1 and self.board[starting_space[1] - 1] != 8:
                        if self.board[starting_space[0] + 1][starting_space[1] - 1].color == opponent_color and self.board[starting_space[0] + 2][starting_space[1] + 2] == None:
                            valid_jumps.append('down left')
                            print('down left appended')
            except IndexError:
                pass

            try:
                if starting_space[0] < 7 and starting_space[1] < 7:
                    if self.board[starting_space[0] + 1][starting_space[1] + 1] is not None and self.board[starting_space[0] + 1] != 1 and self.board[starting_space[1] + 1] != 8:
                        if self.board[starting_space[0] + 1][starting_space[1] + 1].color == opponent_color and self.board[starting_space[0] + 2][starting_space[1] + 2] == None:
                            valid_jumps.append('down right')
                            print('down right appended')
            except IndexError:
                pass

        if player_color == 'blue':
            try:
                if starting_space[0] > 2 and starting_space[1] > 2:
                    if self.board[starting_space[0] - 1][starting_space[1] - 1] is not None and self.board[starting_space[0] - 1] != 1 and self.board[starting_space[1] - 1] != 8:
                        if self.board[starting_space[0] - 1][starting_space[1] - 1].color == opponent_color and self.board[starting_space[0] - 2][starting_space[1] - 2] == None:
                            valid_jumps.append('up left')
                            print('down left appended')
            except IndexError:
                pass
            try:
                if starting_space[0] > 2 and starting_space[1] < 7:
                    if self.board[starting_space[0] - 1][starting_space[1] + 1] is not None and self.board[starting_space[0] - 1] != 1 and self.board[starting_space[1] + 1] != 8:
                        if self.board[starting_space[0] - 1][starting_space[1] + 1].color == opponent_color and self.board[starting_space[0] - 2][starting_space[1] + 2] == None:
                            valid_jumps.append('up right')
                            print('up right appended')
            except IndexError:
                pass   
        # we MIGHT need to redeclare starting_space every single recursive call
        process_valid_jumps(valid_jumps, starting_space, player_color)             

    def king_double_jump_check(self, starting_space, player_color):
            # I think this first var is not needed:
            # self.starting_space = starting_space
            opponent_color = ''
            if player_color == 'red':
                opponent_color = 'blue'
            if player_color == 'blue':
                opponent_color = 'red'
            
            print(starting_space)
            valid_jumps = []
            # UP / LEFT check:
            # This long line checks for a space that isnt none and isnt on the edge of the board:
            try:
                if self.board[starting_space[0] - 1][starting_space[1] - 1] is not None and self.board[starting_space[0] - 1] != 1 and self.board[starting_space[1] - 1] != 8:
                    # Check for opposite color and empty space
                        if self.board[starting_space[0] - 1][starting_space[1] - 1].color == opponent_color and self.board[starting_space[0] - 2][starting_space[1] - 2] == None:
                            valid_jumps.append('up left')
                            print('up left appended')
            except IndexError:
                pass
            # UP / RIGHT check:
            try:
                if self.board[starting_space[0] - 1][starting_space[1] + 1] is not None and self.board[starting_space[0] - 1] != 1 and self.board[starting_space[1] + 1] != 8:
                        if self.board[starting_space[0] - 1][starting_space[1] + 1].color == opponent_color and self.board[starting_space[0] - 2][starting_space[1] + 2] == None:
                            valid_jumps.append('up right')
                            print('up right appended')
            except IndexError:
                pass
            # DOWN / RIGHT check:
            try:
                if self.board[starting_space[0] + 1][starting_space[1] + 1] is not None and self.board[starting_space[0] + 1] != 1 and self.board[starting_space[1] + 1] != 8:
                    if self.board[starting_space[0] + 1][starting_space[1] + 1].color == opponent_color and self.board[starting_space[0] + 2][starting_space[1] + 2] == None:
                        valid_jumps.append('down right')
                        print('down right appended')
            except IndexError:
                pass
            # DOWN / LEFT check:
            try:
                if self.board[starting_space[0] + 1][starting_space[1] - 1] is not None and self.board[starting_space[0] + 1] != 1 and self.board[starting_space[1] - 1] != 8:
                    if self.board[starting_space[0] + 1][starting_space[1] - 1].color == opponent_color and self.board[starting_space[0] + 2][starting_space[1] + 2] == None:
                        valid_jumps.append('down left')
                        print('down left appended')
            except IndexError:
                pass
            # If jump is single, force it:
            print(valid_jumps)
            if len(valid_jumps) == 1:
                if valid_jumps[0] == 'up left':
                    self.board[starting_space[0]][starting_space[1]] = None
                    self.board[starting_space[0] - 1][starting_space[1] - 1] = None
                    self.board[starting_space[0] - 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                    self.board[starting_space[0] - 2][starting_space[1] - 2].king = True
                    if player_color == 'red':
                        self.red_score += 1
                    else:
                        self.blue_score += 1
                    starting_space = [starting_space[0] - 2, starting_space[1] - 2]                   
                    self.king_double_jump_check(starting_space, player_color)
                    return
                elif valid_jumps[0] == 'up right':
                    self.board[starting_space[0]][starting_space[1]] = None
                    self.board[starting_space[0] - 1][starting_space[1] + 1] = None
                    self.board[starting_space[0] - 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                    self.board[starting_space[0] - 2][starting_space[1] + 2].king = True
                    if player_color == 'red':
                        self.red_score += 1
                    else:
                        self.blue_score += 1
                    starting_space = [starting_space[0] - 2, starting_space[1] + 2]                   
                    self.king_double_jump_check(starting_space, player_color)
                    return
                elif valid_jumps[0] == 'down right':
                    self.board[starting_space[0]][starting_space[1]] = None
                    self.board[starting_space[0] + 1][starting_space[1] + 1] = None
                    self.board[starting_space[0] + 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                    self.board[starting_space[0] + 2][starting_space[1] + 2].king = True
                    if player_color == 'red':
                        self.red_score += 1
                    else:
                        self.blue_score += 1
                    starting_space = [starting_space[0] + 2, starting_space[1] + 2]                   
                    self.king_double_jump_check(starting_space, player_color)
                    return
                elif valid_jumps[0] == 'down left':
                    self.board[starting_space[0]][starting_space[1]] = None
                    self.board[starting_space[0] + 1][starting_space[1] - 1] = None
                    self.board[starting_space[0] + 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                    self.board[starting_space[0] + 2][starting_space[1] - 2].king = True
                    if player_color == 'red':
                        self.red_score += 1
                    else:
                        self.blue_score += 1
                    starting_space = [starting_space[0] + 2, starting_space[1] - 2]                   
                    self.king_double_jump_check(starting_space, player_color)
                    return
                
            elif len(valid_jumps) > 1:
                valid_input = False
                while valid_input == False:
                    ending_space = input('Type the direction in which you would like to jump to (ex: up left, up right): ')
                    if ending_space not in valid_jumps:
                        print('ERROR: invalid input!')
                        continue
                    elif ending_space == 'up left':
                        self.board[starting_space[0]][starting_space[1]] = None
                        self.board[starting_space[0] - 1][starting_space[1] - 1] = None
                        self.board[starting_space[0] - 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                        self.board[starting_space[0] - 2][starting_space[1] - 2].king = True
                        if player_color == 'red':
                            self.red_score += 1
                        else:
                            self.blue_score += 1
                        starting_space = [starting_space[0] - 2, starting_space[1] - 2]                        
                        self.king_double_jump_check(starting_space, player_color)
                        return
                    elif ending_space == 'up right':
                        self.board[starting_space[0]][starting_space[1]] = None
                        self.board[starting_space[0] - 1][starting_space[1] + 1] = None
                        self.board[starting_space[0] - 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                        self.board[starting_space[0] - 2][starting_space[1] + 2].king = True
                        if player_color == 'red':
                            self.red_score += 1
                        else:
                            self.blue_score += 1
                        starting_space = [starting_space[0] - 2, starting_space[1] + 2]                       
                        self.king_double_jump_check(starting_space, player_color)
                        return
                    elif ending_space == 'down right':
                        self.board[starting_space[0]][starting_space[1]] = None
                        self.board[starting_space[0] + 1][starting_space[1] + 1] = None
                        self.board[starting_space[0] + 2][starting_space[1] + 2] = Checkers_Piece(player_color)
                        self.board[starting_space[0] + 2][starting_space[1] + 2].king = True
                        if player_color == 'red':
                            self.red_score += 1
                        else:
                            self.blue_score += 1
                        starting_space = [starting_space[0] + 2, starting_space[1] + 2]                        
                        self.king_double_jump_check(starting_space, player_color)
                        return
                    elif ending_space == 'down left':
                        self.board[starting_space[0]][starting_space[1]] = None
                        self.board[starting_space[0] + 1][starting_space[1] - 1] = None
                        self.board[starting_space[0] + 2][starting_space[1] - 2] = Checkers_Piece(player_color)
                        self.board[starting_space[0] + 2][starting_space[1] - 2].king = True
                        if player_color == 'red':
                            self.red_score += 1
                        else:
                            self.blue_score += 1
                        starting_space = [starting_space[0] + 2, starting_space[1] - 2]
                        self.king_double_jump_check(starting_space, player_color)
                        return
            else: # No double jumps found
                return
            
    def get_users_move(self, current_player):
        # Not sure yet why I put this var here:
        if current_player == 'blue':
            print(YELLOW + 'PLAYER: ' + RESET + BLUE + 'Blue' + RESET)
        else:
            print(YELLOW + 'PLAYER: ' + RESET + RED + 'Red' + RESET)
        enemy_piece_is_king = False
        is_valid_piece = False
        is_valid_input = False
        is_valid_move = False

        while is_valid_piece == False:
            while is_valid_input == False:
                try:
                    starting_input = input('Select a piece to move (ex: i, j): ')
                    starting_space = list(map(int, starting_input.split(',')))
                    if len(starting_space) != 2 or starting_space[0] <= 0 or starting_space[1] <= 0 or starting_space[0] >= 9 or starting_space[1] >= 9:
                        raise ValueError
                    
                    break # Not sure why a BREAK is needed here, I thought the is_valid_input = True would work
                except ValueError:
                    print(RED + 'ERROR: ' + RESET + 'Invalid input format. Please enter two integers separated by a comma (ex: 1, 2)1')
                
            if self.board[starting_space[0]][starting_space[1]] is None or self.board[starting_space[0]][starting_space[1]].color != self.current_player:
                print(RED + 'ERROR: ' + RESET + 'That space does not contain a valid piece!1')
            else:
                is_valid_piece = True
            # COULD be an issue here, when a jump attempt is considered falsey, I dont know if i handled the while loops correctly
            #   ^^ Need to have the user enter another move if jump attempt fails.
            # Select space to move to (REGULAR piecex):
            if self.board[starting_space[0]][starting_space[1]].king == False:
                while is_valid_move == False:
                    while is_valid_input == False:
                        try:
                            ending_input = input('Select space to move to (ex: i, j): ')
                            ending_space = list(map(int, ending_input.split(',')))
                            if len(ending_space) != 2 or ending_space[0] <= 0 or ending_space[1] <= 0 or ending_space[0] >= 9 or ending_space[1] >= 9:
                                raise ValueError
                            # perhaps do NOT change this to true, just use BREAK - That way when we fail a jump attempt, we can loop again:
                            is_valid_input = True
                        except ValueError:
                            (RED + 'ERROR: ' + RESET + 'Invalid input!1')

                        if abs(starting_space[0] - ending_space[0]) == 2:
                            if self.current_player == 'red': 
                                if starting_space[0] - ending_space[0] == -2 and self.board[ending_space[0]][ending_space[1]] is None:
                                    # Could set the return value to this method to boolean, save as var, and exit state or display message based on bool
                                    is_jump_valid_boolean = self.is_jump_valid(starting_space, ending_space, self.current_player)
                                    if is_jump_valid_boolean == True:
                                        # Break the loop
                                        is_valid_move = True
                                        return
                                    else:
                                        # Jump is invalid
                                        print('Invalid move! (jump attempt, red player)')
                                        is_valid_input = False
                                        continue
                            elif self.current_player == 'blue':
                                if starting_space[0] - ending_space[0] == 2 and self.board[ending_space[0]][ending_space[1]] is None:
                                    is_jump_valid_boolean = self.is_jump_valid(starting_space, ending_space, self.current_player)
                                    if is_jump_valid_boolean == True:
                                        # Break the loop
                                        is_valid_move = True
                                        return
                                    else:
                                        # Jump is invalid
                                        print('Invalid move! (jump attempt, blue player)')
                                        is_valid_input = False
                                        continue

                        else:
                            # Just move the piece?
                            pass
            elif self.board[starting_space[0]][starting_space[1]].king == True:
                pass
                            
                        




# MAIN script:
board = Checkers_Board()
board.make_board()

board.board[4][3] = Checkers_Piece('blue')
board.board[5][6] = Checkers_Piece('red')
board.board[7][4] = Checkers_Piece('red')
board.board[2][5] = None
board.board[6][5] = None
board.board[8][3].king = True

while board.game_over == False:
    board.create_king()
    board.print_board()
    board.get_users_move(board.current_player)
    board.change_player()
                        
                            
                    

                            
