### 井字遊戲！

# 程式碼版本（vision)
  python 3.7.3
  
# 遊玩方式(overview)
  先決定玩家為Ｏ或Ｘ
  玩家先手，跟電腦進行遊戲
  
# 遊戲設計流程（program flow）
  棋盤：
  1  2  3 
  4  5  6
  7  8  9
  模擬下棋後的狀況
  ```
   for let in [chess[1],chess[0]]:
        for i in possible_move:
            boardcopy = board[:]
            boardcopy[i] = let
            if win(boardcopy,let):
                move = i
                return move
  ```
  先防禦必勝格5號格
  ```
  if 5 in possible_move:
            move = 5
            return move
  ```
  接著防禦角落格(1,3,7,9號格）
  
  ```
  for i in possible_move:
        if i in[1,3,7,9]:
            corner.append(i)

        if len(corner) > 0:
            move = random(corner)
            return move
  ```
  最後考慮2,4,6,8號格防禦
  ```
  for i in possible_move:
        if i in[2,4,6,8]:
            edge.append(i)

        if len(edge) > 0:
            move = random(edge)
            return move
  ```
  
  
