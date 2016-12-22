import arcade
import arcade.key

from models import World, Me

SCREEN_WIDTH = 850
SCREEN_HEIGHT = 600

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            
    def draw(self):
        self.sync_with_model()
        super().draw()
        
class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        
        self.setup(width,height)
        
    def setup(self, width, height):
        arcade.set_background_color(arcade.color.GREEN)
        self.world = World(width, height)

        self.me_sprite = ModelSprite('images/Me.png',model=self.world.me)
        self.her_sprite = ModelSprite('images/Me.png',model=self.world.her)
        self.vega_sprite = ModelSprite('images/Orange.png',model=self.world.vega)
        self.vegb_sprite = ModelSprite('images/Banana.png',model=self.world.vegb)
        self.vegc_sprite = ModelSprite('images/Grape.png',model=self.world.vegc)
        self.vegd_sprite = ModelSprite('images/Watermelon.png',model=self.world.vegd)
        self.vege_sprite = ModelSprite('images/Strawberry.png',model=self.world.vege)
        self.shovel_sprite = ModelSprite('images/Shovel.png',model=self.world.shovel)
        self.trash_sprite = ModelSprite('images/Trash.png',model=self.world.trash)
        self.wateringcan_sprite = ModelSprite('images/WateringCan.png',model=self.world.wateringcan)
        self.shop_sprite = ModelSprite('images/Shop.png',model=self.world.shop)

        self.plant1_texture = arcade.load_texture('images/Plant1.png')
        self.plant2_texture = arcade.load_texture('images/Plant2.png')
        self.grass_texture = arcade.load_texture('images/Grass.png')
        self.vega_texture = arcade.load_texture('images/Orange.png')
        self.vegb_texture = arcade.load_texture('images/Banana.png')
        self.vegc_texture = arcade.load_texture('images/Grape.png')
        self.vegd_texture = arcade.load_texture('images/Watermelon.png')
        self.vege_texture = arcade.load_texture('images/Strawberry.png')
        self.soil_texture = arcade.load_texture('images/Soil.png')
        self.shovel_texture = arcade.load_texture('images/Shovel.png')
        self.wateringcan_texture = arcade.load_texture('images/WateringCan.png')
        self.deadplant_texture = arcade.load_texture('images/DeadPlant.png')
        self.ground_texture = arcade.load_texture('images/Ground.png')
        
    def draw_me_state(self):
        if self.world.me.STATE == 'a':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y+20, 10, 10,
                                              self.vega_texture)
            arcade.draw_texture_rectangle(380, 50, 75, 75,
                                              self.vega_texture)
        if self.world.me.STATE == 'a2':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y+20, 30, 30,
                                              self.vega_texture)
            arcade.draw_texture_rectangle(380, 50, 75, 75,
                                              self.vega_texture)
        if self.world.me.STATE == 'b':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y+20, 10, 10,
                                              self.vegb_texture)
            arcade.draw_texture_rectangle(380, 50, 75, 75,
                                              self.vegb_texture)
        if self.world.me.STATE == 'b2':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y+20, 30, 30,
                                              self.vegb_texture)
            arcade.draw_texture_rectangle(380, 50, 75, 75,
                                              self.vegb_texture)
        if self.world.me.STATE == 'c':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y+20, 10, 10,
                                              self.vegc_texture)
            arcade.draw_texture_rectangle(380, 50, 75, 75,
                                              self.vegc_texture)
        if self.world.me.STATE == 'c2':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y+20, 30, 30,
                                              self.vegc_texture)
            arcade.draw_texture_rectangle(380, 50, 75, 75,
                                              self.vegc_texture)
        if self.world.me.STATE == 'd':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y+20, 10, 10,
                                              self.vegd_texture)
            arcade.draw_texture_rectangle(380, 50, 75, 75,
                                              self.vegd_texture)
        if self.world.me.STATE == 'd2':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y+20, 30, 30,
                                              self.vegd_texture)
            arcade.draw_texture_rectangle(380, 50, 75, 75,
                                              self.vegd_texture)
        if self.world.me.STATE == 'e':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y+20, 10, 10,
                                              self.vege_texture)
            arcade.draw_texture_rectangle(380, 50, 75, 75,
                                              self.vege_texture)
        if self.world.me.STATE == 'e2':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y+20, 30, 30,
                                              self.vege_texture)
            arcade.draw_texture_rectangle(380, 50, 75, 75,
                                              self.vege_texture)
        if self.world.me.STATE == 's':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y+20, 20, 20,
                                              self.shovel_texture)
            arcade.draw_texture_rectangle(380, 50, 75, 75,
                                              self.shovel_texture)
        if self.world.me.STATE == 'w':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y+20, 20, 20,
                                              self.wateringcan_texture)
            arcade.draw_texture_rectangle(380, 50, 75, 75,
                                              self.wateringcan_texture)

    def draw_soils_state(self):
        for s in self.world.soils:
            arcade.draw_texture_rectangle(s.x, s.y, 50, 50,
                                              self.soil_texture)
            if s.plant_dead == True:
                s.watered = False
                arcade.draw_texture_rectangle(s.x, s.y, 15, 15,
                                              self.deadplant_texture)
                
            elif s.STATE == 'a':
                arcade.draw_texture_rectangle(s.x, s.y, 15, 15,
                                              self.plant1_texture)
            elif s.STATE == 'a2':
                arcade.draw_texture_rectangle(s.x, s.y, 20, 20,
                                              self.plant2_texture)
            elif s.STATE == 'a3':
                arcade.draw_texture_rectangle(s.x, s.y, 30, 30,
                                              self.vega_texture)
                
            elif s.STATE == 'b':
                arcade.draw_texture_rectangle(s.x, s.y, 15, 15,
                                              self.plant1_texture) 
            elif s.STATE == 'b2':
                arcade.draw_texture_rectangle(s.x, s.y, 20, 20,
                                              self.plant2_texture)    
            elif s.STATE == 'b3':
                arcade.draw_texture_rectangle(s.x, s.y, 30, 30,
                                              self.vegb_texture)

            elif s.STATE == 'c':
                arcade.draw_texture_rectangle(s.x, s.y, 15, 15,
                                              self.plant1_texture)
            elif s.STATE == 'c2':
                arcade.draw_texture_rectangle(s.x, s.y, 20, 20,
                                              self.plant2_texture)
            elif s.STATE == 'c3':
                arcade.draw_texture_rectangle(s.x, s.y, 30, 30,
                                              self.vegc_texture)

            elif s.STATE == 'd':
                arcade.draw_texture_rectangle(s.x, s.y, 15, 15,
                                              self.plant1_texture)
            elif s.STATE == 'd2':
                arcade.draw_texture_rectangle(s.x, s.y, 20, 20,
                                              self.plant2_texture)
            elif s.STATE == 'd3':
                arcade.draw_texture_rectangle(s.x, s.y, 30, 30,
                                              self.vegd_texture)

            elif s.STATE == 'e':
                arcade.draw_texture_rectangle(s.x, s.y, 15, 15,
                                              self.plant1_texture)
            elif s.STATE == 'e2':
                arcade.draw_texture_rectangle(s.x, s.y, 20, 20,
                                              self.plant2_texture)
            elif s.STATE == 'e3':
                arcade.draw_texture_rectangle(s.x, s.y, 30, 30,
                                              self.vege_texture)
            
            timer = s.timer
            if s.timer_on == True:
                seconds2 = int(timer) % 60
                output2 = "{:02d}".format(seconds2)
                arcade.draw_text(output2, s.x-5, s.y+25, arcade.color.WHITE, 10)

            timer2 = s.timer2
            if s.timer2_on == True:
                seconds3 = int(timer2) % 60
                output3 = "{:02d}".format(seconds3)
                arcade.draw_text(output3, s.x-5, s.y+25, arcade.color.WHITE, 10)
                
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(425, 325, 850, 650,
                                              self.grass_texture)
        arcade.draw_texture_rectangle(450, 575, 900, 50,
                                              self.ground_texture)
        arcade.draw_texture_rectangle(25, 325, 50, 450,
                                              self.ground_texture)
        arcade.draw_texture_rectangle(450, 50, 900, 100,
                                              self.ground_texture)
        self.draw_soils_state()
        self.shovel_sprite.draw()
        self.wateringcan_sprite.draw()
        self.trash_sprite.draw()
        self.vega_sprite.draw()
        self.vegb_sprite.draw()
        self.vegc_sprite.draw()
        self.vegd_sprite.draw()
        self.vege_sprite.draw()
        self.shop_sprite.draw()
        self.her_sprite.draw()
        self.me_sprite.draw()
        self.draw_me_state()
        minutes = int(self.world.total_time) // 60
        seconds = int(self.world.total_time) % 60
        money = int(self.world.me.MONEY)
        strawberry = int(self.world.me.STRAWBERRY_GIVEN)

        output = "Time: {:02d}:{:02d}".format(minutes, seconds)
        moneyShow = "Money: {:02d}" .format(money)
        output2 = "Current Equipment :"
        strawberryshow = "Strawberries Given: {:d}/3" .format(strawberry)
        arcade.draw_text("Cost: 50", 100, 585, arcade.color.WHITE, 10)
        arcade.draw_text("Cost: 100", 200, 585, arcade.color.WHITE, 10)
        arcade.draw_text("Cost: 200", 300, 585, arcade.color.WHITE, 10)
        arcade.draw_text("Cost: 300", 400, 585, arcade.color.WHITE, 10)
        arcade.draw_text("Cost: 500", 500, 585, arcade.color.WHITE, 10)
        arcade.draw_text("Sell: 75", 100, 555, arcade.color.WHITE, 10)
        arcade.draw_text("Sell: 150", 200, 555, arcade.color.WHITE, 10)
        arcade.draw_text("Sell: 275", 300, 555, arcade.color.WHITE, 10)
        arcade.draw_text("Sell: 400", 400, 555, arcade.color.WHITE, 10)
        arcade.draw_text("Sell: 625", 500, 555, arcade.color.WHITE, 10)
        
        arcade.draw_text(output, 560, 565, arcade.color.WHITE, 20)
        arcade.draw_text(moneyShow, 700, 565, arcade.color.WHITE, 20)
        arcade.draw_text(output2, 75, 40, arcade.color.WHITE, 20)
        arcade.draw_text(strawberryshow, 525, 40, arcade.color.WHITE, 20)
    
        if self.world.END_STATE == 1:
            arcade.draw_text("Game Over", 250, 450, arcade.color.WHITE, 30)
            arcade.draw_text("Press Space Bar to Restart", 250, 250, arcade.color.WHITE, 30)
            Eminutes = int(self.world.end_time) // 60
            Eseconds = int(self.world.end_time) % 60
            endtime = "Time Spent: {:02d}:{:02d}".format(Eminutes,Eseconds)
            arcade.draw_text(endtime, 250, 350, arcade.color.WHITE, 30)
        
    def animate(self, delta):
        if self.world.END_STATE == 0:
            self.world.animate(delta)
        
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
        
    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)
        if self.world.END_STATE == 1 and key == arcade.key.SPACE:
            self.setup(850, 600)

        
        
if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
