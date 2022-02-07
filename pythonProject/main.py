import arcade

# Mengatur ukuran layar
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


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

def godong(x, y):
    """ This function draws a pine tree at the specified location. """

    # Menggambar segitiga di bagian atas.
    # Kita butuh tiga poin x, y untuk menggambar segitiga
    arcade.draw_triangle_filled(x + 40, y,  # Poin 1
                                x, y - 100,  # Poin 2
                                x + 80, y - 100,  # Poin 3
                                arcade.color.DARK_GREEN)
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    pohon(250, 150)
    godong(250, 200)
    godong(250, 250)
    godong(250, 300)
    godong(250, 350)
    godong(250, 400)
    godong(250, 450)
    godong(250, 500)
    godong(250, 550)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()