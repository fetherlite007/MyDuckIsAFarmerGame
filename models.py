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
    
class World:
    BUY_STATE = 0
    HIT_BOX = 50
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.me = Me(self, 125, 125)
        self.vega = VegA(self, 125, 25)
 
    def animate(self, delta):
        self.me.animate(delta)
 
        if self.me.hit(self.vega, 0) and self.me.MONEY >= 50 and self.BUY_STATE == 1:
            self.me.MONEY -= 50
            self.me.VEGA_COUNT += 1
            print (self.me.VEGA_COUNT)
            self.BUY_STATE=0

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
            self.BUY_STATE = 1
            
            
            
class Me(Model):
    d=1
    SPEED = 0
    MONEY = 100
    VEGA_COUNT = 0
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
  
 
    def animate(self, delta):
    
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

        
class VegA(Model):
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

    
