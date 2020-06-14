import arcade
import Enemigos
import os
import random
import math

RIGHT_FACING = 0
LEFT_FACING = 1
UP_FACING = 2
DOWN_FACING = 3

UPDATES_PER_FRAME = 10
NUM_TEXTURAS_ANDAR = 3


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


class boss(arcade.Sprite):

    def __init__(self):
        super().__init__()

        self.character_face_direction = RIGHT_FACING

        self.cur_texture = 0

        self.vida = 50

        self.change_x = 0
        self.change_y = 0

        self.textura_quieto = load_texture_4dir("sprites_master" + os.path.sep + "BOSS1.png",
                                                "sprites_master" + os.path.sep + "BOSS10.png",
                                                "sprites_master" + os.path.sep + "BOSS7.png")

        self.textura_andar = []
        for i in range(10, 13):
            self.textura_andar.append(
                load_texture_4dir("sprites_master" + os.path.sep + f"BOSS{i - 6}.png",
                                  "sprites_master" + os.path.sep + f"BOSS{i}.png",
                                  f"sprites_master" + os.path.sep + f"BOSS{i - 3}.png"))
        self.sonido_disparar = arcade.load_sound("Sonidos" + os.path.sep + "ataque boss.wav")

    def recibir_damage(self, damage):
        self.vida -= damage

    def movimiento(self, player_sprite, velocidad_enemigos):

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

    def update_animation(self, delta_time: float = 1 / 60):
        # Saber si hay que mirar hacia la derecha, izquierda, arriba o abajo.
        if self.change_x < 0 and (self.character_face_direction == RIGHT_FACING or UP_FACING or DOWN_FACING):
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and (self.character_face_direction == LEFT_FACING or UP_FACING or DOWN_FACING):
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and (self.character_face_direction == RIGHT_FACING or LEFT_FACING or UP_FACING):
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0 and (self.character_face_direction == RIGHT_FACING or LEFT_FACING or DOWN_FACING):
            self.character_face_direction = UP_FACING

        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.textura_quieto[self.character_face_direction]
            return

        self.cur_texture += 1
        if self.cur_texture >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
            self.cur_texture = 0
        self.texture = self.textura_andar[self.cur_texture // UPDATES_PER_FRAME][self.character_face_direction]

    def generar_enemigos(self, lista_enemigos):
        if random.randrange(1000) == 1:
            masked = Enemigos.Masked()
            masked.center_x = random.choice((self.center_x - 40, self.center_x + 40))
            masked.center_y = random.choice((self.center_y - 40, self.center_y + 40))
            lista_enemigos.append(masked)
        if random.randrange(1000) == 1:
            gasmasked = Enemigos.Gasmasked()
            gasmasked.center_x = random.choice((self.center_x - 40, self.center_x + 40))
            gasmasked.center_y = random.choice((self.center_y - 40, self.center_y + 40))
            lista_enemigos.append(gasmasked)
        if random.randrange(1000) == 1:
            skeleton = Enemigos.Skeleton()
            skeleton.center_x = random.choice((self.center_x - 40, self.center_x + 40))
            skeleton.center_y = random.choice((self.center_y - 40, self.center_y + 40))
            lista_enemigos.append(skeleton)

    def disparar(self, boss, velocidad_disparo, lista_balas_boss, diagonal=False, diagonal_invertida=False):
        tuerca = arcade.Sprite("sprites_master" + os.path.sep + "ENGRANAJE.png")
        self.sonido_disparar.play()

        if self.character_face_direction == RIGHT_FACING:
            if diagonal:  # Arriba -->
                tuerca.left = boss.right
                tuerca.center_y = boss.center_y
                tuerca.change_x = velocidad_disparo
                tuerca.change_y = velocidad_disparo
            elif diagonal_invertida:  # Abajo -->
                tuerca.left = boss.right
                tuerca.center_y = boss.center_y
                tuerca.change_x = velocidad_disparo
                tuerca.change_y = -velocidad_disparo
            else:  # -->
                tuerca.left = boss.right
                tuerca.center_y = boss.center_y
                tuerca.change_x = velocidad_disparo
        elif self.character_face_direction == LEFT_FACING:
            if diagonal:  # Abajo <--
                tuerca.right = boss.left
                tuerca.center_y = boss.center_y
                tuerca.change_x = -velocidad_disparo
                tuerca.change_y = -velocidad_disparo
            elif diagonal_invertida:  # Arriba <--
                tuerca.right = boss.left
                tuerca.center_y = boss.center_y
                tuerca.change_x = -velocidad_disparo
                tuerca.change_y = velocidad_disparo
            else:  # <--
                tuerca.right = boss.left
                tuerca.center_y = boss.center_y
                tuerca.change_x = -velocidad_disparo
        elif self.character_face_direction == UP_FACING:
            if diagonal:  # Arriba -->
                tuerca.bottom = boss.top
                tuerca.center_x = boss.center_x
                tuerca.change_x = velocidad_disparo
                tuerca.change_y = velocidad_disparo
            elif diagonal_invertida:  # Arriba <--
                tuerca.bottom = boss.top
                tuerca.center_x = boss.center_x
                tuerca.change_x = -velocidad_disparo
                tuerca.change_y = velocidad_disparo
            else:  # Arriba
                tuerca.bottom = boss.top
                tuerca.center_x = boss.center_x
                tuerca.change_y = velocidad_disparo
        elif self.character_face_direction == DOWN_FACING:
            if diagonal:  # Abajo <--
                tuerca.top = boss.bottom
                tuerca.center_x = boss.center_x
                tuerca.change_x = -velocidad_disparo
                tuerca.change_y = -velocidad_disparo
            elif diagonal_invertida:  # Abajo -->
                tuerca.top = boss.bottom
                tuerca.center_x = boss.center_x
                tuerca.change_x = velocidad_disparo
                tuerca.change_y = -velocidad_disparo
            else:  # Abajo
                tuerca.top = boss.bottom
                tuerca.center_x = boss.center_x
                tuerca.change_y = -velocidad_disparo
        lista_balas_boss.append(tuerca)
        return tuerca
