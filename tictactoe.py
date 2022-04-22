board = [' ' for x in range(10)] 
chess = ['O','X']
def input_letter(letter,position): 
    board[position] = letter

def chooseOX():
    print("你想要當Ｏ還是Ｘ？")
    a = input()
    if a=='O':
        chess[0] = 'O'
        chess[1] = 'X'
    else:
        chess[0] = 'X'
        chess[1] = 'O'
def printboard(board):
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] )
    print("   |   |")
    print("------------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] )
    print("   |   |")
    print("------------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] )
    print("   |   |")

def emptyspace(position):
    return board[position] == ' '


def win(board, letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter)or(board[4] == letter and board[5] == letter and board[6] == letter)or(board[7] == letter and board[8] == letter and board[9] == letter)or(board[1] == letter and board[4] == letter and board[7] == letter)or (board[2] == letter and board[5] == letter and board[8] == letter)or(board[3] == letter and board[6] == letter and board[9] == letter)or(board[1] == letter and board[5] == letter and board[9] == letter)or(board[3] == letter and board[5] == letter and board[7] == letter)


def boardfull(board):
    if board.count(' ') > 1:
        return False
    
    else:
        return True
 
def playermove():
    run = True
    while run:
        p_move = int(input("要將 " + chess[0] + " 放在哪一格? (1- 9):"))
        if p_move > 0 and p_move < 10:
            if emptyspace(p_move):
                input_letter(chess[0], p_move)
                run = False
            else:
                print("這格子已經被佔領過了，請選擇其他未佔領的格子")
        else:
            print("輸入錯誤")
def computermove():
    possible_move = [x for x,letter  in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in [chess[1],chess[0]]:
        for i in possible_move:
            boardcopy = board[:]
            boardcopy[i] = let
            if win(boardcopy,let):
                move = i
                return move

    if 5 in possible_move:
            move = 5
            return move
        
    corner = []
    for i in possible_move:
        if i in[1,3,7,9]:
            corner.append(i)

        if len(corner) > 0:
            move = random(corner)
            return move
    edge = []
    for i in possible_move:
        if i in[2,4,6,8]:
            edge.append(i)

        if len(edge) > 0:
            move = random(edge)
            return move

def random(a):
    import random as r
    ln = len(a)
    r = r.randrange(0,ln)
    return a[r]
        
def main():
    print("九宮格遊戲！")
    printboard(board)
    chooseOX()
    
        
    
    while boardfull(board) == False:
        if win(board, chess[0]):
            print('玩家勝利')
            
            
        else:
            playermove()
            printboard(board)
            if win(board, chess[0]):
                print('玩家勝利')
                break
            if (boardfull(board)):
                print("平手")
                break

        if win(board, chess[1]):
            print('電腦獲勝')
            
        else:
            move = computermove()
            if move == 0:
                print("平手")
            else:
                input_letter(chess[1],move)
                print("電腦將" , chess[1] , "放在第" ,move, "格")
                printboard(board)

                if win(board, chess[1]):
                    print('電腦獲勝')
                    break
                if (boardfull(board)):
                    print("遊戲結束")
                    break
                
main()       
