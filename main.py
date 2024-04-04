class Borad:
    def __init__(self):
        self.arr = arr = [[' ',' ',' '],
                          [' ',' ',' '],
                          [' ',' ',' ']]
        print(self.arr)

    def choose(self, row, col):
        self.arr[row][col] = "X"
        print(self.arr[0])
        print(self.arr[1])
        print(self.arr[2])
        
class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

#Signs


#Player

#Game loop
def play_game():
    name = input("Write name:")
    player1 = Player(name)
    name = input("Write name:")
    player2 = Player(name)
    borad = Borad()
    row = 0
    col = 0
    check = True
    while check: 
        try:
            row = int(input("Choose row:"))
            check = False
        except ValueError:
            print("Choose one more time:")
    check = True
    while check: 
        try:    
            col = int(input("Choose column:"))
            check = False
        except ValueError:
            print("Choose one more time:")

    print(player1.name)
    print(player1.points)
    print(player2.name)
    print(player2.points)
    borad.choose(row=row, col=col)
    

if __name__ == "__main__":
    play_game()