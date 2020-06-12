import arcade
import os


def dibujar_hud(vida, carga_fantasmal):
    """Dibuja en pantalla el hud si se invoca en el método on_draw"""
    # Vida
    if vida == 10:
        vida_x = 0
    elif vida == 9:
        vida_x = -20  # Cada barra de vida una son 20 pixeles
    elif vida == 8:
        vida_x = -40
    elif vida == 7:
        vida_x = -60
    elif vida == 6:
        vida_x = -80
    elif vida == 5:
        vida_x = -100
    elif vida == 4:
        vida_x = -120
    elif vida == 3:
        vida_x = -140
    elif vida == 2:
        vida_x = -160
    elif vida == 1:
        vida_x = -180
    else:
        return  # no tenemos que dibujar vida

    barra_de_vida = arcade.load_texture("sprites_master" + os.path.sep + "VIDA.png", x=vida_x, y=0, width=200,
                                        height=50, mirrored=True)
    arcade.draw_texture_rectangle(160, 865, 200, 50, barra_de_vida)  # centrox, centroy, ancho, alto, textura
    icono_de_vida = arcade.load_texture("sprites_master" + os.path.sep + "VIDAPOWERUP.png")
    arcade.draw_texture_rectangle(35, 867.5, 50, 50, icono_de_vida)
    # Carga Fantasmal
    carga_fantasmal_s = str(carga_fantasmal)  # lo convertimos a String
    if carga_fantasmal >= 100:
        arcade.draw_text(carga_fantasmal_s, 50, 800, arcade.color.GREEN_YELLOW, 24)
    else:
        arcade.draw_text(carga_fantasmal_s, 50, 800, arcade.color.WHITE, 24)
    icono_carga = arcade.load_texture("sprites_master" + os.path.sep + "alma.png")
    arcade.draw_texture_rectangle(30, 815, 25, 25, icono_carga)


def dibujar_contador_de_muerte(contador):
    arcade.draw_text(str(int(contador / 60)), 445, 825, arcade.color.RED_ORANGE, 40, bold=True, align="center")
    arcade.draw_text("¡Acaba con todos los enemigos de la sala!", 250, 800, arcade.color.RED_ORANGE, 20, bold=True,
                     align="center")


def dibujar_pantalla_de_inicio():
    arcade.draw_texture_rectangle(450, 450, 900, 900,
                                  arcade.load_texture("sprites_master" + os.path.sep + "PANTALLAINICIO.jpg"))
    arcade.draw_text("Pulsa enter para comenzar", -50, 450, arcade.color.GUPPIE_GREEN, 20, 450, "center", bold=True)
    arcade.draw_text("Pulsa 'C' para ver los controles", 500, 450, arcade.color.GUPPIE_GREEN, 20, 450, "center")


def dibujar_controles():
    arcade.draw_lrtb_rectangle_filled(0, 900, 900, 0, arcade.color.BLACK)
    arcade.draw_text("Moverse: W,A,S,D ó las flechas", 0, 550, arcade.color.WOOD_BROWN, 20, 900, "center")
    arcade.draw_text("Disparar: Q", 0, 450, arcade.color.WOOD_BROWN, 20, 900, "center")
    arcade.draw_text("Bloquear dirección: Espacio", 0, 350, arcade.color.WOOD_BROWN, 20, 900, "center")
    arcade.draw_text("Pausar/Reaunudar el juego: P", 0, 250, arcade.color.WOOD_BROWN, 20, 900, "center")
    arcade.draw_text("Pulsa retroceso para volver", 0, 100, arcade.color.WOOD_BROWN, 20, 900, "center")


def dibujar_hud_pausado(buffs):
    arcade.draw_lrtb_rectangle_filled(0, 900, 900, 0, arcade.color.BLACK)
    arcade.draw_text("Pausado", 0, 800, arcade.color.WOOD_BROWN, 40, 900, "center", bold=True)
    arcade.draw_text("Pulsa P para volver", 0, 100, arcade.color.WOOD_BROWN, 30, 900, align="center", bold=True)
    if buffs[0]:
        # Info modo fantasmal
        icono_carga = arcade.load_texture("sprites_master" + os.path.sep + "alma.png")
        arcade.draw_text(
            "Modo fantasmal: Una vez tu vida llegue a 0, consumirás 100 de       y te convertirás en un fantasma",
            0, 750, arcade.color.GREEN_YELLOW, 17, 900, align="center", bold=True)
        arcade.draw_texture_rectangle(585, 760, 25, 25, icono_carga)
        arcade.draw_text(
            "Si matas a todos los enemigos de la sala en 10 segundos siendo un fantasma, volverás a la vida.",
            0, 700, arcade.color.GREEN_YELLOW, 17, 900, align="center", bold=True)
    if buffs[1] or buffs[2]:
        arcade.draw_text("Mejoras modo fantasmal:", 450, 550, arcade.color.GREEN_YELLOW, 17, 450, align="center",
                         bold=True)
    if buffs[1]:
        # Info mejora velocidad modo fant
        arcade.draw_text(
            "Velocidad: x1.5",
            450, 500, arcade.color.GREEN_YELLOW, 17, 450, align="center", bold=True)
    if buffs[2]:
        # Info mejora triple disparo modo fant
        arcade.draw_text(
            "Triple disparo",
            450, 450, arcade.color.GREEN_YELLOW, 17, 450, align="center", bold=True)
    if buffs[3] or buffs[4]:
        arcade.draw_text("Mejoras generales:", 0, 550, arcade.color.GOLDEN_BROWN, 17, 450, align="center",
                         bold=True)
        arcade.draw_text(
            "Las mejoras generales también afectan al modo fantasmal",
            0, 650, arcade.color.GOLDEN_BROWN, 17, 900, align="center", bold=True)
    if buffs[3]:
        # Info mejora velocidad permanente
        arcade.draw_text(
            "Velocidad: x1.2",
            0, 500, arcade.color.GOLDEN_BROWN, 17, 450, align="center", bold=True)
    if buffs[4]:
        # Info mejora daño permanente
        arcade.draw_text(
            "Daño doble",
            0, 450, arcade.color.GOLDEN_BROWN, 17, 450, align="center", bold=True)


def dibujar_hud_gameover():
    arcade.draw_lrtb_rectangle_filled(0, 900, 900, 0, arcade.color.BLACK)
    arcade.draw_text("GAME OVER", 0, 450, arcade.color.RED_DEVIL, 36, 900, align="center", bold=True)
    arcade.draw_text("Pulsa R para reiniciar", 0, 250, arcade.color.RED_DEVIL, 24, 900, align="center")
    arcade.draw_text("(Puede tardar unos segundos)", 0, 150, arcade.color.RED_DEVIL, 24, 900, align="center")


def mostrar_mensaje_buff(n):
    arcade.draw_lrtb_rectangle_filled(300, 800, 875, 825, arcade.color.DARK_SEA_GREEN)
    if n == 1:
        # Buff inicial para habilitar el modo fantasmal
        arcade.draw_text("Ahora ya puedes habilitar el modo fantasamal!", 300, 850,
                         arcade.color.WHITE, align="center", bold=True, font_size=18)
    elif n == 2:
        # Buff mejora de velocidad modo fantasmal
        arcade.draw_text("Ahora vas más rápido durante el modo fantasmal!", 300, 850,
                         arcade.color.WHITE, align="center", bold=True, font_size=18)
    elif n == 3:
        # Disparo triple modo fantasmal
        arcade.draw_text("Ahora disparas tres balas durante el modo fantasmal!", 300, 850,
                         arcade.color.WHITE, align="center", bold=True, font_size=18)
    elif n == 4:
        # Velocidad 1.2 permanente
        arcade.draw_text("Ahora vas más rápido!", 300, 850,
                         arcade.color.WHITE, align="center", bold=True, font_size=18)
    elif n == 5:
        # Daño doble permanente
        arcade.draw_text("Ahora haces más daño!", 300, 850,
                         arcade.color.WHITE, align="center", bold=True, font_size=18)

    arcade.draw_text("Ve al menú de pausa para más información", 300, 825,
                     arcade.color.WHITE, align="center", bold=True, font_size=16)


def dibujar_partes_artefacto(buffs):
    if buffs[0]:
        piedra = arcade.load_texture("sprites_master" + os.path.sep + "PARTE1.png")
        arcade.draw_texture_rectangle(840, 840, 40, 50, piedra)
    if buffs[1]:
        vasija = arcade.load_texture("sprites_master" + os.path.sep + "PARTE3.png")
        arcade.draw_texture_rectangle(840, 810, 50, 20, vasija)
    if buffs[2]:
        jaula = arcade.load_texture("sprites_master" + os.path.sep + "PARTE2.png")
        arcade.draw_texture_rectangle(840, 840, 40, 50, jaula)
