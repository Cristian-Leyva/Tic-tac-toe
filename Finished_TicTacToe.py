from graphics import *

board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
    ]

def makeline(point1x,point1y,point2x,point2y,width):
    line=Line(Point(point1x,point1y),Point(point2x,point2y))
    line.setWidth(width)
    return line

win=GraphWin("Window",1000,1000)
win.setBackground(color_rgb(0,255,200))

def makeo(center):
    cir=Circle(Point(center[0],center[1]),50)
    cir.setWidth(10)
    cir.draw(win)

def makex(center):
    cross1=Line(Point(center[0]-50,center[1]+50),Point(center[0]+50,center[1]-50))
    cross2=Line(Point(center[0]-50,center[1]-50),Point(center[0]+50,center[1]+50))
    cross1.setWidth(10)
    cross2.setWidth(10)
    cross1.draw(win)
    cross2.draw(win)

def outofbounds(coords):
    if coords.getX()<=50 or coords.getX()>=950 or coords.getY()<=50 or coords.getY()>=950:
        return False
    else: return True

def current_user(user):
    if user: return "x"
    else: return "o"

def add_to_board(storexy, active_user):
    row=storexy[1]
    col=storexy[0]
    board[row][col]=active_user

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()

def istaken(storexy, board):
    row=storexy[1]
    col=storexy[0]
    if board[row][col]!="-":
        print("This position is already taken.")
        return True
    else: return False

def iswin(user, board):
    if check_row(user, board):return True
    if check_col(user, board):return True
    if check_diag(user,board):return True
    return False

def check_row(user, board):
    for row in board:
        complete_row=True
        for slot in row:
            if slot !=user:
                complete_row=False
                break
        if complete_row:return True
    return False

def check_col(user, board):
    for col in range(3):
        complete_col=True
        for row in range(3):
            if board[row][col]!=user:
                complete_col=False
                break
        if complete_col:return True
    return False

def check_diag(user, board):
    if board[0][0]==user and board[1][1]==user and board[2][2]==user:return True
    elif board[0][2]==user and board[1][1]==user and board[2][0]==user:return True
    else:return False

def main():

    user=True
    Turns=0

    line=makeline(350,50,350,950,5)
    line2=makeline(650,50,650,950,5)
    line3=makeline(50,350,950,350,5)
    line4=makeline(50,650,950,650,5)

    square=Rectangle(Point(35,35),Point(965,965))
    square.setWidth(15)

    line.draw(win)
    line2.draw(win)
    line3.draw(win)
    line4.draw(win)
    square.draw(win)
    
    while Turns<9:
        active_user=current_user(user)
        coords=win.getMouse()
        if not outofbounds(coords):
            continue
        coordsX=coords.getX()-50
        coordsY=coords.getY()-50
        xxx = int(coordsX/300.0)
        yyy = int(coordsY/300.0)
        storexy=(xxx,yyy)
        if istaken(storexy,board):
            continue
        add_to_board(storexy,active_user)
        print_board(board)
        center = (xxx * 300 + 200,yyy * 300 + 200)
        if user:makex(center)
        else:makeo(center)
        if iswin(active_user, board):
            print(f"{active_user.upper()} won!")
            print_board(board)
            break
        user=not user
        Turns+=1
        if Turns==9:print("Tie!")

    win.getMouse()
    win.close()

main()