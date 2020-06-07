import arcade
import os
import math
import Main
import Jugador
import random


RIGHT_FACING = 0
LEFT_FACING = 1
UP_FACING = 2
DOWN_FACING = 3

UPDATES_PER_FRAME = 10
NUM_TEXTURAS_ANDAR = 2


def load_texture_4dir(filename_lados, filename_up, filename_down):
    """
    Carga texturas en las 4 direcciones, siendo la seguna un versión espejo del
    primer argumento.
    """
    return [
        arcade.load_texture(filename_lados),
        arcade.load_texture(filename_lados, mirrored=True),
        arcade.load_texture(filename_up),
        arcade.load_texture(filename_down)
    ]


class Masked(arcade.Sprite):
    def __init__(self):
        """Constructor del sprite del jugador"""
        super().__init__()
        self.character_face_direction = RIGHT_FACING

        self.cur_texture = 0

        self.vida = 2

        self.jugador = Jugador()  # OJO!

        self.change_x = 0
        self.change_y = 0

        self.textura_quieto = load_texture_4dir("sprites_master/MASKED1.png", "sprites_master/MASKED10.png",
                                                "sprites_master/MASKED7.png")

        self.textura_andar = []
        for i in range(11, 12):
            texture = load_texture_4dir(f"sprites_master/MASKED{i - 6}.png", f"sprites_master/MASKED{i}.png",
                                        f"sprites_master/MASKED{i - 3}.png")
            self.textura_andar.append(texture)

        self.texture = self.textura_quieto[3]

        self.set_hit_box(self.texture.hit_box_points)

    def recibir_damage(self, damage):
        self.vida -= damage


    def follow_sprite(self, path):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        self.center_x += self.change_x
        self.center_y += self.change_y

        # Random 1 in 100 chance that we'll change from our old direction and
        # then re-aim toward the player
        if random.randrange(1) == 0:
            start_x = self.center_x
            start_y = self.center_y

            # Get the destination location for the bullet
            for i in range(len(path)):
                dest_x = path[i][0]
                if self.center_x == dest_x:
                    continue



            for i in range(len(path)):
                dest_y = path[i][1]
                if self.center_y == dest_y:
                    continue


            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the bullet travels.
            self.change_x = math.cos(angle) * COIN_SPEED
            self.change_y = math.sin(angle) * COIN_SPEED

    def actualizar_animacion(self, delta_time: float = 1 / 60):

        # Saber si hay que mirar hacia la derecha, izquierda, arriba o abajo.
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or UP_FACING:
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or DOWN_FACING:
            self.character_face_direction = UP_FACING

        if self.change_x == 0:
            self.texture = self.textura_quieto[self.character_face_direction]
            return

        self.cur_texture += 1
        if self.cur_texture >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
            self.cur_texture = 0
        self.texture = self.textura_andando[self.cur_texture // UPDATES_PER_FRAME][
            self.character_face_direction]


class Skeleton(arcade.Sprite):
    def __init__(self):
        """Constructor del sprite del jugador"""
        super().__init__()

        self.character_face_direction = RIGHT_FACING

        self.cur_texture = 0

         #self.lista_balas_enemigos = arcade.SpriteList()
        self.change_x = 0
        self.change_y = 0

        self.vida = 1

        self.textura_quieto = load_texture_4dir("sprites_master/ESQUELETO1.png", "sprites_master/ESQUELETO10.png",
                                                "sprites_master/ESQUELETO7.png")

        self.textura_andar = []
        for i in range(11, 12):

            self.textura_andar.append(load_texture_4dir(f"sprites_master/ESQUELETO{i - 6}.png", f"sprites_master/ESQUELETO{i}.png",
                                        f"sprites_master/ESQUELETO{i - 3}.png"))

        self.texture = self.textura_quieto[3]

        self.set_hit_box(self.texture.hit_box_points)

        self.lista_laser = arcade.SpriteList()

        self.sonido_laser = arcade.load_sound("Sonidos/Disparo pew.wav")

    def follow_sprite(self, player_sprite, velocidad_enemigos):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        self.center_x += self.change_x
        self.center_y += self.change_y

        # Random 1 in 100 chance that we'll change from our old direction and
        # then re-aim toward the player
        if random.randrange(1) == 0:
            start_x = self.center_x
            start_y = self.center_y

            # Get the destination location for the bullet
            dest_x = player_sprite.center_x
            dest_y = player_sprite.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the bullet travels.
            self.change_x = math.cos(angle) * velocidad_enemigos
            self.change_y = math.sin(angle) * velocidad_enemigos

    def disparar(self, skeleton, velocidad_disparo_enemigos, jugador, lista_balas_enemigos):
        laser = arcade.Sprite("sprites_master/LASER.png")
        self.change_y = 0
        self.change_x = 0

        if self.character_face_direction == RIGHT_FACING:
            laser.left = skeleton.right
            laser.center_y = skeleton.center_y
            laser.change_x = velocidad_disparo_enemigos
        elif self.character_face_direction == LEFT_FACING:
            laser.right = skeleton.left
            laser.center_y = skeleton.center_y
            laser.change_x = -velocidad_disparo_enemigos
        elif self.character_face_direction == UP_FACING:
            laser.bottom = skeleton.top
            laser.center_x = skeleton.center_x
            laser.change_y = velocidad_disparo_enemigos
        elif self.character_face_direction == DOWN_FACING:
            laser.top = skeleton.bottom
            laser.center_x = skeleton.center_x
            laser.change_y = -velocidad_disparo_enemigos

        start_x = skeleton.center_x
        start_y = skeleton.center_y
        # Get the destination location for the bullet
        dest_x = jugador.center_x
        dest_y = jugador.center_y

        # Do math to calculate how to get the bullet to the destination.
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Shoot every 60 frames change of shooting each frame

        laser.center_x = start_x
        laser.center_y = start_y

        # Angle the bullet sprite
        laser.angle = math.degrees(angle)

        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        laser.change_x = math.cos(angle) * velocidad_disparo_enemigos
        laser.change_y = math.sin(angle) * velocidad_disparo_enemigos
        lista_balas_enemigos.append(laser)
        return laser


        #arcade.play_sound(self.sonido_laser)

    def recibir_damage(self, damage):
        self.vida -= damage

    def actualizar_animacion(self, delta_time: float = 1 / 60):

        # Saber si hay que mirar hacia la derecha, izquierda, arriba o abajo.
        if self.change_x < 0 and (self.character_face_direction == RIGHT_FACING or UP_FACING or DOWN_FACING):
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and (self.character_face_direction == LEFT_FACING or UP_FACING or DOWN_FACING):
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and (self.character_face_direction == RIGHT_FACING or LEFT_FACING or UP_FACING):
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0 and (self.character_face_direction == RIGHT_FACING or LEFT_FACING or DOWN_FACING):
            self.character_face_direction = UP_FACING

        if self.change_x == 0:
            self.texture = self.textura_quieto[self.character_face_direction]
            return

        self.cur_texture += 1
        if self.cur_texture >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
            self.cur_texture = 0
        self.texture = self.textura_andando[self.cur_texture // UPDATES_PER_FRAME][
            self.character_face_direction]




class Gasmasked(arcade.Sprite):
    def __init__(self):
        """Constructor del sprite del jugador"""
        super().__init__()

        self.character_face_direction = RIGHT_FACING

        self.cur_texture = 0

        self.change_x = 0
        self.change_y = 0

        self.vida = 3

        self.textura_quieto = load_texture_4dir("sprites_master/GASMASK1.png", "sprites_master/GASMASK10.png",
                                                "sprites_master/GASMASK7.png")

        self.textura_andar = []
        for i in range(11, 12):
            texture = load_texture_4dir(f"sprites_master/GASMASK{i - 6}.png", f"sprites_master/GASMASK{i}.png",
                                        f"sprites_master/GASMASK{i - 3}.png")
            self.textura_andar.append(texture)

        self.texture = self.textura_quieto[0]

        self.set_hit_box(self.texture.hit_box_points)

        self.sonido_disparar = arcade.load_sound("Sonidos/Ataque Gas.wav")

        self.lista_gases = arcade.SpriteList()

    def follow_sprite(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        self.center_x += self.change_x
        self.center_y += self.change_y

        # Random 1 in 100 chance that we'll change from our old direction and
        # then re-aim toward the player
        if random.randrange(100) == 0:
            start_x = self.center_x
            start_y = self.center_y

            # Get the destination location for the bullet
            dest_x = player_sprite.center_x
            dest_y = player_sprite.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the bullet travels.
            self.change_x = math.cos(angle) * COIN_SPEED
            self.change_y = math.sin(angle) * COIN_SPEED

    def disparar(self, gasmasked, velocidad_disparo_enemigos, jugador, lista_balas_enemigos):

        proyectil_gaseoso = arcade.Sprite("sprites_master/GASATTACK.png")
        self.change_y = 0
        self.change_x = 0
        self.sonido_disparar.play()

        if self.character_face_direction == RIGHT_FACING:
            proyectil_gaseoso.left = gasmasked.right
            proyectil_gaseoso.center_y = gasmasked.center_y
            proyectil_gaseoso.change_x = velocidad_disparo_enemigos
        elif self.character_face_direction == LEFT_FACING:
            proyectil_gaseoso.right = gasmasked.left
            proyectil_gaseoso.center_y = gasmasked.center_y
            proyectil_gaseoso.change_x = -velocidad_disparo_enemigos
        elif self.character_face_direction == UP_FACING:
            proyectil_gaseoso.bottom = gasmasked.top
            proyectil_gaseoso.center_x = gasmasked.center_x
            proyectil_gaseoso.change_y = velocidad_disparo_enemigos
        elif self.character_face_direction == DOWN_FACING:
            proyectil_gaseoso.top = gasmasked.bottom
            proyectil_gaseoso.center_x = gasmasked.center_x
            proyectil_gaseoso.change_y = -velocidad_disparo_enemigos
        #self.lista_laser.append(proyectil_gaseoso)

        start_x = gasmasked.center_x
        start_y = gasmasked.center_y
        # Get the destination location for the bullet
        dest_x = jugador.center_x
        dest_y = jugador.center_y

        # Do math to calculate how to get the bullet to the destination.
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Shoot every 60 frames change of shooting each frame

        proyectil_gaseoso.center_x = start_x
        proyectil_gaseoso.center_y = start_y

        # Angle the bullet sprite
        proyectil_gaseoso.angle = math.degrees(angle)

        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        proyectil_gaseoso.change_x = math.cos(angle) * velocidad_disparo_enemigos
        proyectil_gaseoso.change_y = math.sin(angle) * velocidad_disparo_enemigos
        lista_balas_enemigos.append(laser)

        return proyectil_gaseoso


    def recibir_damage(self, damage):
        self.vida -= damage

    def actualizar_animacion(self, delta_time: float = 1 / 60):

        # Saber si hay que mirar hacia la derecha, izquierda, arriba o abajo.
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING or UP_FACING or DOWN_FACING:
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or UP_FACING:
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0 and self.character_face_direction == LEFT_FACING or RIGHT_FACING or DOWN_FACING:
            self.character_face_direction = UP_FACING

        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        self.cur_texture += 1
        if self.cur_texture >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
            self.cur_texture = 0
        self.texture = self.textura_andando[self.cur_texture // UPDATES_PER_FRAME][
            self.character_face_direction]

        self.lista_gases.update()
