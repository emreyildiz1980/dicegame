
# Dice Game
from random import randint
class Player:
    def __init__(self, name):
        self.name = name

class Game:
    def __init__(self):
        self.results = []

class Dice:
    def __init__(self, list ):
        self.list = list

    def printDice(self, dice_result):
        length = len(dice_result)
        for i in range(length):
            print(dice_result[i])

    def get_value(self, element):
        return self.list.index(element) + 1


D1 = ["+-------+", "|       |", "|   O   |", "|       |", "+-------+"] # python listesi
a_tuple = (1, "Emre")
number_list = [2, 3, 5, 23, "emre"]
char_list = ['a', 'b', 'z']

D2 = ['+-------+',
      '| 0     |',
      '|       |',
      '|     0 |',
      '+-------+']

D3 = ['+-------+',
      '| 0     |',
      '|   0   |',
      '|     0 |',
      '+-------+']

D4 = ['+-------+',
      '| 0   0 |',
      '|       |',
      '| 0   0 |',
      '+-------+']

D5 = ['+-------+',
      '| 0   0 |',
      '|   0   |',
      '| 0   0 |',
      '+-------+']

D6 = ['+-------+',
      '| 0 0 0 |',
      '|       |',
      '| 0 0 0 |',
      '+-------+']

if __name__ == '__main__':
    dice_list = [D1, D2, D3, D4, D5, D6]

    dice = Dice(dice_list)

    game = Game()

    player1_name = input("1. oyuncu ismini giriniz : ")

    player1 = Player(player1_name)

    player2_name = input("2. oyuncu ismini giriniz : ")

    player2 = Player(player2_name)


    result1 = input(f"{player1.name}.. Lutfen zar atmak icin Enter a basiniz")
    random_index = randint(0, len(dice.list) - 1)
    random_dice = dice.list[random_index]
    dice.printDice(random_dice)
    game.results.append(random_index + 1)

    result2 = input(f"{player2.name}.. Lutfen zar atmak icin Enter a basiniz")
    random_index = randint(0, len(dice.list) - 1)
    random_dice = dice.list[random_index]
    dice.printDice(random_dice)
    game.results.append(random_index + 1)

    if(game.results[0] > game.results[1]):
        print(f"{player1.name} kazandi")
    elif(game.results[0] == game.results[1]):
        print("Berabere")
    else:
        print(f"{player2.name} kazandi")




