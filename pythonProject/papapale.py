import arcade

# Mengatur ukuran layar
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class sprite:

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Membuat list sprite
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Skor
        self.score = 0

        # Menyiapkan pemain
        # Gambar karakter dari kenney.nl
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50 # Posisi awal pemain
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Membuat koin
        for i in range(COIN_COUNT):

            # Membuat instance koin
            # Gambar koin dari kenney.nl
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)

            # Posisi koin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Menambah koin ke lists
            self.coin_list.append(coin)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()

    def update(self, delta_time):
        # Membuat list koin yang bertabrakan dengan pemain
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Lakukan looping ke sprite yang ditabrak, lalu, hapus dari game, dan tambahkan skor
        for coin in coins_hit_list:
            coin.kill()
            self.score += 1