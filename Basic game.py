import arcade as arc
from pyglet.event import EVENT_HANDLE_STATE


class MyGame(arc.Window):
    def __init__(self):
        super().__init__(600, 400, "MyGame", resizable= True)
        arc.set_background_color(arc.color.WHITE)
        self.ninja = None
        self.sprites_list = arc.SpriteList()
        self.key_list = []
        self.R_L = self.U_D = None

    def set_up(self):
        self.ninja = arc.AnimatedWalkingSprite()
        self.ninja.center_x = 200
        self.ninja.center_y = 200


        self.ninja.stand_right_textures.append(arc.load_texture("ninja.png"))
        self.ninja.stand_left_textures.append(arc.load_texture("ninja.png"))

        self.ninja.walk_up_textures.append(arc.load_texture("ninja.png"))
        self.ninja.walk_up_textures.append(arc.load_texture("ninja.png"))
        self.ninja.walk_up_textures.append(arc.load_texture("ninja.png"))

        self.ninja.walk_down_textures.append(arc.load_texture("ninja.png"))
        self.ninja.walk_down_textures.append(arc.load_texture("ninja.png"))
        self.ninja.walk_down_textures.append(arc.load_texture("ninja.png"))

        self.ninja.walk_left_textures.append(arc.load_texture("ninja walking left 1.png"))
        self.ninja.walk_left_textures.append(arc.load_texture("ninja walking left 2.png"))
        self.ninja.walk_left_textures.append(arc.load_texture("ninja walking left 3.png"))

        self.ninja.walk_right_textures.append(arc.load_texture("ninja walking right 1.png"))
        self.ninja.walk_right_textures.append(arc.load_texture("ninja walking right 2.png"))
        self.ninja.walk_right_textures.append(arc.load_texture("ninja walking right 3.png"))


        self.sprites_list.append(self.ninja)

    def on_key_press(self, key, modifiers):
        self.key_list.append(key)

    def on_key_release(self, key, modifiers):
        self.key_list.remove(key)

    def on_update(self, delta_time):
        if self.key_list:
            if self.key_list[-1] == arc.key.RIGHT:
                self.ninja.change_x = 5
            elif self.key_list[-1] == arc.key.LEFT:
                self.ninja.change_x = -5
            elif self.key_list[-1] == arc.key.UP:
                self.ninja.change_y = 5
            elif self.key_list[-1] == arc.key.DOWN:
                self.ninja.change_y = -5

        if arc.key.RIGHT not in self.key_list and arc.key.LEFT not in self.key_list:
            self.ninja.change_x = 0
        if arc.key.UP not in self.key_list and arc.key.DOWN not in self.key_list:
            self.ninja.change_y = 0

        self.ninja.update()
        self.ninja.update_animation(delta_time)


    def on_draw(self):
        self.clear()
        self.sprites_list.draw()


if __name__ == "__main__":
    game = MyGame()
    game.set_up()
    arc.run()