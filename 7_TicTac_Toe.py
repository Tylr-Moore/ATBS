import pprint

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ','mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
pprint.pprint(theBoard)

theBoard['top-L'] = 'O'
theBoard['top-M'] = 'O'
theBoard['top-R'] = 'O'
theBoard['mid-L'] = 'X'
theBoard['mid-M'] = 'X'
theBoard['low-R'] = 'X'


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

    
printBoard(theBoard)
