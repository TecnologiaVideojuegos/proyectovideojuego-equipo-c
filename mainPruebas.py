import arcade
import Jugador
import os
import math
import Enemigos
# --- Constantes ---

# SPRITE_SCALING_BOX = 0.5
# SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

MOVEMENT_SPEED = 5


class Room:
    """
    This class holds all the information about the
    different rooms.
    """

    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None
        self.background = None
        self.enemigos_list = None
        self.balas_list = None




def setup_room_1():
    """
    Create and return room 1.
    """
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()




    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "PRISION1.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "ROCAS Y CAJAS")
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "PRISION1.png")

    # Definir muros
    room.wall_list = obstaculos
    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemigos_list = arcade.SpriteList()
    room.balas_list = arcade.SpriteList()

    skeleton = Enemigos.Skeleton()
    skeleton.center_x = 450
    skeleton.center_y = 200
    room.enemigos_list.append(skeleton)

    masked = Enemigos.Masked()
    masked.center_x = 450
    masked.center_y = 800
    room.enemigos_list.append(masked)

    gasmasked = Enemigos.Gasmasked()
    gasmasked.center_x = 750
    gasmasked.center_y = 475
    room.enemigos_list.append(gasmasked)

    # Tile map
    mapa_hab2 = arcade.tilemap.read_tmx("Mapas y Objetos" + os.path.sep + "RUINAS3.tmx")
    obstaculos = arcade.process_layer(mapa_hab2, "CAJAS Y ROCAS")  # OJO!
    room.background = arcade.load_texture("sprites_master" + os.path.sep + "RUINAS3.png")

    # Definir muros
    room.wall_list = obstaculos

    return room


class SteamPunkGame(arcade.Window):
    """ Ventana principal del juego """

    def __init__(self):
        """ Constructor """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Juego")  # Poner nombre del juego
        # Sprite lists
        self.player_list = None
        self.bullet_list = None

        # Habitacion
        self.current_room = 0
        self.rooms = None
        # Set up the player
        self.jugador = None
        self.physics_engine = None

        # Variables para el disparo del jugador
        self.velocidad_disparo = 10


    def setup(self):
        arcade.set_background_color(arcade.color.WOOD_BROWN)
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Create the player
        self.jugador = Jugador.Jugador()  # OJO!
        self.jugador.center_x = 350
        self.jugador.center_y = 350
        self.player_list.append(self.jugador)



        # Rooms
        self.rooms = []  # lista de todas las habitaciones
        room = setup_room_1()  # convendria hacer un for cuando se pongan mas
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)
        self.current_room = 0  # habitacion inicial
        # Fisicas para la habitacion en la que estemos
        self.physics_engine = arcade.PhysicsEngineSimple(self.jugador, self.rooms[self.current_room].wall_list)

    def on_draw(self):
        arcade.start_render()
        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.rooms[self.current_room].background)
        self.rooms[self.current_room].wall_list.draw()
        self.player_list.draw()
        self.bullet_list.draw()
        self.rooms[self.current_room].enemigos_list.draw()




    def on_update(self, delta_time: float = 1 / 60):
        # Actualizar todos los sprites
        self.physics_engine.update()
        self.jugador.update_animation()
        self.bullet_list.update()

        for enemy in self.rooms[self.current_room].enemigos_list:

            # First, calculate the angle to the player. We could do this
            # only when the bullet fires, but in this case we will rotate
            # the enemy to face the player each frame, so we'll do this
            # each frame.

            # Position the start at the enemy's current location
            start_x = enemy.center_x
            start_y = enemy.center_y

            # Get the destination location for the bullet
            dest_x = self.player.center_x
            dest_y = self.player.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Set the enemy to face the player.
            enemy.angle = math.degrees(angle) - 90

            # Shoot every 60 frames change of shooting each frame
            if self.frame_count % 60 == 0:
                bullet = arcade.Sprite("sprites_master/LASER.png")
                bullet.center_x = start_x
                bullet.center_y = start_y

                # Angle the bullet sprite
                bullet.angle = math.degrees(angle)

                # Taking into account the angle, calculate our change_x
                # and change_y. Velocity is how fast the bullet travels.
                bullet.change_x = math.cos(angle) * BULLET_SPEED
                bullet.change_y = math.sin(angle) * BULLET_SPEED

                room.balas_list.append(bullet)



        # Mirar en que habitación estamos y si necesitamos cambiar a otra
        if self.jugador.center_x > SCREEN_WIDTH - 110 and self.current_room == 0:  # 0-->1
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                             self.rooms[self.current_room].wall_list)
            self.jugador.center_x = 110
            self.bullet_list = arcade.SpriteList()  # Resetear la lista de balas
        elif self.jugador.center_x < 110 and self.current_room == 1:  # 1-->0
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.jugador,
                                                             self.rooms[self.current_room].wall_list)
            self.bullet_list = arcade.SpriteList()  # Resetear la lista de balas
            self.jugador.center_x = SCREEN_WIDTH - 110

        # Actualizar balas jugador
        # Loop through each bullet
        for bala in self.bullet_list:
            # Mirar si ha chocado con una pared
            hit_list = arcade.check_for_collision_with_list(bala, self.rooms[self.current_room].wall_list)
            # Si choca contra una pared, eliminar la bala
            if len(hit_list) > 0:
                bala.remove_from_sprite_lists()
            # Mirar si choca contra un enemigo
            hit_list2 = arcade.check_for_collision_with_list(bala,self.rooms[self.current_room].enemigos_list)
            if len(hit_list2) > 0:
                bala.remove_from_sprite_lists()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        # Movimiento
        if key == arcade.key.UP or key == arcade.key.W:
            self.jugador.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.jugador.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.jugador.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.jugador.change_x = MOVEMENT_SPEED
        # Disparo
        if key == arcade.key.Q:
            bala = self.jugador.disparar(self.jugador, self.velocidad_disparo)
            self.bullet_list.append(bala)
        # Bloquear direccion a la que mira el personaje (hay que mantener)
        if key == arcade.key.SPACE:
            self.jugador.bloquear_direccion()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.DOWN or key == arcade.key.W or key == arcade.key.S:
            self.jugador.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.A or key == arcade.key.D:
            self.jugador.change_x = 0
        # Desbloquear direccion a la que mira el personaje
        if key == arcade.key.SPACE:
            self.jugador.desbloquear_direccion()


def main():
    ventana = SteamPunkGame()
    ventana.setup()
    arcade.run()


if __name__ == "__main__":
    main()