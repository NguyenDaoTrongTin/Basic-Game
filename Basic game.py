import arcade as arc


class MyGame(arc.Window):
    def __init__(self):
        super().__init__(600, 400, "MyGame", resizable= True)
        arc.set_background_color(arc.color.WHITE)
        self.ninja = None
        self.jump_c = 0
        self.jumping = False
        self.ninja_bottom = None
        self.walking_right = self.walking_left = False
        self.background = None
        self.sprites_list = arc.SpriteList()
        self.key_list = self.jump = []
        self.R_L = self.U_D = None
        self.start_texture = 0
        self.timing = self.timing_jump = 0.0

    def set_up(self):
        self.ninja = arc.Sprite("ninja_rgba.png")
        self.ninja.center_x = 400
        self.ninja.bottom = 135
        self.ninja_bottom = self.ninja.bottom
        self.sprites_list.append(self.ninja)

        self.ninja.textures.extend([arc.load_texture(f"ninja walking right {i}_rgba.png") for i in range(1,4)])
        self.ninja.textures.extend([arc.load_texture(f"ninja walking left {i}_rgba.png") for i in range(1, 4)])

        self.background = arc.Sprite("back ground.png")
        self.background.left = 0
        self.background.bottom = -150
        self.sprites_list.append(self.background)

        self.jump = []
        for t in range(21):
            y = 2.5*t*(20-t)
            self.jump.append(y)



    def on_key_press(self, key, modifiers):
        self.key_list.append(key)

    def on_key_release(self, key, modifiers):
        self.key_list.remove(key)
        if key == arc.key.RIGHT or key == arc.key.D:
            self.walking_right = False
        if key == arc.key.LEFT or key == arc.key.A:
            self.walking_left = False

    def on_update(self, delta_time):
        if self.key_list:
            if self.key_list[-1] == arc.key.RIGHT or self.key_list[-1] == arc.key.D:
                self.start_texture += 1
                if self.start_texture > 3:
                    self.start_texture = 1
                self.timing += 0.25
                if self.timing > 1.0:
                    self.ninja.texture = self.ninja.textures[self.start_texture]
                    self.background.left -= 40
                    if -self.background.left > 4913 - (self.width // 40 + 1) * 40:
                        self.background.left = 0
                    self.timing = 0.0

            if self.key_list[-1] == arc.key.LEFT or self.key_list[-1] == arc.key.A:
                self.start_texture += 1
                if self.start_texture > 3:
                    self.start_texture = 1
                self.timing += 0.25
                if self.timing > 1.0:
                    self.ninja.texture = self.ninja.textures[self.start_texture + 3]
                    if self.background.left < -40:
                        self.background.left += 40
                    self.timing = 0.0

            if self.key_list[-1] == arc.key.K or self.key_list[-1] == arc.key.KEY_2:
                self.jumping = True
            if self.key_list[-1] == arc.key.UP:
                pass
            if self.key_list[-1] == arc.key.DOWN:
                pass
        else:
            self.ninja.texture = self.ninja.textures[0]


        if self.jumping:
            self.timing_jump += 0.5
            if self.timing_jump > 1.0:
                self.jump_c += 1
                if self.jump_c < len(self.jump) + 1:
                    self.ninja.bottom = self.ninja_bottom + self.jump[self.jump_c - 1]
                    if self.jump_c == len(self.jump):
                        self.jumping = False
                        self.jump_c = 0
                self.timing_jump = 0.0



    def on_draw(self):
        self.clear()
        self.sprites_list.draw()


if __name__ == "__main__":
    game = MyGame()
    game.set_up()
    arc.run()
