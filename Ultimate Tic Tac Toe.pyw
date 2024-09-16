# Импорт библиотек

from os import stat
from turtle import * # Графика
from winsound import * # Звуки

# Переменные

player = None
big_selected_cell = None
small_selected_cell = None
loading = 0
cells = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
screen = Screen()
xcell = [3,3,3,3,3,3,3,3,3]
ocell = [4,4,4,4,4,4,4,4,4]
Beep(500,50)
status = 0
hideturtle()
# Функции нацеленные на отрисовку

def PrintStartScreen():
    up()
    title("Start Screen")
    pensize(5)
    speed(9999999999999999999999999999999999999999999)
    down()
    fd(-200)
    for i in range(3):
        for i in range(2):
            fd(400)
            rt(90)
            fd(50)
            rt(90)   
        up()
        goto(xcor(),ycor()-50)
        down()
    up()
    goto(0,100)
    write("Ultimate\n Tic Tac Toe", move=False, align="center", font=("Courier New", 60, "normal"))
    goto(0,-50)
    write("Play", move=False, align="center", font=("Courier New", 35, "normal"))
    goto(0,-100)
    write("Rules", move=False, align="center", font=("Courier New", 35, "normal"))
    goto(0,-150)
    write("Language", move=False, align="center", font=("Courier New", 35, "normal"))

def PrintMiniCell(x, y): # Отрисовка маленькой части поля
    title("Loading...")
    up()
    goto(x, y)
    goto(xcor()+25,ycor()+75)
    down()
    fd(150)
    up()
    goto(xcor(),ycor()+50)
    down()
    fd(-150)
    rt(90)
    up()
    goto(xcor()+50,ycor()+50)
    down()
    fd(150)
    up()
    goto(xcor()+50,ycor())
    down()
    fd(-150)
    lt(90)
    up()

def PrintCells(): # Отрисовка поля
    title("Loading...")
    up()
    pensize(10)
    speed(10)
    goto(-300, 100)
    down()
    fd(600)
    up()
    goto(xcor(),ycor()-200)
    down()
    fd(-600)
    rt(90)
    up()
    goto(-100,300)
    down()
    fd(600)
    up()
    goto(xcor()+200,ycor())
    down()
    fd(-600)
    lt(90)
    up()
    pensize(5)
    speed(9999999999999)
    PrintMiniCell(-300,100)
    PrintMiniCell(-100,100)
    PrintMiniCell(100,100)
    PrintMiniCell(-300,-100)
    PrintMiniCell(-100,-100)
    PrintMiniCell(100,-100)
    PrintMiniCell(-300,-300)
    PrintMiniCell(-100,-300)
    PrintMiniCell(100,-300)
    hideturtle()

def clear_select(s):
    title("Loading...")
    up()
    pensize(5)
    color("white")
    speed(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    if s == 1:
        goto(-300,100)
    if s == 2:
        goto(-100,100)
    if s == 3:
        goto(100,100)
    if s == 4:
        goto(-300,-100)
    if s == 5:
        goto(-100,-100)
    if s == 6:
        goto(100,-100)
    if s == 7:
        goto(-300,-300)
    if s == 8:
        goto(-100,-300)
    if s == 9:
        goto(100,-300)
    goto(xcor()+20,ycor()+20)
    down()
    for i in range(4):
        fd(160)
        lt(90)
    up()

def PrintSelect(): # Отрисовка выбора большой клетки
    global big_selected_cell
    title("Loading...")
    for i in range(1,10):
        clear_select(i)
    up()
    pensize(5)
    color("black")
    speed(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    if big_selected_cell == 0:
        goto(-300,100)
    if big_selected_cell == 1:
        goto(-100,100)
    if big_selected_cell == 2:
        goto(100,100)
    if big_selected_cell == 3:
        goto(-300,-100)
    if big_selected_cell == 4:
        goto(-100,-100)
    if big_selected_cell == 5:
        goto(100,-100)
    if big_selected_cell == 6:
        goto(-300,-300)
    if big_selected_cell == 7:
        goto(-100,-300)
    if big_selected_cell == 8:
        goto(100,-300)
    goto(xcor()+20,ycor()+20)
    for i in range(4):
        down()
        fd(30)
        up()
        fd(100)
        down()
        fd(30)
        lt(90)
        up()
    pencolor("yellow")
    pensize(3)
    for i in range(4):
        down()
        fd(30)
        up()
        fd(100)
        down()
        fd(30)
        lt(90)
    up()
    hideturtle()

def PrintCross(s, i):
    title("Loading...")
    Beep(500,50)
    up()
    pensize(5)
    color("black")
    speed(10)
    if s == 0:
        goto(-300,100)
    if s == 1:
        goto(-100,100)
    if s == 2:
        goto(100,100)
    if s == 3:
        goto(-300,-100)
    if s == 4:
        goto(-100,-100)
    if s == 5:
        goto(100,-100)
    if s == 6:
        goto(-300,-300)
    if s == 7:
        goto(-100,-300)
    if s == 8:
        goto(100,-300)
    if i == 0:
        goto(xcor()+25,ycor()+125)
    if i == 1:
        goto(xcor()+75,ycor()+125)
    if i == 2:
        goto(xcor()+125,ycor()+125)
    if i == 3:
        goto(xcor()+25,ycor()+75)
    if i == 4:
        goto(xcor()+75,ycor()+75)
    if i == 5:
        goto(xcor()+125,ycor()+75)
    if i == 6:
        goto(xcor()+25,ycor()+25)
    if i == 7:
        goto(xcor()+75,ycor()+25)
    if i == 8:
        goto(xcor()+125,ycor()+25)
    goto(xcor()+5,ycor()+5)
    for s in range(2):
        down()
        goto(xcor()+40,ycor()+40)
        up()
        goto(xcor(),ycor()-40)
        down()
        goto(xcor()-40,ycor()+40)
        up()
        goto(xcor(),ycor()-40)
        pensize(3)
        pencolor("red")
    goto(400, 400)

def PrintCircle(s, i):
    title("Loading...")
    Beep(500,50)
    up()
    pensize(5)
    color("black")
    speed(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    if s == 0:
        goto(-300,100)
    if s == 1:
        goto(-100,100)
    if s == 2:
        goto(100,100)
    if s == 3:
        goto(-300,-100)
    if s == 4:
        goto(-100,-100)
    if s == 5:
        goto(100,-100)
    if s == 6:
        goto(-300,-300)
    if s == 7:
        goto(-100,-300)
    if s == 8:
        goto(100,-300)
    if i == 0:
        goto(xcor()+25,ycor()+125)
    if i == 1:
        goto(xcor()+75,ycor()+125)
    if i == 2:
        goto(xcor()+125,ycor()+125)
    if i == 3:
        goto(xcor()+25,ycor()+75)
    if i == 4:
        goto(xcor()+75,ycor()+75)
    if i == 5:
        goto(xcor()+125,ycor()+75)
    if i == 6:
        goto(xcor()+25,ycor()+25)
    if i == 7:
        goto(xcor()+75,ycor()+25)
    if i == 8:
        goto(xcor()+125,ycor()+25)
    goto(xcor()+25,ycor()+5)
    for s in range(2):
        down()
        circle(20)
        up()
        pensize(3)
        pencolor("blue")
    goto(400, 400)

def PrintBigCross(s):
    title("Loading...")
    up()
    pensize(15)
    color("black")
    if s == 0:
        goto(-300,100)
    if s == 1:
        goto(-100,100)
    if s == 2:
        goto(100,100)
    if s == 3:
        goto(-300,-100)
    if s == 4:
        goto(-100,-100)
    if s == 5:
        goto(100,-100)
    if s == 6:
        goto(-300,-300)
    if s == 7:
        goto(-100,-300)
    if s == 8:
        goto(100,-300)
    goto(xcor()+33,ycor()+33)
    for i in range(2):
        down()
        goto(xcor()+134,ycor()+134)
        up()
        goto(xcor(),ycor()-134)
        down()
        goto(xcor()-134,ycor()+134)
        up()
        goto(xcor(),ycor()-134)
        pencolor("red")
        pensize(9)
    up()

def PrintBigCircle(s):
    title("Loading...")
    up()
    pensize(15)
    color("black")
    if s == 0:
        goto(-300,100)
    if s == 1:
        goto(-100,100)
    if s == 2:
        goto(100,100)
    if s == 3:
        goto(-300,-100)
    if s == 4:
        goto(-100,-100)
    if s == 5:
        goto(100,-100)
    if s == 6:
        goto(-300,-300)
    if s == 7:
        goto(-100,-300)
    if s == 8:
        goto(100,-300)
    goto(xcor()+100,ycor()+30)
    down()
    for i in range(2):
        circle(70)
        pencolor("blue")
        pensize(9)
    up()

# Функции нацеленные на исплнение

def SmallCellsWinCheck(i):
    if cells[i][0] == 1 and cells[i][3] == 1 and cells[i][6] == 1:
        cells[i] = xcell
        PrintBigCross(i)
    elif cells[i][1] == 1 and cells[i][4] == 1 and cells[i][7] == 1:
        cells[i] = xcell
        PrintBigCross(i)
    elif cells[i][2] == 1 and cells[i][5] == 1 and cells[i][8] == 1:
        cells[i] = xcell
        PrintBigCross(i)
    elif cells[i][0] == 1 and cells[i][1] == 1 and cells[i][2] == 1:
        cells[i] = xcell
        PrintBigCross(i)
    elif cells[i][3] == 1 and cells[i][4] == 1 and cells[i][5] == 1:
        cells[i] = xcell
        PrintBigCross(i)
    elif cells[i][6] == 1 and cells[i][7] == 1 and cells[i][8] == 1:
        cells[i] = xcell
        PrintBigCross(i)
    elif cells[i][0] == 1 and cells[i][4] == 1 and cells[i][8] == 1:
        cells[i] = xcell
        PrintBigCross(i)
    elif cells[i][2] == 1 and cells[i][4] == 1 and cells[i][6] == 1:
        cells[i] = xcell
        PrintBigCross(i)

    if cells[i][0] == 2 and cells[i][3] == 2 and cells[i][6] == 2:
        cells[i] = ocell
        PrintBigCircle(i)
    elif cells[i][1] == 2 and cells[i][4] == 2 and cells[i][7] == 2:
        cells[i] = ocell
        PrintBigCircle(i)
    elif cells[i][2] == 2 and cells[i][5] == 2 and cells[i][8] == 2:
        cells[i] = ocell
        PrintBigCircle(i)
    elif cells[i][0] == 2 and cells[i][1] == 2 and cells[i][2] == 2:
        cells[i] = ocell
        PrintBigCircle(i)
    elif cells[i][3] == 2 and cells[i][4] == 2 and cells[i][5] == 2:
        cells[i] = ocell
        PrintBigCircle(i)
    elif cells[i][6] == 2 and cells[i][7] == 2 and cells[i][8] == 2:
        cells[i] = ocell
        PrintBigCircle(i)
    elif cells[i][0] == 2 and cells[i][4] == 2 and cells[i][8] == 2:
        cells[i] = ocell
        PrintBigCircle(i)
    elif cells[i][2] == 2 and cells[i][4] == 2 and cells[i][6] == 2:
        cells[i] = ocell
        PrintBigCircle(i)

def OWIN(i):
    for s in range(1,10):
        clear_select(s)
    title("Игрок 0 Выйграл, Нажмите что бы выйти")
    exitonclick()

def XWIN(i):
    for s in range(1,10):
        clear_select(s)
    title("Игрок X Выйграл, Нажмите что бы выйти")
    exitonclick()

def DRAW():
    for s in range(1,10):
        clear_select(s)
    title("Ничья, Нажмите что бы выйти")
    exitonclick()

def WinCheck():
    for i in range(0,9):
        SmallCellsWinCheck(i)
    if cells[0] == ocell and cells[3] == ocell and cells[6] == ocell:
        OWIN(1)
    elif cells[1] == ocell and cells[4] == ocell and cells[7] == ocell:
        OWIN(2)
    elif cells[2] == ocell and cells[5] == ocell and cells[8] == ocell:
        OWIN(3)
    elif cells[0] == ocell and cells[1] == ocell and cells[2] == ocell:
        OWIN(4)
    elif cells[3] == ocell and cells[4] == ocell and cells[5] == ocell:
        OWIN(5)
    elif cells[6] == ocell and cells[7] == ocell and cells[8] == ocell:
        OWIN(6)
    elif cells[0] == ocell and cells[4] == ocell and cells[8] == ocell:
        OWIN(7)
    elif cells[2] == ocell and cells[4] == ocell and cells[6] == ocell:
        OWIN(8)

    if cells[0] == xcell and cells[3] == xcell and cells[6] == xcell:
        XWIN(1)
    elif cells[1] == xcell and cells[4] == xcell and cells[7] == xcell:
        XWIN(2)
    elif cells[2] == xcell and cells[5] == xcell and cells[8] == xcell:
        XWIN(3)
    elif cells[0] == xcell and cells[1] == xcell and cells[2] == xcell:
        XWIN(4)
    elif cells[3] == xcell and cells[4] == xcell and cells[5] == xcell:
        XWIN(5)
    elif cells[6] == xcell and cells[7] == xcell and cells[8] == xcell:
        XWIN(6)
    elif cells[0] == xcell and cells[4] == xcell and cells[8] == xcell:
        XWIN(7)
    elif cells[2] == xcell and cells[4] == xcell and cells[6] == xcell:
        XWIN(8)

    if 0 not in cells[0] and 0 not in cells[1] and 0 not in cells[2] and 0 not in cells[3] and 0 not in cells[4] and 0 not in cells[5] and 0 not in cells[6] and 0 not in cells[7] and 0 not in cells[8]:
        DRAW()

def CheckSelectedBigCell(s): # Проверка содержимого выбранной большой клетки
    global big_selected_cell, player
    if cells[s] == xcell or cells[s] == ocell:
        big_selected_cell = None
    elif 0 not in cells[s]:
        big_selected_cell = None
    else:
        Beep(500,50)
        PrintSelect()
        Beep(250,50)
        if player == 0:
            title("[X] Выберите маленькую клетку")
        else:
            title("[0] Выберите маленькую клетку")

def SelectBigCell(x,y): # Выбор большой клетки
    global big_selected_cell

    check = 1

    if x > -300 and x < -100 and y > 100 and y < 300:
        big_selected_cell = 0
    elif x > -100 and x < 100 and y > 100 and y < 300:
        big_selected_cell = 1
    elif x > 100 and x < 300 and y > 100 and y < 300:
        big_selected_cell = 2
    elif x > -300 and x < -100 and y > -100 and y < 100:
        big_selected_cell = 3
    elif x > -100 and x < 100 and y > -100 and y < 100:
        big_selected_cell = 4
    elif x > 100 and x < 300 and y > -100 and y < 100:
        big_selected_cell = 5
    elif x > -300 and x < -100 and y > -300 and y < -100:
        big_selected_cell = 6
    elif x > -100 and x < 100 and y > -300 and y < -100:
        big_selected_cell = 7
    elif x > 100 and x < 300 and y > -300 and y < -100:
        big_selected_cell = 8
    else:
        check = 0
    if check != 0:
        CheckSelectedBigCell(big_selected_cell)

def NextBigCell():
    global big_selected_cell, small_selected_cell, cellsm, player
    big_selected_cell = small_selected_cell
    if cells[big_selected_cell] == xcell or cells[big_selected_cell] == ocell:
        big_selected_cell = None
        for i in range(1,10):
            clear_select(i)
    elif 0 not in cells[big_selected_cell]:
        big_selected_cell = None
        for i in range(1,10):
            clear_select(i)
    else:
        PrintSelect()

    if player == 1:
        player = 0
        Beep(250,50)
        title("[X] Выберите маленькую клетку")
        if big_selected_cell == None:
            title("[X] Выберите большую клетку")
    else:
        player = 1
        Beep(250,50)
        title("[0] Выберите маленькую клетку")
        if big_selected_cell == None:
            title("[0] Выберите большую клетку")

def CheckSelectedSmallCell(): # Проверка содержимого выбранной маленькой клетки
    global small_selected_cell, cells, player
    if cells[big_selected_cell][small_selected_cell] == 0:
        if player == 0:
            cells[big_selected_cell][small_selected_cell] = 1
            PrintCross(big_selected_cell,small_selected_cell)
        if player == 1:
            cells[big_selected_cell][small_selected_cell] = 2
            PrintCircle(big_selected_cell,small_selected_cell)
        WinCheck()
        NextBigCell()
    else:
        pass

def SelectSmallCell(x,y): # Выбор маленькой клетки
    global big_selected_cell, small_selected_cell
    if big_selected_cell == 0:
        x += 200
        y -= 200
    if big_selected_cell == 1:
        y -= 200
    if big_selected_cell == 2:
        x -= 200
        y -= 200
    if big_selected_cell == 3:
        x += 200
    if big_selected_cell == 5:
        x -= 200
    if big_selected_cell == 6:
        x += 200
        y += 200
    if big_selected_cell == 7:
        y += 200
    if big_selected_cell == 8:
        x -= 200
        y += 200

    check = 1

    if x > -75 and x < -25 and y > 25 and y < 75:
        small_selected_cell = 0
    elif x > -25 and x < 25 and y > 25 and y < 75:
        small_selected_cell = 1
    elif x > 25 and x < 75 and y > 25 and y < 75:
        small_selected_cell = 2
    elif x > -75 and x < -25 and y > -25 and y < 25:
        small_selected_cell = 3
    elif x > -25 and x < 25 and y > -25 and y < 25:
        small_selected_cell = 4
    elif x > 25 and x < 75 and y > -25 and y < 25:
        small_selected_cell = 5
    elif x > -75 and x < -25 and y > -75 and y < -25:
        small_selected_cell = 6
    elif x > -25 and x < 25 and y > -75 and y < -25:
        small_selected_cell = 7
    elif x > 25 and x < 75 and y > -75 and y < -25:
        small_selected_cell = 8
    else:
        check = 0
    if check != 0:
        CheckSelectedSmallCell()

def XPlayer(x,y): # Ход игрока X
    if big_selected_cell == None:
        SelectBigCell(x,y)
    else:
        SelectSmallCell(x,y)

def OPlayer(x,y): # Ход игрока 0
    if big_selected_cell == None:
        SelectBigCell(x,y)
    else:
        SelectSmallCell(x,y)

def StartScreen(x,y):
    global status
    if x > -200 and x < 200 and y > -50 and y < 0:
        clear()
        up()
        goto(0,0)
        PrintCells()
        status = 1
        title("[X] Выберите большую клетку")

def Main(x, y): # Основная функция
    global player, loading, status
    if status == 0:
        if loading == 0:
            loading = 1
            StartScreen(x,y)
            loading = 0
        else:
            pass
    elif status == 1:
        if loading == 0:
            loading = 1
            if player == 0:
                XPlayer(x,y)
            else:
                OPlayer(x,y)
            loading = 0
        else:
            pass

# Основной код

player = 0
PrintStartScreen()
Beep(250,50)

screen.onscreenclick(Main)

mainloop()