import random


#Code starts from here

def Changetheplayer(gamer):
    """Opposite player is returned"""
    if gamer == "O":
        return "X"
    else:
        return "O"

class TicTacToe:

    def __init__(self):
        """Numbered XO board initializaiton"""
        # self.XO_board = ["1", "2", "3", 
        #               "4", "5", "6", 
        #               "7", "8", "9"]
        self.XO_board = [" ", " ", " ", 
                      " ", " ", " ", 
                      " ", " ", " "]

    def display(self):
        """Upadation and printing the XO board"""
        print("""
             {} | {} | {}
            -----------
             {} | {} | {}
            -----------
             {} | {} | {}
        """.format(*self.XO_board))

    def MoveSetter(self, pos, gamer):
        """sets the move on board""" 
        self.XO_board[pos] = gamer

    def MoveGetter(self, pos):
        "To know which variable is there"
        if(self.XO_board[pos] == "X"):
            return "X"
        elif(self.XO_board[pos] == "O"):
            return "O"

    def MovesSoFar(self, gamer):
        """Get all moves made till now by a given gamer"""
        vectormoves = []
        i=0
        # for i in range(0, len(self.XO_board)):
        while i<len(self.XO_board) :
            if self.XO_board[i] == gamer:
                vectormoves.append(i)
            i = i+1
        return vectormoves

    def winCheker(self):
        """winner will be returned"""
        possibilities = ([0, 1, 2], 
                         [3, 4, 5], 
                         [6, 7, 8],
                         [0, 3, 6], 
                         [1, 4, 7], 
                         [2, 5, 8],
                         [0, 4, 8], 
                         [2, 4, 6])

        for gamer in (player_var, computer_var):
            positions = self.MovesSoFar(gamer)
            for possibilty in possibilities:
                winner = True
                for pos in possibilty:
                    if pos not in positions:
                        winner = False
                if winner:
                    return gamer

    def gameOver(self):
        """Return True if X wins, O wins, or draw, else return False"""
        if self.winCheker() != None:
            return True
        for i in self.XO_board:
            if i == " " :
                return False
        return True

    def Winner(self):
        if self.winCheker() == computer_var:
            return "Computer Wins. Better Luck Next time :)"
        elif self.winCheker() == player_var:
            return "Player Wins. Congratulations! you are smarter than computer XD"
        elif self.gameOver() == True:
            return "Game drawn"

    def PossiblyAMoves(self):
        """Return empty spaces on the board"""
        availablemoves = []
        i=0
        # for i in range(0, len(self.XO_board)):
        while i < len(self.XO_board):
            if self.XO_board[i] == " ":
                availablemoves.append(i)
            i=i+1
        return availablemoves

    def MinMax(self, Nd, dp, gamer):
        """
        Recursively analyze every possible game state and choose
        the best move location.

        node - the board
        depth - how far down the tree to look
        player - what player to analyze best move for (currently setup up ONLY for "O")
        """
        if dp == 0 or Nd.gameOver():
            if Nd.winCheker() == computer_var:
                return 10
            elif Nd.winCheker() == player_var:
                return 0
            else:
                return 5

        if gamer == computer_var:
            bV = 0
            for move in Nd.PossiblyAMoves():
                Nd.MoveSetter(move, gamer)
                mV = self.MinMax(Nd, dp-1, Changetheplayer(gamer))
                Nd.MoveSetter(move, " ")
                bV = max(bV, mV)
            return bV
        
        if gamer == player_var:
            bV = 10
            for move in Nd.PossiblyAMoves():
                Nd.MoveSetter(move, gamer)
                mV = self.MinMax(Nd, dp-1, Changetheplayer(gamer))
                Nd.MoveSetter(move, " ")
                bV = min(bV, mV)
            return bV
        

def make_best_move(XO_board, dp, gamer):
    """
    Controllor function to initialize minimax and keep track of optimal move choices

    board - what board to calculate best move for
    depth - how far down the tree to go
    player - who to calculate best move for (Works ONLY for "O" right now)
    """
    nV = 5
    PossChoice = []
    for move in XO_board.PossiblyAMoves():
        XO_board.MoveSetter(move, gamer)
        mV = XO_board.MinMax(XO_board, dp-1, Changetheplayer(gamer))
        XO_board.MoveSetter(move, " ")

        if mV == nV:
            PossChoice.append(move)
        elif mV > nV:
            PossChoice = [move]
            break
    # print("choices: ", choices)

    if len(PossChoice) == 0:        
        return random.choice(XO_board.PossiblyAMoves())
    elif len(PossChoice) > 0:
        return random.choice(PossChoice)

def make_random_move(XO_board) :
    return random.choice(XO_board.PossiblyAMoves())

# some string declarations
s1=""
s1+="INSTRUCTION \n"
s1+="To"
s1+=" choose"
s1+=" the"
s1+=" position"
s1+=" type"
s1+=" the"
s1+=" corresponding"
s1+=" number"

s2=""
s2+="Do"
s2+=" you"
s2+=" want"
s2+=" X"
s2+=" or"
s2+=" O"
s2+=" : "

s3=""
s3+="Do"
s3+=" you"
s3+=" want"
s3+=" to"
s3+=" play"
s3+=" first"
s3+=" Y/N"
s3+=" : "

s4="You"
s4+=" are "

s5=": "
s5+=" Choose"
s5+="  number"
s5+="  from"
s5+=" 1-9:"
s5+=" "

s6=""
s6+="Computer"
s6+=" already"
s6+=" occupied"
s6+=" that"
s6+=" position,"
s6+=" choose"
s6+=" some"
s6+=" other"
s6+=" position"

s7=""
s7+="You"
s7+=" already"
s7+=" chose"
s7+=" this"
s7+=" location,"
s7+=" choose"
s7+=" some"
s7+=" other"
s7+=" location"

s8=""
s8+="Computer"
s8+=" choosing"
s8+=" move"
s8+="..."

s9=""
s9+="Computer"
s9+=" chose"
s9+=" : "

s10=""
s10+="Computer"
s10+=" choosing"
s10+=" move"
s10+="..."

s11=""
s11+="Computer"
s11+=" chose"
s11+=" : "

s12="You"
s12+=" are "

s13=": "
s13+=" Choose"
s13+="  number"
s13+="  from"
s13+=" 1-9:"
s13+=" "

s60=""
s60+="Computer"
s60+=" already"
s60+=" occupied"
s60+=" that"
s60+=" position,"
s60+=" choose"
s60+=" some"
s60+=" other"
s60+=" position"

s70=""
s70+="You"
s70+=" already"
s70+=" chose"
s70+=" this"
s70+=" location,"
s70+=" choose"
s70+=" some"
s70+=" other"
s70+=" location"

s111=""
s111+="Game"
s111+=" Over. "
#_____________________________________________________________



#The game begins

play_again = "Y"
while play_again=="Y" : 

    diff_level = str(input("\nChoose difficulty level \nType 'E' for Easy, 'M' for Medium and 'H' for Hard : "))

    # s2= "Do you want X or O :"
    player_var = str(input(s2))
    computer_var = ""
    if player_var == "X" :
        computer_var = "O"
    else :
        computer_var = "X"


    # s3="Do you want to play first Y/N :"
    player_move = str(input(s3))

    print("\n")
    # print(" \n To choose the position type the corresponding number")
    print(s1)

    print("""
             1 | 2 | 3
            -----------
             4 | 5 | 6
            -----------
             7 | 8 | 9
            """)

    print("\n          The Game Beigns\n")


    #Game Initiation
    game = TicTacToe()

    #Gameplay
    if player_move == "Y" :
        while game.gameOver() == False:

            game.display()
            print("""
             1 | 2 | 3
            -----------
             4 | 5 | 6
            -----------
             7 | 8 | 9
            """)

            #player's turn
            player_move = int(input(s4 + player_var + s5))
            if(game.MoveGetter(player_move-1)== computer_var):
                print(s6)
                game.display()
                continue
            elif(game.MoveGetter(player_move-1)== player_var):
                print(s7)
                game.display()
                continue
            else:
                game.MoveSetter(player_move-1, player_var)

            game.display()

            if game.gameOver() == True:
                break

            #computer's turn    
            print(s8)
            if(diff_level=="H"):
                computer_ai_move = make_best_move(game, -1, computer_var)
            elif(diff_level=="E"):
                computer_ai_move = make_random_move(game)
            elif(diff_level=="M"):
                m1 = make_best_move(game, -1, computer_var)
                m2 = make_random_move(game)
                computer_ai_move = random.choice([m1,m2])

            print(s9+ str(computer_ai_move+1) )
            game.MoveSetter(computer_ai_move, computer_var)
            

    else :
        computer_ai_move = make_random_move(game)
        game.MoveSetter(computer_ai_move, computer_var)
        while game.gameOver() == False:
            
            game.display()
            print("""
             1 | 2 | 3
            -----------
             4 | 5 | 6
            -----------
             7 | 8 | 9
            """)

            #Player's turn
            player_move = int(input(s12 + player_var + s13))
            if(game.MoveGetter(player_move-1)== computer_var):
                print(s60)
                game.display()
                continue
            elif(game.MoveGetter(player_move-1)== player_var):
                print(s70)
                game.display()
                continue
            else:
                game.MoveSetter(player_move-1, player_var)

            game.display()

            if game.gameOver() == True:
                break

            #Computer's turn
            print(s10)
            if(diff_level=="H"):
                computer_ai_move = make_best_move(game, -1, computer_var)
            elif(diff_level=="E"):
                computer_ai_move = make_random_move(game)
            elif(diff_level=="M"):
                m1 = make_best_move(game, -1, computer_var)
                m2 = make_random_move(game)
                computer_ai_move = random.choice([m1,m2])

            print(s11+ str(computer_ai_move+1) )
            game.MoveSetter(computer_ai_move, computer_var)
            
    if(game.winCheker()== computer_var) :
        game.display()

    print(s111 + game.Winner())

    play_again = str(input("Do you want to play again. Y/N : "))

if(play_again =="N"):
    print("\nThanks for playing. Hope you had fun")
    print("""   
                                                     ..::''''::..
                                           .:::.   .;''        ``;.
   ....                                    :::::  ::    ::  ::    ::
 ,;' .;:                ()  ..:            `:::' ::     ::  ::     ::
 ::.      ..:,:;.,:;.    .   ::   .::::.    `:'  :: .:' ::  :: `:. ::
  '''::,   ::  ::  ::  `::   ::  ;:   .::    :   ::  :          :  ::
,:';  ::;  ::  ::  ::   ::   ::  ::,::''.    .    :: `:.      .:' ::
`:,,,,;;' ,;; ,;;, ;;, ,;;, ,;;, `:,,,,:'   :;:    `;..``::::''..;'
                                                     ``::,,,,::''
    Had so much fun in this CS242 course 
    Thanks
    Aadarsh
        """)
