import arcade



my_window = arcade.open_window(1000,900, "Our First Window Demo")
arcade.set_background_color(arcade.color.BLUE)
arcade.start_render()


arcade.draw_lrtb_rectangle_filled(50, 150, 200, 50, arcade.color.SILVER)
arcade.draw_xywh_rectangle_outline(10, 50, 380, 250, arcade.color.GRAY, 6)
arcade.draw_triangle_filled(700,275, 295, 285, 475,
330, arcade.color.BLACK)






arcade.finish_render()

arcade.run()




