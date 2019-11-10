import arcade

# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Click on Ada!"
GAME_SPEED = 1/60
TIMER_MAX = 50

class Ada_or_Potato(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.image_list = None
        self.ada_sprite = None
        self.potato_sprite = None
        self.time = None
        self.score = None

    def setup(self):
        """ Setup the game (or reset the game) """
        self.time = 0
        self.score = 0
        arcade.set_background_color(arcade.color.AQUA)
        self.image_list = arcade.SpriteList()
        self.ada_sprite = arcade.Sprite('images/ada.png')
        self.ada_sprite.center_x = WINDOW_WIDTH/2
        self.ada_sprite.center_y = WINDOW_HEIGHT/2
        self.image_list.append(self.ada_sprite)
        self.potato_sprite = arcade.Sprite('images/potato.png', .15)
        self.potato_sprite.angle = 90
        self.potato_sprite.center_x = WINDOW_WIDTH/2
        self.potato_sprite.center_y = WINDOW_HEIGHT/2
        self.image_list.append(self.potato_sprite)

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        if self.time < TIMER_MAX/4:
            self.image_list[0].draw()
            arcade.draw_text("Score " + str(self.score), 15, 15, arcade.color.BLACK, 25)
        else:
            self.image_list[1].draw()
            arcade.draw_text("Score " + str(self.score), 15, 15, arcade.color.BLACK, 25)


    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        if self.time < TIMER_MAX:
            self.time += 1
        else:
            self.time = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if self.time < TIMER_MAX/4:
            self.score += 1
        else:
            self.score -= 1

def main():
    window = Ada_or_Potato()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
