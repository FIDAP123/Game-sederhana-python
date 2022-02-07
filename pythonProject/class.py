import arcade
KECEPATA_GERAK = 5
UKURAN_SPRITE_PLAYER = 0.05
UKURAN_SPRITE_KOIN = 0.05

LEBAR_LAYAR = 800               # width
TINGGI_LAYAR = 600              # height
JUDUL_GAME = "MANJAT POHON :V"  # tittle

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, lebar, tinggi, judul):
        super().__init__(lebar, tinggi, judul)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here
        '''list sprite'''
        self.player_list = arcade.SpriteList()
        self.koin_list = arcade.SpriteList()


        '''Player'''
        self.player_sprite = arcade.Sprite("character.png", UKURAN_SPRITE_PLAYER)
        self.player_sprite.center_x = 290  # Posisi awal pemain
        self.player_sprite.center_y = 16
        self.player_list.append(self.player_sprite)

        """Koin"""

        # Membuat instance koin
        koin = arcade.Sprite("coin_01.png", UKURAN_SPRITE_KOIN)
        # Posisi koin
        koin.center_x = 290
        koin.center_y = 550
        # Menambah koin ke lists
        self.koin_list.append(koin)

    def on_draw(self):
        """ Render the screen. """
        """ Draw everything """
        arcade.start_render()
        def pohon(x, y):
            """ This function draws a pine tree at the specified location. """

            # Menggambar segitiga di bagian atas.
            # Kita butuh tiga poin x, y untuk menggambar segitiga
            arcade.draw_triangle_filled(x + 40, y,  # Poin 1
                                        x, y - 100,  # Poin 2
                                        x + 80, y - 100,  # Poin 3
                                        arcade.color.DARK_GREEN)

            # Menggambar batang pohonnya
            arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                              arcade.color.DARK_BROWN)
        def daun(x, y):
            """ This function draws a pine tree at the specified location. """

            # Menggambar segitiga di bagian atas.
            # Kita butuh tiga poin x, y untuk menggambar segitiga
            arcade.draw_triangle_filled(x + 40, y,  # Poin 1
                                        x, y - 100,  # Poin 2
                                        x + 80, y - 100,  # Poin 3
                                        arcade.color.DARK_GREEN)
        def main():
            pohon(250, 150)
            daun(250, 200)
            daun(250, 250)
            daun(250, 300)
            daun(250, 350)
            daun(250, 400)
            daun(250, 450)
            daun(250, 500)
            daun(250, 550)
        # Call the main function to get the program started.
        main()
        self.player_list.draw()
        self.koin_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        # Membuat list koin yang bertabrakan dengan pemain
        koin_ditabrak = arcade.check_for_collision_with_list(self.player_sprite, self.koin_list)

        # Lakukan looping ke sprite yang ditabrak, lalu, hapus dari game, dan tambahkan skor
        for coin in koin_ditabrak:
            coin.kill()
            quit()
        self.player_list.update()
        self.koin_list.update()




    def on_key_press(self, key, modifiers):
        """Dipanggil setiap tombol di tekan. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = KECEPATA_GERAK
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -KECEPATA_GERAK

    def on_key_release(self, key, modifiers):
        """Dipanggil setiap tombol dilepas. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0



def main():
    window = MyGame(LEBAR_LAYAR, TINGGI_LAYAR, JUDUL_GAME) # (lebar, tinggi, judul)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()