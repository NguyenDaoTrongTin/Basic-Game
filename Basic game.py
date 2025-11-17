import arcade as arc


class MyGame(arc.Window):
    def __init__(self):
        super().__init__(600, 400, "MyGame", resizable= True)
        arc.set_background_color(arc.color.WHITE)
        self.ninja = None
        self.sprites_list = arc.SpriteList()
        self.key_list = []
        self.R_L = self.U_D = None
        self.start_texture = 0
        self.timing = 0.0

    def set_up(self):
        self.ninja = arc.Sprite("ninja.png")
        self.ninja.center_x = 200
        self.ninja.center_y = 200
        self.sprites_list.append(self.ninja)

        self.ninja.textures.extend([arc.load_texture(f"ninja walking right {i}.png") for i in range(1,4)])
        self.ninja.textures.extend([arc.load_texture(f"ninja walking left {i}.png") for i in range(1, 4)])

    def on_key_press(self, key, modifiers):
        self.key_list.append(key)

    def on_key_release(self, key, modifiers):
        self.key_list.remove(key)

    def on_update(self, delta_time):
        if self.key_list:
            if self.key_list[-1] == arc.key.RIGHT:
                self.start_texture += 1
                if self.start_texture > 3:
                    self.start_texture = 1
                self.timing += 0.25
                if self.timing > 1.0:
                    self.ninja.texture = self.ninja.textures[self.start_texture]
                    self.timing = 0.0

            elif self.key_list[-1] == arc.key.LEFT:
                self.start_texture += 1
                if self.start_texture > 3:
                    self.start_texture = 1
                self.timing += 0.25
                if self.timing > 1.0:
                    self.ninja.texture = self.ninja.textures[self.start_texture+3]
                    self.timing = 0.0

            elif self.key_list[-1] == arc.key.UP:
                pass
            elif self.key_list[-1] == arc.key.DOWN:
                pass


    def on_draw(self):
        self.clear()
        self.sprites_list.draw()


if __name__ == "__main__":
    game = MyGame()
    game.set_up()
    arc.run()