import arcade
import arcade.key
from random import randint



class Model:
    
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        
    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)
        
class VegA(Model):
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

class VegB(Model):
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

class Shovel(Model):
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

class Trash(Model):
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

class Soil(Model):

    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        self.x = x
        self.y = y
        self.STATE = 'none'
        self.timer_on = False
        self.timer = 20
        

class World:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.BUY_STATE = 0
        self.E_STATE = 0
        self.X_STATE = 0
        self.HIT_BOX = 50
        self.total_time = 0
        self.soils = []
        
 
        self.me = Me(self, 125, 125)
        self.vega = VegA(self, 125, 25)
        self.vegb = VegB(self, 225, 25)
        self.shovel = Shovel(self, 225, 125)
        self.trash = Trash(self, 325, 125)
        
        for i in range(2):
            self.soils.append(Soil(self, 225+(100*i), 225))
            
        
    def animate(self, delta_time):
        self.me.animate(delta_time)
        self.total_time += delta_time 
 
        if self.me.hit(self.vega, 0) and self.me.MONEY >= 10 and self.BUY_STATE == 1 and self.me.STATE == 'none':
            self.me.MONEY -= 10
            self.BUY_STATE=0
            self.me.STATE = 'a'

        if self.me.hit(self.vegb, 0) and self.me.MONEY >= 10 and self.BUY_STATE == 1 and self.me.STATE == 'none':
            self.me.MONEY -= 10
            self.BUY_STATE=0
            self.me.STATE = 'b'
            
        for s in self.soils:
            if self.me.hit(s, 0) and self.me.STATE != 'none' and self.BUY_STATE == 1:
                if self.me.STATE == 'a' and s.STATE == 'none':
                    s.STATE = 'a'
                    self.me.STATE = 'none'
                    self.BUY_STATE=0
                    s.timer_on = True
                    
                if self.me.STATE == 'b' and s.STATE == 'none':
                    s.STATE = 'b'
                    self.me.STATE = 'none'
                    self.BUY_STATE=0
                    s.timer_on = True

                if self.me.STATE == 's' and s.STATE != 'none':
                    s.STATE = 'none'
                    s.timer_on = False
                    s.timer = 20
                    self.BUY_STATE=0
                    
            if s.timer > -0.2 and s.timer < 0.2:
                s.timer_on = False
                print(s.timer)
                s.timer = 20
                s.timer = 20
                s.timer = 20
                print(s.timer)
                
            if s.timer_on == True:
                s.timer -= delta_time

        if self.me.hit(self.shovel, 0) and self.E_STATE == 1 and self.me.STATE == 'none':
            self.me.STATE = 's'
            self.E_STATE=0

        if self.me.hit(self.shovel, 0) and self.E_STATE == 1 and self.me.STATE == 's':
            self.me.STATE = 'none'
            self.E_STATE=0

        if self.me.hit(self.trash, 0) and self.X_STATE == 1 and self.me.STATE != 's':
            self.me.STATE = 'none'
            self.X_STATE=0

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.me.switch_direction_to_up()
            self.me.SPEED = self.HIT_BOX
        elif key == arcade.key.DOWN:
            self.me.switch_direction_to_down()
            self.me.SPEED = self.HIT_BOX
        elif key == arcade.key.RIGHT:
            self.me.switch_direction_to_right()
            self.me.SPEED = self.HIT_BOX
        elif key == arcade.key.LEFT:
            self.me.switch_direction_to_left()
            self.me.SPEED = self.HIT_BOX
        
    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.X_STATE = 0
            self.E_STATE = 0
            self.BUY_STATE = 1
        if key == arcade.key.C:
            self.X_STATE = 0
            self.E_STATE = 1
            self.BUY_STATE = 0
        if key == arcade.key.X:
            self.X_STATE = 1
            self.E_STATE = 0
            self.BUY_STATE = 0
            
            
class Me(Model):
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

        self.d=1
        self.SPEED = 0
        self.MONEY = 100
        self.STATE = 'none'
  
 
    def animate(self, delta_time):
    
        if self.d == 1:          
            if self.y > self.world.height-25:
                self.y = self.world.height-25
            self.y += self.SPEED
            self.SPEED = 0
        elif self.d == 2:
            if self.y < 25:
                self.y = 25
            self.y -= self.SPEED
            self.SPEED = 0
        elif self.d == 3:
            if self.x > self.world.width-25:
                self.x = self.world.width-25
            self.x += self.SPEED
            self.SPEED = 0
        elif self.d == 4:
            if self.x < 25:
                self.x = 25
            self.x -= self.SPEED
            self.SPEED = 0

    def switch_direction_to_up(self):
        self.d = 1

    def switch_direction_to_down(self):
        self.d = 2

    def switch_direction_to_right(self):
        self.d = 3

    def switch_direction_to_left(self):
        self.d = 4

