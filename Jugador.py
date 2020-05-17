import arcade
import os

# Constantes para mirar a que lado mira
RIGHT_FACING = 0
LEFT_FACING = 1
UP_FACING = 2
DOWN_FACING = 3

# Veces que se actualizan las texturas por segundo
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


class Jugador(arcade.Sprite):

    def __init__(self):
        """Constructor del sprite del jugador"""
        super().__init__()

        # Dirección a la que mira por defecto
        self.character_face_direction = RIGHT_FACING  # tiene valores del 0 al 3
        # Booleanos para saber el estado del personaje
        self.bloq_direccion = False
        self.disparando = False
        self.estado_fantasmal = False
        self.invencible = False     # sin implementar en el main/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
        # Usado para quitar la pistola a los 2s
        self.contador_remove_pistola = 0
        # Usado para restringir el tiempo en modo fantasmal a los 10s
        self.contador_de_muerte = 0
        # Used for flipping between image sequences
        self.cur_texture = 0

        # ---Cargar texturas---
        self.textura_quieto = load_texture_4dir("sprites_master" + os.path.sep + "PERSONAJE10.png",
                                                "sprites_master" + os.path.sep + "PERSONAJE7.png",
                                                "sprites_master" + os.path.sep + "PERSONAJE4.png")
        self.textura_quieto_pistola = load_texture_4dir("sprites_master" + os.path.sep + "PERSONAJE14.png",
                                                        "sprites_master" + os.path.sep + "PERSONAJE16.png",
                                                        "sprites_master" + os.path.sep + "PERSONAJE15.png")
        self.textura_andando = []
        for i in (11, 12):
            # Cargamos texturas 11 y 12 (derecha moviendo los pies)
            # 8 y 9 (arriba moviendo los pies)
            # 5 y 6 (abajo moviendo los pies)
            self.textura_andando.append(load_texture_4dir("sprites_master" + os.path.sep + "PERSONAJE{}.png".format(i),
                                                          "sprites_master" + os.path.sep + "PERSONAJE{}.png".format(
                                                              i - 3),
                                                          "sprites_master" + os.path.sep + "PERSONAJE{}.png".format(
                                                              i - 6)))
        # Sonidos
        self.sonido_disparar = arcade.load_sound("Sonidos" + os.path.sep + "Disparo prota.wav")
        self.textura_andando_pistola = []
        for i in (17, 18):
            # Cargamos texturas 21 y 22 (derecha moviendo los pies)
            # 23 y 24 (arriba moviendo los pies)
            # 17 y 18 (abajo moviendo los pies)
            self.textura_andando_pistola.append(
                load_texture_4dir("sprites_master" + os.path.sep + "PERSONAJE{}.png".format(i + 4),
                                  "sprites_master" + os.path.sep + "PERSONAJE{}.png".format(
                                      i + 6),
                                  "sprites_master" + os.path.sep + "PERSONAJE{}.png".format(
                                      i)))

    def disparar(self, jugador, velocidad_disparo):
        """ArcadeSprite, int ---> ArcadeSprite
        Crea y calcula la trayectoria de la bala y retorna esta"""
        # Poner el booleano a True para cambiar texturas y que se muestre la pistola
        self.disparando = True
        # Resetear el contador para que la textura de la pistola dure 2s desde la última vez que se disparó
        self.contador_remove_pistola = 0
        # Crear la bala
        bala = arcade.Sprite("sprites_master" + os.path.sep + "BALA.png")
        # Ponemos el sonido
        self.sonido_disparar.play()
        # Calcular su trayectoria y su posicion de spawn
        if self.character_face_direction == RIGHT_FACING:
            bala.left = jugador.right
            bala.center_y = jugador.center_y
            bala.change_x = velocidad_disparo
        elif self.character_face_direction == LEFT_FACING:
            bala.right = jugador.left
            bala.center_y = jugador.center_y
            bala.change_x = -velocidad_disparo
        elif self.character_face_direction == UP_FACING:
            bala.bottom = jugador.top
            bala.center_x = jugador.center_x
            bala.change_y = velocidad_disparo
        elif self.character_face_direction == DOWN_FACING:
            bala.top = jugador.bottom
            bala.center_x = jugador.center_x
            bala.change_y = -velocidad_disparo
        return bala

    def bloquear_direccion(self):
        self.bloq_direccion = True

    def desbloquear_direccion(self):
        self.bloq_direccion = False

    def activar_modo_fantasmal(self):
        self.estado_fantasmal = True  # se utilizará para meter los sprites adecuados en update_animation
        self.contador_de_muerte = 600  # 10s
        self.invencible = True
        return 8  # nueva velocidad del jugador

    def update_animation(self, delta_time: float = 1 / 60):
        """Utilizado para actualizar la animación del jugador"""
        # Vemos adonde tenemos que mirar
        if not self.bloq_direccion:
            if self.change_x < 0 and (self.character_face_direction == RIGHT_FACING or UP_FACING or DOWN_FACING):
                self.character_face_direction = LEFT_FACING
            elif self.change_x > 0 and (self.character_face_direction == LEFT_FACING or UP_FACING or DOWN_FACING):
                self.character_face_direction = RIGHT_FACING
            elif self.change_y < 0 and (self.character_face_direction == RIGHT_FACING or LEFT_FACING or UP_FACING):
                self.character_face_direction = DOWN_FACING
            elif self.change_y > 0 and (self.character_face_direction == RIGHT_FACING or LEFT_FACING or DOWN_FACING):
                self.character_face_direction = UP_FACING

        if self.estado_fantasmal:
            self.contador_de_muerte -= 1
            if self.contador_de_muerte == 0:
                self.estado_fantasmal = False
                # el resto de cosas que pasan cuando se acaba este modo se manejan en el update del main

        # Si no hemos disparado en 2s quitar la pistola
        if self.disparando:
            self.contador_remove_pistola += 1
            if self.contador_remove_pistola == 120:  # LLevamos 2s sin disparar
                self.disparando = False
                self.contador_remove_pistola = 0
            # Animación estando quieto con pistola
            if self.change_x == 0 and self.change_y == 0:
                self.texture = self.textura_quieto_pistola[self.character_face_direction]
                return  # si entramos en este if no debemos mirar nada más de actualizar texturas
            # Animación moviendose con pistola
            else:
                self.cur_texture += 1
                if self.cur_texture >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
                    self.cur_texture = 0
                self.texture = self.textura_andando_pistola[self.cur_texture // UPDATES_PER_FRAME][
                    self.character_face_direction]
        elif not self.disparando:
            # Animación estando quieto
            if self.change_x == 0 and self.change_y == 0:
                self.texture = self.textura_quieto[self.character_face_direction]
                return  # si entramos en este if no debemos mirar nada más de actualizar texturas

            # Animacion andando sin pistola
            self.cur_texture += 1
            if self.cur_texture >= NUM_TEXTURAS_ANDAR * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.textura_andando[self.cur_texture // UPDATES_PER_FRAME][
                self.character_face_direction]
