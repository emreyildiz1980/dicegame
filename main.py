import random


def printDice(arr):
    arr_length = len(arr)
    for i in range(arr_length):
        print(arr[i])


D1 = ['+-------+',
      '|       |',
      '|   O   |',
      '|       |',
      '+-------+']

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
    dice = [D1, D2, D3, D4, D5, D6]
    dice_length = len(dice)
    dice_index = random.randint(0, dice_length - 1)
    random_dice = dice[dice_index]
    printDice(random_dice)
