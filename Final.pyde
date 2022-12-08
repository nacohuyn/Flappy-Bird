# Nathan Huynh
# Final Project: Flappy Bird Remake
# Press Space to jump and "R" to reset the game


go = 'GAME OVER!!!'
walls = []
startTime = 0

def setup():
    global bird, walls
    size(800, 500)
    bird = Bird()
    walls.append(Wall())

def draw():
    global bird, go, walls
    background(152, 253, 240)
    
    #timer function
    pressTime = millis() - startTime
    millisString = str(pressTime/1000) + ":" + str((pressTime/100) - (pressTime/1000) * 10) + ":" + nf(pressTime % 100, 2)
    text(millisString, width/8, height/4)
    textSize(60)

    #generated walls
    if walls[len(walls) - 1].pos_.x + walls[len(walls) - 1].xGap <= width:
        walls.append(Wall())

    for i in range(len(walls) - 1, -1, -1): #collision condition
        if walls[i].pos_.x <= bird.pos.x <= (walls[i].pos_.x + walls[i].width_) and (0 < bird.pos.y < walls[i].upH or (height - 15 - walls[i].downH) < bird.pos.y < height):
            bird.gameOver = True

        if not walls[i].terminate:
            walls[i].render()
        else:
            walls.pop(i)

    if not bird.gameOver:
        bird.render()
    else: #the game over screen
        textSize(60)
        fill(255, 50, 50)
        text(go, (width - len(go) * 25) / 2, height / 2)
        bird.render()
        noLoop()


def keyPressed():
    global bird, walls, startTime
    if key == " ": #jumping mechanic
        bird.vel.set(0, -8)
    elif key == "r" or key == "R": #restarting key
        bird = Bird()
        walls = []
        walls.append(Wall())
        loop()
        startTime = 0
        
class Bird: #class to define the bird object
    def __init__(self):
        self.pos = PVector(100, height / 2)
        self.vel = PVector(0, 0)
        self.gravity = PVector(0, 0.5)
        self.dia = 40
        self.gameOver = False

    def update(self):
        self.vel.add(self.gravity)
        if 0 < self.pos.y < height:
            self.pos.add(self.vel)
        else:
            self.gameOver = True
            self.pos.sub(self.vel)

    def render(self):
        if not self.gameOver:
            self.update()
            fill(255, 100, 0)
            noStroke()
            ellipse(self.pos.x, self.pos.y, self.dia, self.dia)
        else:
            fill(255, 100, 0)
            noStroke()
            ellipse(self.pos.x, self.pos.y, self.dia, self.dia)
            
class Wall: #class to define the wall object
    def __init__(self):
        self.pos_ = PVector(width, 0)
        self.width_ = 50
        self.yGap = 100
        self.xGap = 200
        self.upH = int(random(50, height - self.yGap))
        self.downH = height - (self.yGap + self.upH)
        self.vel = PVector(-2, 0)
        self.terminate = False

    def update(self):
        self.pos_.add(self.vel)

    def render(self):
        self.update()
        if self.pos_.x > 0 - self.width_:
            fill(33, 248, 87)
            stroke(0, 150, 0)
            strokeWeight(2)
            rect(self.pos_.x, self.pos_.y, self.width_, self.upH)
            rect(self.pos_.x, self.upH + self.yGap, self.width_, self.downH)
        else:
            self.terminate = True
