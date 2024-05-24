SAMPLEARRAYS = [[['X','X','X'],
                [' ',' ',' '],
                [' ',' ',' ']],
                
                [[' ',' ',' '],
                ['X','X','X'],
                [' ',' ',' ']],
                
                [[' ',' ',' '],
                [' ',' ',' '],
                ['X','X','X']],
                
                [['X',' ',' '],
                ['X',' ',' '],
                ['X',' ',' ']],
                
                [[' ','X',' '],
                [' ','X',' '],
                [' ','X',' ']],
                
                [[' ',' ','X'],
                [' ',' ','X'],
                [' ',' ','X']],
                
                [['X',' ',' '],
                [' ','X',' '],
                [' ',' ','X']],
                
                [[' ',' ','X'],
                [' ','X',' '],
                ['X',' ',' ']],

                [['O','O','O'],
                [' ',' ',' '],
                [' ',' ',' ']],
                
                [[' ',' ',' '],
                ['O','O','O'],
                [' ',' ',' ']],
                
                [[' ',' ',' '],
                [' ',' ',' '],
                ['O','O','O']],
                
                [['O',' ',' '],
                ['O',' ',' '],
                ['O',' ',' ']],
                
                [[' ','O',' '],
                [' ','O',' '],
                [' ','O',' ']],
                
                [[' ',' ','O'],
                [' ',' ','O'],
                [' ',' ','O']],
                
                [['O',' ',' '],
                [' ','O',' '],
                [' ',' ','O']],
                
                [[' ',' ','O'],
                [' ','O',' '],
                ['O',' ',' ']],

                ]

class Borad:
    def __init__(self):
        self.arr = [[' ',' ',' '],
                    [' ',' ',' '],
                    [' ',' ',' ']]

    def choose(self, row, col, player1Test):
        if player1Test:
            self.arr[row][col] = "X"
        else:
            self.arr[row][col] = "O"
        
    def printBoard(self):
        print(self.arr[0])
        print(self.arr[1])
        print(self.arr[2])
        
class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        

class RoundsCounter:
    def __init__(self):
        self.Rounds = 1
        
    def nextRound(self):
        self.Rounds += 1
        
    def getRound(self):
        if self.Rounds % 2 == 0:
            return False
        else:
            return True
        
    def endGame(self):
        print("End Game")
        return False

def checkUserInput():
    # Getting row from the player
    check = True
    while check: 
        try:
            row = int(input("Choose row:"))
            if row < 3:
                check = False
        except ValueError:
            print("Choose one more time:")
            
    # Getting col from the player
    check = True
    while check: 
        try:    
            col = int(input("Choose column:"))
            if col < 3:
                check = False
        except ValueError:
            print("Choose one more time:")
    return row, col

#Game loop
def main():
    # Set players
    name = input("Write name:")
    player1 = Player(name)
    name = input("Write name:")
    player2 = Player(name)
    
    # Init game board
    borad = Borad()
    roundsCounter = RoundsCounter()
    row = 0
    col = 0
    
    # Start game loop
    running = True
    while running:
        # Geting input from user
        row, col = checkUserInput()
        
        # Set sign on board and show the result
        borad.choose(row=row, col=col, player1Test=roundsCounter.getRound())
        borad.printBoard()
        
        # Check if pattern exists in a board
        if roundsCounter.Rounds < 9:
            for array in SAMPLEARRAYS:
                if borad.arr == array:
                    running = roundsCounter.endGame()
                    
        # Check if max of rounds was reached
        if roundsCounter.Rounds == 9:
            running = roundsCounter.endGame()
            print("It's a draw!")

        # Go to next round
        roundsCounter.nextRound()

if __name__ == "__main__":
    main()