class Lutador():
    hp = 100
    mp = 0
    x = 0
    y = 0
    x0 = 0
    y0 = 0
    vx = 0
    vy = 0
    angle = 60
    time = 0
    def __init__(self, hp, mp, x, y):
        self.hp = hp
        self.mp = mp
        self.x = x
        self.y = y           
            
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y    
        
    def walk_right(self):
        self.vx = 10
     
    def walk_left(self):
        self.vx = -10
        
    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
    
    def jump(self, curr_time):
        self.vx = 10
        self.x = self.vx * curr_time
        
        
