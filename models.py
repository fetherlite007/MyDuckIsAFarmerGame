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

class VegC(Model):
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

class VegD(Model):
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

class VegE(Model):
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

class Shovel(Model):
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

class WateringCan(Model):
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        
class Trash(Model):
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

class Shop(Model):
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

class Soil(Model):

    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        self.x = x
        self.y = y
        self.t1 = 10
        self.t2 = 15
        self.gt = 5
        self.STATE = 'none'
        self.timer_on = False
        self.timer2_on = False
        self.grow_time_on = False
        self.grow_time2_on = False
        self.plant_dead = False
        self.watered = False
        self.grown = False
        self.collectable = False
        self.timer = self.t1
        self.timer2 = self.t2
        self.grow_time = self.gt
        self.grow_time2 = self.gt
        
        

class World:
    
    def __init__(self, width, height):
        
        self.width = width
        self.height = height

        self.COST_A = 50
        self.COST_B = 100
        self.COST_C = 200
        self.COST_D = 300
        self.COST_E = 500
        self.SELL_A = 75
        self.SELL_B = 150
        self.SELL_C = 275
        self.SELL_D = 400
        self.SELL_E = 625
        self.BUY_STATE = 0
        self.HIT_BOX = 50
        self.total_time = 0
        self.soils = []
        
        
        self.me = Me(self, 75, 525)
        self.vega = VegA(self, 75, 575)
        self.vegb = VegB(self, 175, 575)
        self.vegc = VegC(self, 275, 575)
        self.vegd = VegD(self, 375, 575)
        self.vege = VegE(self, 475, 575)
        self.shovel = Shovel(self, 875, 475)
        self.wateringcan = WateringCan(self, 875, 375)
        self.trash = Trash(self, 875, 275)
        self.shop = Shop(self, 875, 175)
        
        for i in range(5):
            for j in range(3):
                self.soils.append(Soil(self, 125+(150*i), 175+(150*j)))
            
        
    def animate(self, delta_time):
        self.me.animate(delta_time)
        self.total_time += delta_time 
 
        if self.me.hit(self.vega, 0) and self.me.MONEY >= self.COST_A and self.BUY_STATE == 1 and self.me.STATE == 'none':
            self.me.MONEY -= self.COST_A
            self.BUY_STATE=0
            self.me.STATE = 'a'

        if self.me.hit(self.vegb, 0) and self.me.MONEY >= self.COST_B and self.BUY_STATE == 1 and self.me.STATE == 'none':
            self.me.MONEY -= self.COST_B
            self.BUY_STATE=0
            self.me.STATE = 'b'

        if self.me.hit(self.vegc, 0) and self.me.MONEY >= self.COST_C and self.BUY_STATE == 1 and self.me.STATE == 'none':
            self.me.MONEY -= self.COST_C
            self.BUY_STATE=0
            self.me.STATE = 'c'

        if self.me.hit(self.vegd, 0) and self.me.MONEY >= self.COST_D and self.BUY_STATE == 1 and self.me.STATE == 'none':
            self.me.MONEY -= self.COST_D
            self.BUY_STATE=0
            self.me.STATE = 'd'

        if self.me.hit(self.vege, 0) and self.me.MONEY >= self.COST_E and self.BUY_STATE == 1 and self.me.STATE == 'none':
            self.me.MONEY -= self.COST_E
            self.BUY_STATE=0
            self.me.STATE = 'e'
            
        for s in self.soils:
            if self.me.hit(s, 0) and self.BUY_STATE == 1 and self.me.STATE == 'none' and s.collectable == True:
                    if s.STATE == 'a3':
                        self.me.STATE = 'a2'
                    elif s.STATE == 'b3':
                        self.me.STATE = 'b2'
                    elif s.STATE == 'c3':
                        self.me.STATE = 'c2'
                    elif s.STATE == 'd3':
                        self.me.STATE = 'd2'
                    elif s.STATE == 'e3':
                        self.me.STATE = 'e2'
                    s.STATE = 'none'
                    s.timer_on = False
                    s.timer2_on = False
                    s.plant_dead = False
                    s.watered = False
                    s.grown = False
                    s.grow_time_on = False
                    s.grow_time2_on = False
                    s.collectable = False
                    s.timer = s.t1
                    s.timer2 = s.t2
                    s.grow_time = s.gt
                    s.grow_time2 = s.gt
                    self.BUY_STATE=0
                    
            if self.me.hit(s, 0) and self.me.STATE != 'none' and self.BUY_STATE == 1:
                if self.me.STATE == 'a' and s.STATE == 'none' and s.plant_dead == False and s.watered == False:
                    s.STATE = 'a'
                    self.me.STATE = 'none'
                    self.BUY_STATE=0
                    s.timer_on = True
                    
                if self.me.STATE == 'b' and s.STATE == 'none' and s.plant_dead == False and s.watered == False:
                    s.STATE = 'b'
                    self.me.STATE = 'none'
                    self.BUY_STATE=0
                    s.timer_on = True

                if self.me.STATE == 'c' and s.STATE == 'none' and s.plant_dead == False and s.watered == False:
                    s.STATE = 'c'
                    self.me.STATE = 'none'
                    self.BUY_STATE=0
                    s.timer_on = True

                if self.me.STATE == 'd' and s.STATE == 'none' and s.plant_dead == False and s.watered == False:
                    s.STATE = 'd'
                    self.me.STATE = 'none'
                    self.BUY_STATE=0
                    s.timer_on = True

                if self.me.STATE == 'e' and s.STATE == 'none' and s.plant_dead == False and s.watered == False:
                    s.STATE = 'e'
                    self.me.STATE = 'none'
                    self.BUY_STATE=0
                    s.timer_on = True

                if self.me.STATE == 's' and s.STATE != 'none':
                    s.STATE = 'none'
                    s.timer_on = False
                    s.timer2_on = False
                    s.plant_dead = False
                    s.watered = False
                    s.grown = False
                    s.grow_time_on = False
                    s.grow_time2_on = False
                    s.collectable = False
                    s.timer = s.t1
                    s.timer2 = s.t2
                    s.grow_time = s.gt
                    s.grow_time2 = s.gt
                    self.BUY_STATE=0
                    

                if self.me.STATE == 'w' and s.STATE != 'none' and s.grow_time == s.gt:
                    if s.plant_dead != True:
                        s.timer_on = False
                        s.watered == True
                        s.timer = s.t1
                        if s.grown == False:
                            s.grow_time_on = True
                        if s.grown == True:
                            s.timer2_on = False
                            s.timer2 = s.t2
                            s.grow_time2_on = True
                    self.BUY_STATE=0
                    
            if s.timer > -0.2 and s.timer < 0.2:
                s.timer_on = False
                s.timer = s.t1
                s.timer = s.t1
                s.timer = s.t1
                s.plant_dead = True
                s.watered == False
                s.grown = False

            if s.timer2 > -0.2 and s.timer2 < 0.2:
                s.timer2_on = False
                s.timer2 = s.t2
                s.timer2 = s.t2
                s.timer2 = s.t2
                s.plant_dead = True
                s.watered == False
                s.grown = False

            if s.grow_time > -0.2 and s.grow_time < 0.2:
                s.grow_time_on = False
                s.grow_time = s.gt
                s.grow_time = s.gt
                s.grow_time = s.gt
                s.watered = False
                s.timer2_on = True
                s.grown = True
                if s.STATE == 'a':
                    s.STATE = 'a2'
                elif s.STATE == 'b':
                    s.STATE = 'b2'
                elif s.STATE == 'c':
                    s.STATE = 'c2'
                elif s.STATE == 'd':
                    s.STATE = 'd2'
                elif s.STATE == 'e':
                    s.STATE = 'e2'

            if s.grow_time2 > -0.2 and s.grow_time2 < 0.2:
                s.grow_time2_on = False
                s.grow_time2 = s.gt
                s.grow_time2 = s.gt
                s.grow_time2 = s.gt
                s.watered = False
                s.collectable = True
                if s.STATE == 'a2':
                    s.STATE = 'a3'
                elif s.STATE == 'b2':
                    s.STATE = 'b3'
                elif s.STATE == 'c2':
                    s.STATE = 'c3'
                elif s.STATE == 'd2':
                    s.STATE = 'd3'
                elif s.STATE == 'e2':
                    s.STATE = 'e3'

            if s.timer_on == True:
                s.timer -= delta_time

            if s.timer2_on == True:
                s.timer2 -= delta_time
                
            if s.grow_time_on == True:
                s.grow_time -= delta_time

            if s.grow_time2_on == True:
                s.grow_time2 -= delta_time               
                
        if self.me.hit(self.shovel, 0) and self.BUY_STATE == 1 and self.me.STATE == 'none':
            self.me.STATE = 's'
            self.BUY_STATE=0

        if self.me.hit(self.shovel, 0) and self.BUY_STATE == 1 and self.me.STATE == 's':
            self.me.STATE = 'none'
            self.BUY_STATE=0

        if self.me.hit(self.wateringcan, 0) and self.BUY_STATE == 1 and self.me.STATE == 'none':
            self.me.STATE = 'w'
            self.BUY_STATE=0

        if self.me.hit(self.wateringcan, 0) and self.BUY_STATE == 1 and self.me.STATE == 'w':
            self.me.STATE = 'none'
            self.BUY_STATE=0

        if self.me.hit(self.trash, 0) and self.BUY_STATE == 1 and self.me.STATE != 's' and self.me.STATE != 'w':
            self.me.STATE = 'none'
            self.BUY_STATE = 0

        if self.me.hit(self.shop, 0) and self.BUY_STATE == 1 and self.me.STATE != 's' and self.me.STATE != 'w':
            if self.me.STATE == 'a2':
                self.me.MONEY += self.SELL_A
            elif self.me.STATE == 'b2':
                self.me.MONEY += self.SELL_B
            elif self.me.STATE == 'c2':
                self.me.MONEY += self.SELL_C
            elif self.me.STATE == 'd2':
                self.me.MONEY += self.SELL_D
            elif self.me.STATE == 'e2':
                self.me.MONEY += self.SELL_E
            self.me.STATE = 'none'
            self.BUY_STATE = 0

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.me.switch_direction_to_up()
            self.me.SPEED = self.HIT_BOX
            self.BUY_STATE = 0
        elif key == arcade.key.DOWN:
            self.me.switch_direction_to_down()
            self.me.SPEED = self.HIT_BOX
            self.BUY_STATE = 0
        elif key == arcade.key.RIGHT:
            self.me.switch_direction_to_right()
            self.me.SPEED = self.HIT_BOX
            self.BUY_STATE = 0
        elif key == arcade.key.LEFT:
            self.me.switch_direction_to_left()
            self.me.SPEED = self.HIT_BOX
            self.BUY_STATE = 0
        
    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.BUY_STATE = 1
            
            
class Me(Model):
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

        self.d=1
        self.SPEED = 0
        self.MONEY = 75
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

