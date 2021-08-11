# import required modules here
import math
# python code goes here


#   display board - based on size selected
class Board:
    '''
    Creates a 2d list for the game board(s)
    to display ship locations

    @parameters
    takes in name, dimensions

    '''
    number_of_ships_ratio = 0.6

    def __init__(self, name, dimensions):
        self.name = name
        self.dimensions = dimensions
        self.board = [
            ["~" for i in range(dimensions)] for i in range(dimensions)
            ]

    def calculate_number_of_ships(self):
        number_of_ships_ratio = 0.6
        number_of_ships = math.floor(self.dimensions * number_of_ships_ratio)
        print(number_of_ships)
        return number_of_ships


def setup(dimensions, difficulty):

    player = Board('player', dimensions)
    comp = Board('comp', dimensions)

    letter = 0
    # display_boards = 2
    # for i in range(display_boards):

    print(' '*2, end='| ')
    for i in range(dimensions):
        # print('    ')
        print(i, end=' ')
    print('| ', ' '*20, end=' ')
    print(' '*2, end='| ')
    for i in range(dimensions):
        # print('    ')
        print(i, end=' ')
    print('| ')

    # for letter in range(dimensions):
    #     print(chr(letter + 65), end=' | ')
    #     for row in range(dimensions):
    #         for column in range(dimensions):
    #             print(player.board[row][column], end=' ')
    #         print(' | ')

    for letter in range(dimensions):
        print(chr(letter + 65), end=' | ')
        for column in range(len(player.board[letter])):
            print(player.board[letter][column], end=' ')
        print('|', ' '*20, end='  ')
        print(chr(letter + 65), end=' | ')
        for column in range(len(comp.board[letter])):
            print(comp.board[letter][column], end=' ')
        print('| ')
        letter += 1

    print(player.calculate_number_of_ships())
    # for row in range(dimensions):
    #     print(player.board[row][column])
    #     row += 1
    # print(comp.board)

# GAME SETUP LOGIC

#   display message informing user on next ship to be placed - name and size
#   user input starting location for next ship
#   input validation
#   display error message - repeat user input
#   validation of ship location - does ship fit starting in that location in
#       either horizontal or vertical orientation?
#   if fails location validation - display error message to user
#       informing them why and repeat user input
#   display message asking user if ship horizontal or vertical
#   user choice h = horizontal v = vertical
#   user input layout of ship, horizontal or vertical
#   input validation
#   display error message if wrong type of input inserted by user
#       - repeat user input
#   validation of ship location - does ship fit in selected location
#   display error message if ship does not fit, informing user why
#       - repeat user input
#   validation of ship location - does ship overlap any other ships?
#   display error message informing user
#       - repeat user input to select alternative location
#   ship location ok
#   store ship location to board
#   check to see if more ships still to be placed
#       if yes repeat earlier steps for next ship
#   finalise grid and store player ship locations

# USER OPTIONS LOGIC
#   Game Start
#   Display Welcome Message


def welcome():

    #   difficulty options -
    #   easy, comp selects location at random,
    #   normal, comp will select neighbouring tiles on hit,
    #   hard, comp will pick tiles based on algorithm
    def get_difficulty(dimensions):

        loop = True
        while loop:
            try:
                if dimensions == 6:
                    difficulty = input('''
    A little one, suppose you want it easy as well? Select your difficulty,
    enter 'E' for easy, 'N' for normal or 'H' for hard : ''').lower()
                    if difficulty == 'e':
                        loop = False
                        print("difficulty set to easy")
                        print(difficulty)
                        setup(dimensions, difficulty)
                    elif difficulty == 'n':
                        loop = False
                        print("difficulty set to normal")
                        print(difficulty)
                        setup(dimensions, difficulty)
                    elif difficulty == 'h':
                        loop = False
                        print("difficulty set to hard")
                        print(difficulty)
                        setup(dimensions, difficulty)
                    else:
                        print('''
    There ye go getting artistic, are ye a pirate or a West Indian spy?
    Try again, before we make ye walk the plank, it's 'E', 'N' or 'H' ''')
                elif dimensions == 10:
                    difficulty = input('''
    Hmm a full one, ye be a brave pirate to tryin to impress me? If you really
    want to impress me, you should try it on hard Select your difficulty,
    enter 'E' for easy, 'N' for normal or 'H' for hard : ''').lower()
                    if difficulty == 'e':
                        loop = False
                        print("difficulty set to easy")
                        print(difficulty)
                        setup(dimensions, difficulty)
                    elif difficulty == 'n':
                        loop = False
                        print("difficulty set to normal")
                        print(difficulty)
                        setup(dimensions, difficulty)
                    elif difficulty == 'h':
                        loop = False
                        print("difficulty set to hard")
                        print(difficulty)
                        setup(dimensions, difficulty)
                    else:
                        print('''
    There ye go getting artistic, are ye a pirate or a West Indian spy?
    Try again, before we make ye walk the plank, it's 'E', 'N' or 'H' ''')
            except ValueError:
                print('''
    There ye go getting artistic, are ye a pirate or a West Indian spy?
    Try again, before we make ye walk the plank, it's 'E', 'N' or 'H' ''')

#   user input of choice of board Size
    def get_dimensions():

        print('''
    Good on ya, argh, we'll make a pirate out of ye yet!''')
        while True:
            try:
                dimensions = int(input('''
    How brave are ye? Shall we play a full game or a little one?
    Select a board size, enter '6' for a little one or '10' for normal : '''))
#   validation of user input
                if dimensions == 6:
                    get_difficulty(dimensions)
                    break
                elif dimensions == 10:
                    get_difficulty(dimensions)
                    break
                else:
                    continue
# added incase the value entered does not convert to an int
# but it doesn't seem to work
#   display error message if input fails vaidation
            except TypeError:
                print('''
    It needs to be a number see, like a '6' or a '10'
    Let's try again!''')
            except ValueError:
                print('''
    Don't be getting all artistic with the choices like some scurvy landlover
    It's either '6' or '10' that be it. Try again!''')

    print('''
    Welcome to Pirate Battleships
    This is a test for the multi line string
    To see how it formats it when it runs
    ''')
    print('''
      . .    . .  . . .  . .  . .     ,((/. .    . .  . . .  . .  . .    . .
    . .    . .  . . .  . .  .@@@@@@@@@@@@@@@@@ . .  . . .  . .  . .    . .
    . .    . .  . . .  . . @@@@@@@@@@@@@@@@@@@@@ .  . . .  . .  . .    . .
    @ . .    . .  . . .  . .&@@@@@@@@@@@@@@@@@@@@@@   . . .  . .  . .    . ,
    .@@ .    . .  . . .  .  @@*@@@@@@@@@@@@@@@@@@@@@  . . .  . .  . .    .@@
    *@@@    . .  . . .  . .@/@@.     @@@/. .  %@ @@  . . .  . .  . .  /@@@
    .@@@@( . .  . . .  . .@/@@.    @@.@@@ .  @@ @.  . . .  . .  . .@@@.@ .
    . .@@@@@ .  . . .  . ..@@@@@@@@@ . /@@@@@@@@@.  . . .  . .  *@@@,@ . .
    . .  @@@@@@ .   .  .        %@@@@@&@@@@@ *%. .  . . .  . .@@@@%@   . .
            &@@@@@@.          ,@( (@@@@@@@@  @@            #@@@@,@,
    . .    . @@@@@#@@  .     @@    . .. . ,@(  .    ..@@&@@@@(  . .  . .
    .  . .  . .    %@@@@.@@@   . @@@@@@@@@@@@@/ . . *@@&.@@@@,.    . .  . .
    .  . .  . .    . . @@@@&,@@@&   @@@&@@@% . .@@@@ @@@@&  . .    . .  . .
    .  . .  . .    . .  .  @@@@@,%@@@@/ ..&@@@@,&@@@@# . .  . .    . .  . .
    .  . .  . .  @@@@@  . .    .@@@@@%.@@@@@&,%@# .    . .%@@@@    . .  . .
    .  . .  . .  @@@.@@@. ,%@@@@@& ,#*@@@@@@* (@@@@@@* .@@@%@@@.   . .  . .
    .  . .@@@ @@(@@*@&%@@@@ &@@@@@@#. . .  .*@@@@@@@*/@@@@ @,@@ @@ @@@  . .
    .  . @@@@@ @@@@@@@@%@@ *   . .  . . .  . .  . . . @@@/@@@@@@@,*@@@@ . .
        ,@@/          @@@ (#                    *% /@@          (@@#
                        @@@@@%                   @@@@@
    ''')
#   Grid size selection 6x6 or 10x10 message

    loop = True
    while loop:
        play = input('''
    Would you like to play a game me 'arty?
    (enter 'Y' to play or 'Q' to quit) : ''').lower()

        try:
            if play == "y":
                get_dimensions()
            elif play == "q":
                print('''
    Goodbye''')
                quit()
            else:
                print('''
    Argh! you woke me up for nothin... I should make ye walk the plank...
    Wait, shall we try that again?
    from the else statement''')
                continue
        except ValueError:
            print('''
    Argh! you woke me up for nothin... I should make ye walk the plank...
    Wait, shall we try that again?
    from the first valueerror''')
        except TypeError:
            print('''
    Argh! you woke me up for nothin... I should make ye walk the plank...
    Wait, shall we try that again?
    from the first type error''')


# PLAY GAME LOGIC
#   display grids, one for targetting one for showing own ships locations.
#   display message to user about selecting firing location
#   display message to user to select which column
#   user input of column - should be integer
#   user input validation
#       - column selection
#       - will come in as string
#       - convert to int
#   if value fails validation display error message and have user repeat input
#   display message to user to select row
#   user input of row - should be string - letter
#   user input validation
#       - row selection
#       - will come in as string
#       - convert to lowercase using .lower()
#   if value fails validation
#       - display error message and have user repeat input
#   validated target location check - has target been selected before?
#   if target previously been entered
#       - display error message to user and restart targetting process
#   check target location for enemy ship
#   hit or miss?


# HIT LOGIC LOOP
#   Record hit to board and ship record
#   Did hit sink a ship?
#   if yes, display ship that sunk message
#   are there any other ships remaining?
#   if no, player wins game - game over
#   if yes, display refreshed board and restart targetting loop
#       - user gets another go.


# MISS LOGIC
#   Record miss to board and shot record
#   display updated board
#   start other player turn


# AI SHOT LOGIC
#   AI selects firing location
#       - easy mode fully random selection
#       - normal mode AI will pick neighbouring tiles on hit
#       - hard mode AI uses algorithm to select targets
#   check location not previously selected
#   check if location a hit or miss
#   if hit - run hit logic loop
#   if miss - run miss logic loop


# END OF GAME LOGIC
#   Display end of game screen
#   display message to user showing who won and final score
#   display thank you for playing message
#   ask user if they would like to play again
#   user input y for yes n for no
#   user input validation
#   if yes - restart game
#   if no - display a thank you for playing message and exit app

welcome()
