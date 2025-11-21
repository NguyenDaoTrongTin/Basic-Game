import arcade as arc


class MyGame(arc.Window):
    def __init__(self):
        super().__init__(600, 400, "MyGame", resizable= True)
        arc.set_background_color(arc.color.WHITE)
        self.ninja = None
        self.jump_c = self.attack_c = self.walk_right_c = 0
        self.walk_left_c = self.attack_left_c = self.attack_right_c = 0
        self.shuriken_right_c = self.shuriken_left_c = self.shu_c = 0
        self.jumping = False
        self.attacking = False
        self.shuriken = False
        self.nin_shu = False
        self.ninja_bottom = None
        self.walking_right = self.walking_left = False
        self.background = None
        self.sprites_list = arc.SpriteList()
        self.key_list = self.jump = self.walk_right = self.walk_left = []
        self.attack_right = self.attack_left = self.shuriken_right = self.shuriken_left = []
        self.shu = None
        self.R_L = self.U_D = None
        self.start_texture = 0
        self.timing = self.timing_jump = self.timing_attack = self.timing_shuriken = 0.0

    def set_up(self):
        self.ninja = arc.Sprite("ninja_rgba.png")
        self.ninja.center_x = 400
        self.ninja.bottom = 135
        self.ninja_bottom = self.ninja.bottom
        self.sprites_list.append(self.ninja)

        self.walk_right = [arc.load_texture(f"ninja walking right {i}_rgba.png") for i in range(1,4)]
        self.walk_left = [arc.load_texture(f"ninja walking left {i}_rgba.png") for i in range(1, 4)]

        self.background = arc.Sprite("back ground.png")
        self.background.left = 0
        self.background.bottom = -150
        self.sprites_list.append(self.background)

        self.jump = []
        for t in range(21):
            y = 2.5*t*(20-t)
            self.jump.append(y)

        self.attack_left = [arc.load_texture(f"ninja attack left {i}_rgba.png") for i in range(1, 4)]
        self.attack_right = [arc.load_texture(f"ninja attack right {i}_rgba.png") for i in range(1, 4)]

        self.shuriken_left = [arc.load_texture(f"ninja shuriken left {i}_rgba.png") for i in range(1,4)]
        self.shuriken_right = [arc.load_texture(f"ninja shuriken right {i}_rgba.png") for i in range(1,4)]

        self.shu = arc.Sprite("shuriken 1_rgba.png")
        self.shu.center_x = 400
        self.shu.center_y = 185
        self.shu.scale = 0.25
        self.shu.textures.extend([arc.load_texture(f"shuriken {i}_rgba.png") for i in range(2,5)])

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
            if self.key_list[-1] == arc.key.J or self.key_list[-1] == arc.key.KEY_1:
                self.attacking = True

            if self.key_list[-1] == arc.key.RIGHT or self.key_list[-1] == arc.key.D:
                self.walking_right = True
                self.walking_left = False

            if self.key_list[-1] == arc.key.LEFT or self.key_list[-1] == arc.key.A:
                self.walking_left = True
                self.walking_right = False

            if self.key_list[-1] == arc.key.K or self.key_list[-1] == arc.key.KEY_2:
                self.jumping = True

            if self.key_list[-1] == arc.key.U or self.key_list[-1] == arc.key.KEY_4:
                self.shuriken = True

            if self.key_list[-1] == arc.key.UP:
                pass
            if self.key_list[-1] == arc.key.DOWN:
                pass
        else:
            self.ninja.texture = self.ninja.textures[0]

        if self.walking_right:
            self.walking_or_attack_right()
        if self.walking_left:
            self.walking_or_attack_left()
        if self.jumping:
            self.nin_jump()
        if self.nin_shu:
            self.shuri()

    def walking_or_attack_right(self):
        self.walk_right_c += 1
        if self.walk_right_c > len(self.walk_right):
            self.walk_right_c = 1
        self.timing += 0.25
        if self.timing > 1.0:
            if self.attacking:
                self.attack_c += 1
                if self.attack_c > len(self.attack_right):
                    self.attack_c = 1
                self.ninja.texture = self.attack_right[self.attack_c - 1]
                if self.attack_c == len(self.attack_right):
                    self.attacking = False

            elif self.shuriken:
                self.shuriken_right_c += 1
                if self.shuriken_right_c < len(self.shuriken_right) + 1:
                    self.ninja.texture = self.shuriken_right[self.shuriken_right_c - 1]
                if self.shuriken_right_c == len(self.shuriken_right):
                    self.nin_shu = True
                    self.shuriken = False
                    self.shuriken_right_c = 0

            else: self.ninja.texture = self.walk_right[self.walk_right_c-1]
            self.background.left -= 40
            if -self.background.left > 4913 - (self.width // 40 + 1) * 40:
                self.background.left = 0
            self.timing = 0.0

    def walking_or_attack_left(self):
        self.walk_left_c += 1
        if self.walk_left_c > len(self.walk_left):
            self.walk_left_c = 1
        self.timing += 0.25
        if self.timing > 1.0:
            if self.attacking:
                self.attack_c += 1
                if self.attack_c > len(self.attack_left):
                    self.attack_c = 1
                self.ninja.texture = self.attack_left[self.attack_c - 1]
                if self.attack_c == len(self.attack_left):
                    self.attacking = False

            elif self.shuriken:
                self.shuriken_left_c += 1
                if self.shuriken_left_c < len(self.shuriken_left) + 1:
                    self.ninja.texture = self.shuriken_left[self.shuriken_left_c - 1]
                if self.shuriken_left_c == len(self.shuriken_left):
                    self.shuriken = False
                    self.shuriken_left_c = 0

            else: self.ninja.texture = self.walk_left[self.walk_left_c-1]
            if self.background.left < -40:
                self.background.left += 40
            self.timing = 0.0

    def nin_jump(self):
        self.timing_jump += 0.5
        if self.timing_jump > 1.0:
            self.jump_c += 1
            if self.jump_c < len(self.jump) + 1:
                self.ninja.bottom = self.ninja_bottom + self.jump[self.jump_c - 1]
                if self.jump_c == len(self.jump):
                    self.jumping = False
                    self.jump_c = 0
            self.timing_jump = 0.0

    def shuri(self):
        if self.shu not in self.sprites_list:
            self.sprites_list.append(self.shu)
        self.shu_c += 1
        if self.shu_c > len(self.shu.textures):
            self.shu_c = 1
        self.shu.texture = self.shu.textures[self.shu_c - 1]
        self.shu.center_x += 10
        if self.shu.center_x > self.width + 50:
            self.shu.center_x = 400
            self.sprites_list.remove(self.shu)
            self.nin_shu = False


    def on_draw(self):
        self.clear()
        self.sprites_list.draw()


if __name__ == "__main__":
    game = MyGame()
    game.set_up()
    arc.run()