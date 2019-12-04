import arcade

# Define constants
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 700
GAME_TITLE = "Seize!"
GAME_SPEED = 1/60
TIMER_MAX = 50

class Epilepsy(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.color = arcade.color.BLACK
        self.timer = 0

    def setup(self):
        arcade.set_background_color(self.color)

    def on_draw(self):
        arcade.start_render()


    def on_update(self, delta_time):
        self.timer += 10
        if self.timer > 50:
            self.timer = 0
        if self.timer > 35:
            arcade.set_background_color(arcade.color.AUREOLIN)
        else:
            arcade.set_background_color(arcade.color.AUBURN)

def main():
    window = Epilepsy()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
