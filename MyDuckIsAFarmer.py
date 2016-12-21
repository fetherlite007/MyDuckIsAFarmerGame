import arcade
import arcade.key

from models import World, Me

SCREEN_WIDTH = 600
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
 
        arcade.set_background_color(arcade.color.GREEN)

        self.world = World(width, height)
        self.me_sprite = ModelSprite('images/Me.png',model=self.world.me)
        self.vega_sprite = ModelSprite('images/Orange.png',model=self.world.vega)
        self.vegb_sprite = ModelSprite('images/Banana.png',model=self.world.vegb)
        self.shovel_sprite = ModelSprite('images/Shovel.png',model=self.world.shovel)
        self.trash_sprite = ModelSprite('images/Trash.png',model=self.world.trash)
        self.wateringcan_sprite = ModelSprite('images/WateringCan.png',model=self.world.wateringcan)


        self.vega_texture = arcade.load_texture('images/Orange.png')
        self.vegb_texture = arcade.load_texture('images/Banana.png')
        self.soil_texture = arcade.load_texture('images/Soil.jpg')
        self.shovel_texture = arcade.load_texture('images/Shovel.png')
        self.wateringcan_texture = arcade.load_texture('images/WateringCan.png')
        self.deadplant_texture = arcade.load_texture('images/DeadPlant.png')

        
    def draw_me_state(self):
        if self.world.me.STATE == 'a':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y, 10, 10,
                                              self.vega_texture)
        if self.world.me.STATE == 'b':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y, 10, 10,
                                              self.vegb_texture)
        if self.world.me.STATE == 's':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y, 10, 10,
                                              self.shovel_texture)
        if self.world.me.STATE == 'w':
            arcade.draw_texture_rectangle(self.world.me.x, self.world.me.y, 10, 10,
                                              self.wateringcan_texture)

    def draw_soils_state(self):
        for s in self.world.soils:
            arcade.draw_texture_rectangle(s.x, s.y, 50, 50,
                                              self.soil_texture)
            if s.plant_dead == True:
                s.watered = False
                arcade.draw_texture_rectangle(s.x, s.y, 10, 10,
                                              self.deadplant_texture)
                
            elif s.STATE == 'a':
                arcade.draw_texture_rectangle(s.x, s.y, 10, 10,
                                              self.vega_texture)
                
            elif s.STATE == 'b':
                arcade.draw_texture_rectangle(s.x, s.y, 10, 10,
                                              self.vegb_texture)
                
            
            timer = s.timer
            if s.timer_on == True:
                minutes2 = int(timer) // 60
                seconds2 = int(timer) % 60
                output2 = "{:02d}:{:02d}".format(minutes2, seconds2)
                arcade.draw_text(output2, s.x-15, s.y+25, arcade.color.WHITE, 10)
                
    def on_draw(self):
        arcade.start_render()
        self.draw_soils_state()
        self.shovel_sprite.draw()
        self.wateringcan_sprite.draw()
        self.trash_sprite.draw()
        self.vega_sprite.draw()
        self.vegb_sprite.draw()
        self.me_sprite.draw()
        self.draw_me_state()
        minutes = int(self.world.total_time) // 60
        seconds = int(self.world.total_time) % 60
        money = int(self.world.me.MONEY)

        output = "Time: {:02d}:{:02d}".format(minutes, seconds)
        moneyShow = "Money: {:02d}" .format(money)
        arcade.draw_text(output, 400, 400, arcade.color.WHITE, 20)
        arcade.draw_text(moneyShow, 100, 400, arcade.color.WHITE, 20)

    def animate(self, delta):
        self.world.animate(delta)
        
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
        
    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)
        
if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
