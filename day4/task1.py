#!/usr/bin/python3

def boardHasBingo(board):
    for row in board:
        numOfMarked = 0
        for number in row:
            if number["marked"] == True:
                numOfMarked += 1
        if numOfMarked == len(row):
            return True

    for pos in range(len(board[0])):
        numOfMarked = 0
        for row in board:
            if row[pos]["marked"] == True:
                numOfMarked += 1
        if numOfMarked == len(board):
            return True

    return False

numbers = []
boards = []

with open('./inputs.txt', 'r') as file:
    lines = file.readlines()
    last = lines[-1]
    numbers = list(map(int, lines[0].split(',')))
    board = []
    for line in lines[1:]:
        if len(line) > 1:
            row = []
            for num in line.strip().replace('  ', ' ').split(' '):
                row.append({
                    "number": int(num),
                    "marked": False
                })
            board.append(row)
            if line == last:
                boards.append(board)
        else:
            if len(board) > 0:
                boards.append(board)
            board = []

for calledNumber in numbers:
    done = False
    for board in boards:
        for row in board:
            for num in row:
                if num["number"] == calledNumber:
                    num["marked"] = True
        if boardHasBingo(board):
            sumOfUnmarked = 0
            for row in board:
                for num in row:
                    if num["marked"] == False:
                        sumOfUnmarked += num["number"]
            print(f"Sum of unmarked numbers times called number is: {sumOfUnmarked * calledNumber}")
            done = True

    if done:
        break

