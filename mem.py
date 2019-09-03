import turtle
import time
class mem:
    def __init__(self,x):
        self.free=x
        self.allo=0
    def update(self,x):
        self.allo+=x
        self.free-=x
def drawbk(x):
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(x)
def drawmem(ls):
    turtle.color('black')
    turtle.setposition(100,200)
    for i in range(len(ls)):
        drawbk(ls[i].free+ls[i].allo)
        if ls[i].allo!=0:
            turtle.backward(ls[i].allo+ls[i].free)
            turtle.color('red','lightgreen')
            turtle.begin_fill()
            drawbk(ls[i].allo)
            turtle.end_fill()
            turtle.color('black')
            turtle.forward(ls[i].free)
ls=[]
n=int(input('Enter the number of blocks: '))
for i in range(n):
    ls.append(mem(int(input('Enter the size: '))))
pro=[int(i) for i in input('Enter the size of process : ').split()]
turtle.setposition(100,200)
turtle.clear()
# turtle.hideturtle()
turtle.right(90)
turtle.speed(1)
# ls[1].update(10)
for i in range(len(pro)):
    for j in range(len(ls)):
        drawmem(ls)
        time.sleep(5)
        if pro[i]<=ls[j].free:
            ls[j].update(pro[i])
            turtle.clear()
            break
        turtle.clear()
drawmem(ls)
time.sleep(5)
