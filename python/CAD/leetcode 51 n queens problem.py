def issafe(row,col,board,n):
    duprow = row
    dupcol = col
    while row>=0 and col>=0:
        if board[row][col]=="Q":
            return False
        row-=1
        col-=1
    
    col = dupcol
    row = duprow
    while col>=0:
        if board[row][col]=="Q":
            return False
        col-=1
    
    col = dupcol
    row = duprow
    while col>=0 and row<n:
        if board[row][col]=="Q":
            return False
        col-=1
        row+=1
    return True

    

def s(n,board,ans,col):
    if col==n:
        ans.append(list(board[:]))
        return
    
    for row in range(n):
        if issafe(row,col,board,n):
            board[row]=board[row][:col]+"Q"+board[row][col+1:]
            s(n,board,ans,col+1)
            board[row]=board[row][:col]+"."+board[row][col+1:]



n = 4
board = ["."*n for _ in range(n)]
ans = []
s(n,board,ans,0)
print(ans)