import turtle as tu

blp = ['img/bp.png','img/br.png','img/bn.png','img/bb.png','img/bq.png','img/bk.png']
whp = ['./img/wp','./img/wr','./img/wh','./img/wb','./img/wq','./img/wk']

#
#
#
#   https://www.hackerearth.com/practice/notes/extracting-pixel-values-of-an-image-in-python/
#
#
#



board = []
ws = 600
scr = tu.Screen()
wcol = '#ebecd0'
bcol = '#779556'
bg = 'black'

##turtle.shape(image)

def createBoard():
    global board,blp,whp
    for j in range(8):
        x = []
        for i in range(8):
            x.append("")
        board.append(x)
##    for i in blp:
##        print(i)
##        scr.addshape(i)
##    for j in whp:
##        scr.addshape(i)

    

def click(i,j):
    global ws
    px = ws//8
    i = i//px
    j = j//px
    j += 1
    j *= -1
    if not(i<8 and i>=0):
        return
    if not(j<8 and j>=0):
        return
    j = int(abs(j))
    i = int(abs(i))
    draw(i,j)

def qu():
    tu.bye()
    input()
    quit()

def draw(x,y):
    tu.clear()
    drawBoard(scr)
    print("redrawn")
    drawPieces(scr)
    tu.update()


def drawBoard(scr):
    global wcol,bcol,ws
    for i in range(8):
        for j in range(0,-8,-1):
            if (i%2 == j%2):
                tu.color(wcol)
            else:
                tu.color(bcol)
            px = ws//8
            dsq(i*px,j*px)


def drawPieces(scr):
    global board
    print(board)


def dsq(x,y,s = ws//8):
##    print('i ran',x,y,tu.color(),sep = '   ')
    global ws
    tu.penup()
    tu.goto(x,y)
    tu.pendown()
    tu.begin_fill()
    tu.settiltangle(0)
    tu.goto(x+s,y)
    tu.goto(x+s,y-s)
    tu.goto(x,y-s)
    tu.goto(x,y)
##    for i in range(4):
##        tu.fd(s)
##        tu.rt(90)
##        tu.tilt(0)
    tu.end_fill()
    tu.penup()



class Piece:
    isWhite = True
    path = ''
    typ = 0
    def __init__(self,isWhite = True,typ = 0):
        self.isWhite = isWhite
        self.typ = typ
        print('i was initialised')


##tr = turtle.Turtle()
##wn = turtle.Screen()
##wn.addshape('python2.gif')
##tr.shape('python2.gif')


















##
##class Block:
##    i = 0
##    j = 0
##    loc = []
##    def __init__(self):
##        self.loc.append((0,0))
##        self.i = randint(0,windowWidthInBlocks-1)
##        self.j = 0
##        pass
##    def assign_to(self,l):
##        for k in self.loc:
##            l[ k[0] + self.j  ][  k[1] + self.i ] = 1 
##    def get_bottom(self):
##        tmp = list(min(self.loc,key = lambda x:x[1]))
##        tmp[0] += self.i
##        tmp[1] += self.j
##        return tmp
##    def get_top(self):
##        tmp = list(max(self.loc,key = lambda x:x[1]))
##        tmp[0] += self.i
##        tmp[1] += self.j
##        return tmp
##    def get_right(self):
##        tmp = list(max(self.loc,key = lambda x:x[0]))
##        tmp[0] += self.i
##        tmp[1] += self.j
##        return tmp
##    def get_left(self):
##        tmp = list(min(self.loc,key = lambda x:x[0]))
##        tmp[0] += self.i
##        tmp[1] += self.j
##        return tmp
##    
##    def rotate(self):
##        pass
##    def movelt(self,l):
##        if self.checkcol(l,(0,-1)):
##            return Block()
##        if self.get_left()[0] > 0:
##            self.i -= 1
##        return self
##    def movert(self,l):
##        if self.checkcol(l,(0,1)):
##            return Block()
##        if self.get_right()[0] < 9:
##            self.i += 1
##        return self
##    def movedn(self,l) -> Block:
##        global wh,bls
##        if self.checkcol(l,(1,0)):
##            return Block()
##        if self.get_bottom()[0] + 1 < wh//bls:
##            self.j += 1
##        return self
##    def set(self):
##        pass
##    def checkcol(self,l,d=(0,0)):
##        for k in self.loc:
##            if k[1]+self.j+d[0] >= len(l):
##                self.assign_to(l)
##                return True
##            elif k[0]+self.i+d[1] >= len(l[0]):
##                return False
##            elif l[k[1]+self.j+d[0]][k[0]+self.i+d[1]]:
##                self.assign_to(l)
##                return True
##        return False


##    
##def down():
##    global bl
##    bl = bl.movedn(l)
##def rotate():
##    pass
##def left():
##    global bl,l
##    bl = bl.movelt(l)
##def right():
##    global bl,l
##    bl = bl.movert(l)
